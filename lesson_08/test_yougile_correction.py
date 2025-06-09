import requests
import random
import pytest

BASE_URL = "https://ru.yougile.com/api-v2"
AUTH_TOKEN = "Bearer "

HEADERS = {
    "Authorization": AUTH_TOKEN,
    "Content-Type": "application/json",
}


def generate_project_name():
    return f"Autotest Project {random.randint(1000, 9999)}"


def get_random_project_id():
    """Получает случайный ID проекта из списка"""
    response = requests.get(f"{BASE_URL}/projects", headers=HEADERS)
    assert response.status_code == 200, f"Ошибка получения проектов: {response.status_code}"

    projects = response.json().get("content", [])
    assert projects, "Нет доступных проектов для тестирования"

    return random.choice(projects).get("id")


@pytest.fixture
def new_project():
    """Фикстура для создания временного проекта"""
    payload = {"title": generate_project_name()}
    response = requests.post(f"{BASE_URL}/projects", json=payload, headers=HEADERS)
    assert response.status_code == 201

    project_data = response.json()
    project_id = project_data.get("id")
    assert project_id, "ID проекта не был возвращен"
    assert isinstance(project_id, str), "ID проекта должен быть строкой"
    assert len(project_id) > 0, "ID проекта не может быть пустой строкой"

    yield project_id

    # Архивация проекта после теста
    requests.put(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)


def test_create_project_positive():
    """Тест успешного создания проекта"""
    payload = {"title": generate_project_name()}
    response = requests.post(f"{BASE_URL}/projects", json=payload, headers=HEADERS)

    assert response.status_code == 201
    project_id = response.json().get("id")
    assert project_id
    assert isinstance(project_id, str)
    assert len(project_id) > 0


def test_create_project_negative():
    """Тест создания проекта с невалидными данными"""
    payload = {"title": ""}
    response = requests.post(f"{BASE_URL}/projects", json=payload, headers=HEADERS)
    assert response.status_code == 400


def test_get_project_positive(new_project):
    """Тест успешного получения проекта"""
    response = requests.get(f"{BASE_URL}/projects/{new_project}", headers=HEADERS)

    assert response.status_code == 200
    project_data = response.json()
    assert project_data.get("id") == new_project
    assert project_data.get("title")


def test_get_project_negative():
    """Тест получения несуществующего проекта"""
    response = requests.get(f"{BASE_URL}/projects/nonexistent_id_12345", headers=HEADERS)
    assert response.status_code == 404


def test_delete_project(new_project):
    """Тест удаления проекта позитивный"""
    get_response = requests.get(f"{BASE_URL}/projects/{new_project}", headers=HEADERS)
    assert get_response.status_code == 200

    current_title = get_response.json().get("title", "")

    payload = {
        "deleted": True,
        "title": current_title
    }

    response = requests.put(
        f"{BASE_URL}/projects/{new_project}",
        json=payload,
        headers=HEADERS
    )

    assert response.status_code == 200
    response_data = response.json()
    assert "id" in response_data
    assert response_data["id"] == new_project


def test_delete_project_negative(new_project):
    """Тест удаления проекта негативный"""
    get_response = requests.get(f"{BASE_URL}/projects/{new_project}", headers=HEADERS)
    current_title = get_response.json().get("title", "")

    payload = {
        "deleted": True,
        "title": current_title
    }

    response = requests.put(
        f"{BASE_URL}/projects/nonexistent_id_12345",
        json=payload,
        headers=HEADERS
    )

    assert response.status_code == 404


