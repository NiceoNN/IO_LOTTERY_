from unittest.mock import Mock

import pytest
from pytest import fixture

from IO_LOTTERY.controllers import AddUserController, AddUserRequest, GetUserController
from IO_LOTTERY.repositories import UserRepository
from tests.integration.test_users import UserPayloadFactory

# Fixtures
@pytest.fixture
def user_repository() -> Mock:
    return Mock(UserRepository)

@pytest.fixture
def add_user_controller(user_repository: Mock) -> AddUserController:
    return AddUserController(repository=user_repository)

# Tests
def test_can_instantiate_add_user_controller(capsys, add_user_controller: AddUserController) -> None:
    payload = UserPayloadFactory()
    request = AddUserRequest(json=payload)
    add_user_controller.add(request=request)
    actual = capsys.readouterr().out
    expected = f"{payload}\n"
    assert actual == expected

def test_calls_repository_on_add_method(add_user_controller: AddUserController, user_repository: Mock) -> None:
    payload = UserPayloadFactory()
    request = AddUserRequest(json=payload)
    add_user_controller.add(request)
    assert user_repository.add.call_count == 1

def test_add_user_request_has_json_field() -> None:
    payload = UserPayloadFactory()
    request = AddUserRequest(json=payload)
    assert request.json

def test_get_user_controller_raises_on_get() -> None:
    controller = GetUserController()
    with pytest.raises(NotImplementedError):
        controller.get(id=21)

# TestCase
class TestUserController(unittest.TestCase):
    def setUp(self):
        self.user_controller = UserController(UserRepository(UserDao()))

    def test_create_user(self):
        user = {"id": 1, "name": "Zbigniew Stonoga"}
        response = self.user_controller.create_user(user)
        self.assertEqual(response, user)

    def test_update_user(self):
        user_id = 1
        user = {"name": "Zbigniew Stonoga"}
        response = self.user_controller.update_user(user_id, user)
        self.assertEqual(response["name"], user["name"])

    def test_delete_user(self):
        user_id = 1
        with self.assertRaises(NotImplementedError):
            self.user_controller.delete_user(user_id)
