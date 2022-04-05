from issue.application import services
from classic.http_api import App
from . import auth, controllers


def create_app(
        is_dev_mode: bool,
        issues: services.Issues,
) -> App:
    app = App(prefix='/api')

    app.register(controllers.Issues(issues=issues))

    return app
