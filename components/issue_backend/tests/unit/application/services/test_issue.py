import pytest
from attr import asdict
from issue.application.services import Issues
from issue.application.errors import WrongObjType
from pydantic import ValidationError


@pytest.fixture(scope='function')
def service_issue(issue_repo):
    return Issues(issue_repo=issue_repo)


data_action = {
    'action': 'take',
    'obj_type': 'user_book',
    'id_book': 1,
    'id_user': 1,
    'id': 3
}

data_action_user = {
    'action': 'create',
    'obj_type': 'user',
    'id_user': 1,
    'id_book': None,
    'id': 1
}

data_action_book = {
    'action': 'create',
    'obj_type': 'book',
    'id_book': 1,
    'id_user': None,
    'id': 2
}


def test_message_distributor(service_issue, issue_repo):
    service_issue.message_distributor(obj_type='user', action='create', data=data_action_user)
    service_issue.issue_repo.add_action_user.assert_called_once()


def test_message_distributor_wrong_obj_type(service_issue):
    with pytest.raises(WrongObjType):
        service_issue.message_distributor(obj_type='issue', action='create', data=data_action_user)


def test_message_distributor_valid_error(service_issue):
    with pytest.raises(ValidationError):
        service_issue.message_distributor(action='create', data=data_action_user)


def test_get_all(service_issue):
    action = service_issue.get_all()
    assert asdict(action) == data_action


def test_get_user(service_issue):
    user = service_issue.get_user_action()
    assert asdict(user) == data_action_user


def test_get_book(service_issue):
    book = service_issue.get_book_action()
    assert asdict(book) == data_action_book
