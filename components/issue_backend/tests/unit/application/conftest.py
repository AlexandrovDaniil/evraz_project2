from unittest.mock import Mock

import pytest
from issue.application import dataclasses, interfaces


@pytest.fixture(scope='function')
def action_user():
    return dataclasses.Action(
        action='create',
        obj_type='user',
        id_user=1,
        id=1,
        date=None,
        book_title=None
    )


@pytest.fixture(scope='function')
def action_book():
    return dataclasses.Action(
        action='create',
        obj_type='book',
        id_book=1,
        id=2,
        date=None,
        book_title=None
    )


@pytest.fixture(scope='function')
def action():
    return dataclasses.Action(
        action='take',
        obj_type='user_book',
        id_book=1,
        id_user=1,
        id=3,
        book_title='test'

    )


@pytest.fixture(scope='function')
def issue_repo(action_user, action_book, action):
    issue_repo = Mock(interfaces.IssuesRepo)
    issue_repo.add_action = Mock(return_value=action)
    issue_repo.add_action_user = Mock(return_value=action_user)
    issue_repo.get_all = Mock(return_value=action)
    issue_repo.get_all_by_user = Mock(return_value=action_user)
    issue_repo.get_user_action = Mock(return_value=action_user)
    issue_repo.get_book_action = Mock(return_value=action_book)
    return issue_repo
