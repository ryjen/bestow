import pytest

from bestow.meta import Meta
from bestow.action import Action
from bestow.util import load_yaml


@pytest.fixture
def basic_package() -> str:
    return "tests/data/basic"

@pytest.ficture
def action_package() -> str:
    return "tests/data/action"


@pytest.fixture
def basic_config(basic_package) -> Meta:
    meta = Meta(basic_package)
    meta.process()
    return meta


@pytest.fixture
def copy_action(action_package) -> Action:
    data = load_yaml("{}/copy.yml".format(action_package))
    action = Action(basic_package, data)
    return action


@pytest.fixture
def link_action(action_package) -> Action:
    data = load_yaml("{}/link.yml".format(action_package))
    action = Action(basic_package, data)
    return action
