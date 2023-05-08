import json

from factory import DictFactory
from factory.fuzzy import FuzzyInteger, FuzzyText, FuzzyFloat

from IO_LOTTERYPB.app import app

class UserPayloadFactory(DictFactory):
    name = FuzzyText()
    last_name = FuzzyText()
    email = FuzzyText()
    age = FuzzyInteger(low=0)
    essays_count: object = FuzzyInteger(low=0)
    rating = FuzzyFloat(low=0)


def test_can_add_user_on_post() -> None:
    payload = UserPayloadFactory()
    with app.test_client() as c:
        result = c.post("/users", json=payload)
        assert result.status_code == 200


def test_prints_added_user_on_post(capsys) -> None:
    payload = UserPayloadFactory()
    with app.test_client() as c:
        c.post("/users", json=payload)
    actual = capsys.readouterr().out
    sorted_dict = {k: payload[k] for k in sorted(payload)}
    expected = f"{sorted_dict}\n"
    assert actual == expected

def test_returns_unimplemented() -> None:
    with app.test_client() as c:
        actual = c.get("/users/24")
    assert actual.status_code == 501
