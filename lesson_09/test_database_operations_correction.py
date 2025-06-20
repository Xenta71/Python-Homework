import pytest
from sqlalchemy import inspect
from sqlalchemy.sql import text
from database import engine, get_db


# Описываем структуру существующей таблицы
class User:
    __tablename__ = "users"

    def __init__(self, user_id, user_email, subject_id):
        self.user_id = user_id
        self.user_email = user_email
        self.subject_id = subject_id


@pytest.fixture
def test_email():
    return "test@example.com"


@pytest.fixture
def cleanup_user(test_email):
    db = next(get_db())
    try:
        db.execute(
            text("DELETE FROM users WHERE user_email = :email"), {"email": test_email}
        )
        db.commit()
    finally:
        db.close()


def test_create_user(cleanup_user, test_email):
    db = next(get_db())
    try:
        # Проверяем существование таблицы
        inspector = inspect(engine)
        assert "users" in inspector.get_table_names()

        # Вставка через Core API для надёжности
        db.execute(
            text(
                "INSERT INTO users (user_id, user_email, subject_id) "
                "VALUES (:id, :email, :subject)"
            ),
            {"id": 123456789, "email": test_email, "subject": 1},
        )
        db.commit()

        # Проверка
        result = db.execute(
            text("SELECT subject_id FROM users WHERE user_email = :email"),
            {"email": test_email},
        ).fetchone()

        assert result is not None
        assert result[0] == 1
    finally:
        db.close()


def test_update_user(cleanup_user, test_email):
    db = next(get_db())
    try:
        # Подготовка
        db.execute(
            text(
                "INSERT INTO users (user_id, user_email, subject_id) "
                "VALUES (:id, :email, :subject)"
            ),
            {"id": 123456789, "email": test_email, "subject": 1},
        )
        db.commit()

        # Обновление
        db.execute(
            text("UPDATE users SET subject_id = 2 WHERE user_email = :email"),
            {"email": test_email},
        )
        db.commit()

        # Проверка
        result = db.execute(
            text("SELECT subject_id FROM users WHERE user_email = :email"),
            {"email": test_email},
        ).fetchone()
        assert result[0] == 2
    finally:
        db.close()


def test_delete_user(cleanup_user, test_email):
    db = next(get_db())
    try:
        # Подготовка
        db.execute(
            text(
                "INSERT INTO users (user_id, user_email, subject_id) "
                "VALUES (:id, :email, :subject)"
            ),
            {"id": 123456789, "email": test_email, "subject": 1},
        )
        db.commit()

        # Удаление
        db.execute(
            text("DELETE FROM users WHERE user_email = :email"), {"email": test_email}
        )
        db.commit()

        # Проверка
        result = db.execute(
            text("SELECT 1 FROM users WHERE user_email = :email"), {"email": test_email}
        ).fetchone()
        assert result is None
    finally:
        db.close()
