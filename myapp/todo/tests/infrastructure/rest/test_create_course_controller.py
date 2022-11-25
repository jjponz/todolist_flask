from unittest.mock import patch

import pytest

from app import create_app
from myapp.todo.src.infrastructure.repos.todo_repository import FakeTodoRepository


class TestTodoCreator:
    @pytest.fixture
    def todo_repo(self):
        with patch.object(FakeTodoRepository, 'save') as mock:
            yield mock

    @pytest.fixture()
    def app(self):
        app = create_app()
        app.config.update({
            "TESTING": True,
        })

        yield app

    @pytest.fixture()
    def client(self, app):
        return app.test_client()

    def test_returns_200_when_save_todo(self, client, todo_repo):
        response = client.post("/todos/", json={
            'name': 'name',
            'description': 'description',
            'project': 'project'
        })

        assert response.status_code == 200
        todo_repo.assert_called()

    def test_returns_400_when_todo_has_no_name(self, client, todo_repo):
        response = client.post("/todos/", json={
            'name': '',
            'description': 'description',
            'project': 'project'
        })

        assert response.status_code == 400
        todo_repo.assert_not_called()
