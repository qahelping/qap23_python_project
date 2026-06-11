"""
ORM-модели с той же схемой, что в backend TMS.

Имена таблиц и колонок совпадают с app/models/* — без импорта кода приложения.
"""
import datetime
import uuid
from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from core.db_client import Base


def utcnow_naive() -> datetime:
    """Текущее UTC-время без tzinfo (как в SQLite DATETIME)."""
    return datetime.now(timezone.utc).replace(tzinfo=None)


def unique_token(length: int = 8) -> str:
    """Уникальная строка для username/email в тестах."""
    return uuid.uuid4().hex[:length]


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="admin", nullable=False)
    avatar_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=utcnow_naive, nullable=False)

    boards = relationship("Board", back_populates="creator", cascade="all, delete-orphan")
    tasks = relationship(
        "Task",
        foreign_keys="Task.created_by",
        back_populates="creator",
        cascade="all, delete-orphan",
    )
    assigned_tasks = relationship(
        "Task",
        foreign_keys="Task.assignee_id",
        back_populates="assignee",
    )
    board_memberships = relationship(
        "BoardMember",
        back_populates="user",
        cascade="all, delete-orphan",
    )


class Board(Base):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    public = Column(Boolean, default=False, nullable=False)
    archived = Column(Boolean, default=False, nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=utcnow_naive, nullable=False)

    creator = relationship("User", back_populates="boards")
    tasks = relationship("Task", back_populates="board", cascade="all, delete-orphan")
    members = relationship("BoardMember", back_populates="board", cascade="all, delete-orphan")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String, default="todo", nullable=False)
    priority = Column(String, default="medium", nullable=False)
    order = Column(Integer, default=0, nullable=False)
    parent_task_id = Column(Integer, ForeignKey("tasks.id"), nullable=True)
    board_id = Column(Integer, ForeignKey("boards.id"), nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    assignee_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=utcnow_naive, nullable=False)
    updated_at = Column(DateTime, default=utcnow_naive, onupdate=utcnow_naive, nullable=False)

    board = relationship("Board", back_populates="tasks")
    creator = relationship("User", foreign_keys=[created_by], back_populates="tasks")
    assignee = relationship("User", foreign_keys=[assignee_id], back_populates="assigned_tasks")
    parent_task = relationship("Task", remote_side=[id], backref="subtasks")
    comments = relationship("TaskComment", back_populates="task", cascade="all, delete-orphan")


class BoardMember(Base):
    __tablename__ = "board_members"

    id = Column(Integer, primary_key=True, autoincrement=True)
    board_id = Column(Integer, ForeignKey("boards.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    board = relationship("Board", back_populates="members")
    user = relationship("User", back_populates="board_memberships")


class TaskComment(Base):
    __tablename__ = "task_comments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=utcnow_naive, nullable=False)

    task = relationship("Task", back_populates="comments")
    user = relationship("User")


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    action = Column(String, nullable=False)
    entity_type = Column(String, nullable=False)
    entity_id = Column(Integer, nullable=True)
    details = Column(Text, nullable=True)
    created_at = Column(DateTime, default=utcnow_naive, nullable=False)

    user = relationship("User")
