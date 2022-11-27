import pytest

from ..string_example import shout


@pytest.mark.parametrize(
    "words",
    [
        "a",
        "Bob",
        "Never odd or even",
        "Do geese see God?",
    ],
)
def test_shouting(words):
    assert shout(words)


@pytest.mark.parametrize(
    "words",
    [
        "",
        None,
    ],
)
def test_shouting_nothing(words):
    assert shout(words) is None


@pytest.mark.xfail
@pytest.mark.parametrize(
    "words",
    [
        "",
        None,
    ],
)
def test_shout_nothing_alternative(words):
    assert shout(words)
