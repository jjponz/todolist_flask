from flask import Blueprint, request

from myapp.todo.src.application.todo_creator import TodoCreator
from myapp.todo.src.application.todo_finder import TodoFinder
from myapp.todo.src.domain.exceptions import TodoWithoutNameException
from myapp.todo.src.infrastructure.repos.todo_repository import FakeTodoRepository
from myapp.todo.src.infrastructure.serializers.TodoSerializer import TodoSerializer

todos_blueprint = Blueprint('todos', __name__,)


@todos_blueprint.route('/<id>')
def todo_finder(id: int):
    todos = TodoFinder(FakeTodoRepository()).execute(id)

    return TodoSerializer(todos).data


@todos_blueprint.route('/', methods=['POST'])
def create_todo():
    data = request.json
    try:
        TodoCreator(FakeTodoRepository()).execute(
            data.get('name'),
            data.get('description'),
            data.get('project')
        )
    except TodoWithoutNameException:
        return "Todo without name", 400

    return "created"







