import pytest
from sqlalchemy import inspect
from database import engine, get_db


# Описываем структуру существующей таблицы
class User:
    __tablename__ = 'users'

    def __init__(self, user_id, user_email, subject_id):
        self.user_id = user_id
        self.user_email = user_email
        self.subject_id = subject_id


def test_create_user():
    # Получаем сессию с явным управлением
    db = next(get_db())

    try:
        # Проверяем существование таблицы
        inspector = inspect(engine)
        assert 'users' in inspector.get_table_names()

        # Очистка тестовых данных
        db.execute(f"DELETE FROM users WHERE user_email = 'test@example.com'")
        db.commit()

        # Вставка через Core API для надёжности
        db.execute(
            "INSERT INTO users (user_id, user_email, subject_id) VALUES (:id, :email, :subject)",
            {"id": 123456789, "email": "test@example.com", "subject": 1}
        )
        db.commit()

        # Проверка
        result = db.execute(
            "SELECT subject_id FROM users WHERE user_email = :email",
            {"email": "test@example.com"}
        ).fetchone()

        assert result is not None
        assert result[0] == 1

    finally:
        # Гарантированная очистка
        db.execute(f"DELETE FROM users WHERE user_email = 'test@example.com'")
        db.commit()
        db.close()


def test_update_user():
    db = next(get_db())
    try:
        # Подготовка
        test_email = "test@example.com"
        db.execute(f"DELETE FROM users WHERE user_email = '{test_email}'")
        db.execute(
            "INSERT INTO users (user_id, user_email, subject_id) VALUES (:id, :email, :subject)",
            {"id": 123456789, "email": "test@example.com", "subject": 1}
        )
        db.commit()

        # Обновление
        db.execute(
            "UPDATE users SET subject_id = 2 WHERE user_email = :email",
            {"email": test_email}
        )
        db.commit()

        # Проверка
        result = db.execute(
            "SELECT subject_id FROM users WHERE user_email = :email",
            {"email": test_email}
        ).fetchone()
        assert result[0] == 2

    finally:
        db.execute(f"DELETE FROM users WHERE user_email = 'test@example.com'")
        db.commit()
        db.close()


def test_delete_user():
    db = next(get_db())
    try:
        # Подготовка
        test_email = "test@example.com"
        db.execute(f"DELETE FROM users WHERE user_email = '{test_email}'")
        db.execute(
            "INSERT INTO users (user_id, user_email, subject_id) VALUES (:id, :email, :subject)",
            {"id": 123456789, "email": "test@example.com", "subject": 1}
        )
        db.commit()

        # Удаление
        db.execute(
            "DELETE FROM users WHERE user_email = :email",
            {"email": test_email}
        )
        db.commit()

        # Проверка
        result = db.execute(
            "SELECT 1 FROM users WHERE user_email = :email",
            {"email": test_email}
        ).fetchone()
        assert result is None

    finally:
        db.close()