import shutil
from pathlib import Path

import pytest

from db.base import create_session
from db.models import Board, Task, User
from utils.helpers import unique_token
from utils.password import hash_password

BASE_DB = Path(__file__).resolve().parents[1] / "fixtures" / "app.db"


@pytest.fixture
def db_session(tmp_path):
    """Сессия к временной копии БД. Оригинальный fixtures/app.db не меняется."""
    if not BASE_DB.exists():
        pytest.exit(f"Файл БД не найден: {BASE_DB}", returncode=1)

    test_db = tmp_path / "app.db"
    shutil.copy(BASE_DB, test_db)
    engine, session = create_session(test_db)
    try:
        yield session
    finally:
        session.close()
        engine.dispose()


@pytest.fixture
def sample_user(db_session):
    suffix = unique_token()
    user = User(
        username=f"pytest_user_{suffix}",
        email=f"pytest_user_{suffix}@test.local",
        password_hash=hash_password("password123"),
        role="user",
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


@pytest.fixture
def sample_admin(db_session):
    suffix = unique_token()
    admin = User(
        username=f"pytest_admin_{suffix}",
        email=f"pytest_admin_{suffix}@test.local",
        password_hash=hash_password("admin123"),
        role="admin",
    )
    db_session.add(admin)
    db_session.commit()
    db_session.refresh(admin)
    return admin


@pytest.fixture
def sample_board(db_session, sample_user):
    board = Board(
        title=f"Pytest Board {unique_token()}",
        description="Board for DB tests",
        created_by=sample_user.id,
    )
    db_session.add(board)
    db_session.commit()
    db_session.refresh(board)
    return board


@pytest.fixture
def sample_task(db_session, sample_user, sample_board):
    task = Task(
        title=f"Pytest Task {unique_token()}",
        description="Task for DB tests",
        board_id=sample_board.id,
        created_by=sample_user.id,
    )
    db_session.add(task)
    db_session.commit()
    db_session.refresh(task)
    return task
