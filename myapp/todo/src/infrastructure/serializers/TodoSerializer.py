from dataclasses import asdict


class TodoSerializer:
    def __init__(self, todos):
        self._todos = todos

    @property
    def data(self):
        result = []
        for todo in self._todos:
            result.append(
                {
                    'name': todo.name.name,
                    'description': todo.description,
                    'project': todo.project
                }
            )
        return result
