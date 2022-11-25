from flask import Flask

from myapp.todo.src.infrastructure.rest.controllers import todos_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(todos_blueprint, url_prefix='/todos')

    return app


if __name__ == '__main__':
    create_app().run()
