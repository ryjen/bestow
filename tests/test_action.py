from os import path


def test_action_validate(basic_action):
    assert basic_action.validate()


def test_action_file(basic_action):
    assert basic_action.file() == "test.json.tmpl"


def test_action_location(basic_action):
    assert basic_action.location() == "test.json"


def test_action_type(basic_action):
    assert basic_action.type() == "copy"


def test_action_copy(basic_action, basic_package):
    basic_action.copy()
    assert path.isfile(path.join(basic_package, "test.json"))

def test_action_link(basic_action, basic_package):
    basic_action.link()
    assert path.isfile(path.join(basic_package, "test.json"))
