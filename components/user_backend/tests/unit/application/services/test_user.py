from datetime import datetime

import pytest
from attr import asdict
from components.user_backend.user.application.services import Users
from pydantic import ValidationError


@pytest.fixture(scope='function')
def service_user(user_repo):
    return Users(user_repo=user_repo)


data_user = {
    'user_name': 'user_name_1',
    'id': 1
}


def test_add_user(service_user):
    service_user.add_user(**data_user)
    service_user.user_repo.add_instance.assert_called_once()


def test_get_user(service_user):
    user = service_user.get_info(id=1)
    assert asdict(user) == data_user


def test_get_user_missing_id(service_user):
    with pytest.raises(ValidationError):
        service_user.get_info()


def test_get_all(service_user):
    user = service_user.get_all()
    assert asdict(user) == data_user


def test_delete_user(service_user):
    service_user.delete_user(id=1)
    service_user.user_repo.delete_instance.assert_called_once()
