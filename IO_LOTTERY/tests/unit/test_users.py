from factory import DictFactory
from factory.fuzzy import FuzzyText, FuzzyInteger, FuzzyFloat

from IO_LOTTERY.app import add_user, get_user, app


class UserPayloadFactory(DictFactory):
    name = FuzzyText()
    last_name = FuzzyText()
    email = FuzzyText()
    age = FuzzyInteger(low=0)
    essays_count = FuzzyInteger(low=0)
    rating = FuzzyFloat(low=0)


def test_returns_sent_user() -> None:
    payload = UserPayloadFactory()
    with app.test_request_context(path="/users", method='POST', json=payload):
        response = add_user()
    assert response.json == payload


def test_returns_unimplemented() -> None:
    response = get_user()
    assert response.status_code == 501
