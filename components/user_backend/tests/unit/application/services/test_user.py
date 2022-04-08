from datetime import datetime

import pytest
from attr import asdict
from user.application.services import Users
from pydantic import ValidationError
from user.application.errors import WrongUserPassword


@pytest.fixture(scope='function')
def service_user(user_repo):
    return Users(user_repo=user_repo)


data_user = {
    'user_name': 'user_name_1',
    'id': 1,
    'login': 'test',
    'password': 'test'
}


def test_add_user(service_user):
    service_user.add_user(**data_user)
    service_user.user_repo.add_instance.assert_called_once()


def test_get_user(service_user):
    user = service_user.get_info(id=1)
    assert asdict(user) == data_user


def test_get_by_login(service_user):
    user = service_user.login_user('test', 'test')
    assert asdict(user) == data_user


def test_get_by_login_wrong_password(service_user):
    with pytest.raises(WrongUserPassword):
        service_user.login_user('test', 'test111')


def test_get_by_login_valid_err(service_user):
    with pytest.raises(ValidationError):
        service_user.login_user('test111')


def test_get_user_missing_id(service_user):
    with pytest.raises(ValidationError):
        service_user.get_info()


def test_get_all(service_user):
    user = service_user.get_all()
    assert asdict(user) == data_user


def test_delete_user(service_user):
    service_user.delete_user(id=1)
    service_user.user_repo.delete_instance.assert_called_once()
