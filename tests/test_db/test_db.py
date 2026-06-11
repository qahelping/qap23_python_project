import pytest
from sqlalchemy import inspect

from db_models.models import TaskComment, BoardMember


@pytest.mark.db1
def test_users_table_exist(db_session):
    inspector = inspect(db_session.bind)
    print(inspector.get_table_names())

    assert "users2" in inspector.get_table_names()


def test_create_task_comment(self, db_session, sample_task, sample_user):
    comment = TaskComment(
        task_id=sample_task.id,
        user_id=sample_user.id,
        content="This is a test comment.",
    )
    db_session.add(comment)
    db_session.commit()
    db_session.refresh(comment)

    assert comment.id is not None
    assert comment.content == "This is a test comment."
    assert comment.created_at is not None


def test_board_member_user_relationship(self, db_session, sample_board, sample_admin):
    membership = BoardMember(board_id=sample_board.id, user_id=sample_admin.id)
    db_session.add(membership)
    db_session.commit()
    db_session.refresh(membership)

    assert membership.user.username == sample_admin.username


def test_task_updated_at_changes_on_update(self, db_session, sample_task):
    original_updated = sample_task.updated_at
    sample_task.title = "Updated title"
    db_session.commit()
    db_session.refresh(sample_task)

    assert sample_task.updated_at >= original_updated
