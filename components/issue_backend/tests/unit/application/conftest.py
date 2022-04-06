from unittest.mock import Mock

import pytest
from issue_backend.issue.application import dataclasses, interfaces


@pytest.fixture(scope='function')
def action_user():
    return dataclasses.Action(
        action='create',
        obj_type='user',
        id_user=1,
        id=1
    )


@pytest.fixture(scope='function')
def action_book():
    return dataclasses.Action(
        action='create',
        obj_type='book',
        id_book=1,
        id=2
    )


@pytest.fixture(scope='function')
def action():
    return dataclasses.Action(
        action='take',
        obj_type='user_book',
        id_book=1,
        id_user=1,
        id=3
    )


@pytest.fixture(scope='function')
def issue_repo(action_user, action_book, action):
    issue_repo = Mock(interfaces.IssuesRepo)
    issue_repo.add_action = Mock(return_value=action)
    issue_repo.add_action_user = Mock(return_value=action_user)
    issue_repo.get_all = Mock(return_value=action)
    issue_repo.get_user_action = Mock(return_value=action_user)
    issue_repo.get_book_action = Mock(return_value=action_book)
    return issue_repo
