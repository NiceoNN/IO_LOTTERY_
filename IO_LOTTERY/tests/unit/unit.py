import pytest
from pytest import raises, fixture

from IO_LOTTERY.repositories import UserRepository

@pytest.fixture
def user_repository() -> UserRepository:
    return UserRepository()


def test_can_instantiate_user_repository(user_repository: UserRepository) -> None:
    assert isinstance(user_repository, UserRepository)


def test_raises_on_add_method(user_repository: UserRepository) -> None:
    with raises(NotImplementedError):
        user_repository.add()
