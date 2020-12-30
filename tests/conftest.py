import pytest
import yaml

from bestow.meta import Meta
from bestow.action import Action
from bestow.util import load_yaml


@pytest.fixture
def basic_package() -> str:
    return "tests/data/basic"


@pytest.fixture
def basic_config(basic_package) -> Meta:
    meta = Meta(basic_package)
    meta.process()
    return meta


@pytest.fixture
def basic_action(basic_package) -> Action:
    data = load_yaml("{}/action.yml".format(basic_package))
    action = Action(basic_package, data)
    return action
