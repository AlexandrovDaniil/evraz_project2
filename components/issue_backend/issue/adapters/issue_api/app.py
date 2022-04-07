from issue.application import services
from classic.http_api import App
from . import auth, controllers
from classic.http_auth import Authenticator


def create_app(
        is_dev_mode: bool,
        issues: services.Issues,
) -> App:
    app = App(prefix='/api')
    authenticator = Authenticator(app_groups=auth.ALL_GROUPS)
    if is_dev_mode:
        authenticator.set_strategies(auth.jwt_strategy)

    app.register(controllers.Issues(authenticator=authenticator, issues=issues))

    return app
