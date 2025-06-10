import requests
import random

BASE_URL = "https://ru.yougile.com/api-v2"
AUTH_TOKEN = "Bearer "

HEADERS = {
    "Authorization": AUTH_TOKEN,
    "Content-Type": "application/json",
}


def generate_project_name():
    return f"Autotest Project {random.randint(1000, 9999)}"


def test_create_project_positive():
    """Успешное создание проекта"""
    project_name = generate_project_name()
    response = requests.post(
        f"{BASE_URL}/projects",
        json={"title": project_name},
        headers=HEADERS
    )
    assert response.status_code == 201
    assert "id" in response.json()
    return response.json()["id"]


def test_create_project_negative():
    """неуспешное создание проекта"""
    project_name = ""
    response = requests.post(
        f"{BASE_URL}/projects",
        json={"title": project_name},
        headers=HEADERS
    )
    assert response.status_code == 400


def test_get_project_positive():
    """Успешное получение проекта"""
    project_id = test_create_project_positive()
    response = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS
    )
    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_get_project_negative():
    """Неудачное получение проекта (несуществующий ID)"""
    response = requests.get(
        f"{BASE_URL}/projects/nonexistent_id_12345",
        headers=HEADERS
    )
    assert response.status_code == 404


def test_put_project_positive():
    """Успешное изменение статуса проекта"""
    project_id = test_create_project_positive()

    response = requests.put(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS
    )
    assert response.status_code == 200
    assert "id" in response.json()


def test_put_project_negative():
    """Неудачное изменение статуса проекта (несуществующий проект)"""
    response = requests.put(
        f"{BASE_URL}/projects/nonexistent_id_12345",
        headers=HEADERS
    )
    assert response.status_code == 404
