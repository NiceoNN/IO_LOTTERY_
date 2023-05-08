from factory import Factory
from factory.fuzzy import FuzzyText, FuzzyInteger, FuzzyFloat
import pytest
from pytest import fixture

from IO_LOTTERY.domain import User


class UserFactory(Factory):
    class Meta:
        model = User

    first_name = FuzzyText()
    last_name = FuzzyText()
    email = FuzzyText()
    age = FuzzyInteger(low=0)
    essays_count = FuzzyInteger(low=0)
    rating = FuzzyFloat(low=0)


@pytest.fixture
def user() -> User:
    return UserFactory()


def test_can_instantiate_user(user: User) -> None:
    assert isinstance(user, User)


def test_user_has_first_name_as_attribute(user: User) -> None:
    assert hasattr(user, 'first_name')
    assert isinstance(user.first_name, str)
    assert user.first_name
