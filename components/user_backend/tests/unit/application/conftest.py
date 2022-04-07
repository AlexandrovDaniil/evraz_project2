from datetime import datetime
from unittest.mock import Mock

import pytest
# from user_backend.user.application import dataclasses, interfaces
from user.application import dataclasses, interfaces


@pytest.fixture(scope='function')
def user():
    return dataclasses.User(
        user_name='user_name_1',
        id=1,
    )


@pytest.fixture(scope='function')
def user_repo(user):
    user_repo = Mock(interfaces.UsersRepo)
    user_repo.get_by_id = Mock(return_value=user)
    user_repo.add_instance = Mock(return_value=user)
    user_repo.get_all = Mock(return_value=user)
    return user_repo
