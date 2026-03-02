import os
from dotenv import load_dotenv
import pytest
from ProjectYouGile import ProjectYouGile


load_dotenv()


@pytest.fixture
def api():
    url = "https://ru.yougile.com/api-v2"
    return ProjectYouGile(url)


@pytest.fixture
def project_van(api):
    title = 'Project YouGile'
    user_id = os.getenv('USER_ID')
    status, project = api.create_new_project(title, user_id)
    assert status == 201, " Не создается проект"
    yield project


def test_create_new_project(api):
    title = 'Project YouGile'
    user_id = os.getenv('USER_ID')
    status, project = api.create_new_project(title, user_id)
    assert status == 201
    assert project["id"] is not None


def test_create_new_project_negative(api):
    title = 'Project YouGile'
    status, project = api.create_new_project(title, "111")
    assert status == 400
    assert (
            "Сотрудники со следующими ID не найдены в компании: 111"
            in project["message"]
    )


def test_change_new_project(api, project_van):
    new_title = 'Project YouGile2'
    user_id = os.getenv('USER_ID')
    status, new_project = api.change_new_project(
        project_van["id"], new_title, user_id
    )
    assert status == 200
    assert new_project is not None


def test_change_new_project_negative(api):
    new_title = 'Project YouGile2'
    user_id = os.getenv('USER_ID')
    status, new_project = api.change_new_project(
        222, new_title, user_id
    )
    assert status == 404
    assert "Проект не найден" in new_project["message"]


def test_get_new_project(api, project_van):
    status, project_data = api.get_new_project(project_van["id"])
    assert status == 200
    assert project_data['id'] == project_van['id']


def test_get_new_project_negative(api, project_van):
    status, project_id = api.get_new_project(api)
    assert status == 404
    assert "Проект не найден" in project_id["message"]
