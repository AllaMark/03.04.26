import requests

base_url = "https://ru.yougile.com/api-v2"


def test_create_project():
    my_header = {"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json"}
    body = {"title": "ГосУслуги"}
    response = requests.post(url=f"{base_url}/projects", headers=my_header, json=body)
    assert response.status_code == 201


def test_create_negative_project():
    my_header = {"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json"}
    body = {"title": ""}
    response = requests.post(url=f"{base_url}/projects", headers=my_header, json=body)
    assert response.status_code == 400


def test_change_project():
    # Создание нового проекта
    my_header = {"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json"}
    body = {"title": "Проект"}
    response = requests.post(url=f"{base_url}/projects", headers=my_header, json=body)
    assert response.status_code == 201
    response_body = response.json()
    id = response_body["id"]
    # Редактирование проекта
    body = {"title": "Новый проект"}
    response = requests.put(url=f"{base_url}/projects/{id}", headers=my_header, json=body)
    assert response.status_code == 200
    # Получение проекта по id
    response = requests.get(url=f"{base_url}/projects/{id}", headers=my_header)
    assert response.status_code == 200
    response_body = response.json()
    new_title = response_body["title"]
    assert "Новый проект" == new_title


def test_negative_change_project():
    # Создание нового проекта
    my_header = {"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json"}
    body = {"title": "Проект"}
    response = requests.post(url=f"{base_url}/projects", headers=my_header, json=body)
    assert response.status_code == 201
    response_body = response.json()
    id = response_body["id"]
    # Редактирование проекта
    body = {"title": ""}
    response = requests.put(url=f"{base_url}/projects/{id}", headers=my_header, json=body)
    assert response.status_code == 400
    # Получение проекта по id
    response = requests.get(url=f"{base_url}/projects/{id}", headers=my_header)
    assert response.status_code == 200
    response_body = response.json()
    new_title = response_body["title"]
    assert "Проект" == new_title


def test_get_id():
    # Создание нового проекта
    my_header = {"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json"}
    body = {"title": "Проект"}
    response = requests.post(url=f"{base_url}/projects", headers=my_header, json=body)
    assert response.status_code == 201
    response_body = response.json()
    id = response_body["id"]
    # Получение проекта по id
    response = requests.get(url=f"{base_url}/projects/{id}", headers=my_header)
    assert response.status_code == 200
    response_body = response.json()


def test_negative_get_id():
    # Создание нового проекта
    my_header = {"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json"}
    body = {"title": "Проект2"}
    response = requests.post(url=f"{base_url}/projects", headers=my_header, json=body)
    assert response.status_code == 201
    # id = response_body["id"]
    # Получение проекта по id
    response = requests.get(url=f"{base_url}/projects/{id}", headers=my_header)
    assert response.status_code == 404
