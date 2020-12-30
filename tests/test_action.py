
def test_validate(basic_action):
    print("{}".format(basic_action.values))
    assert basic_action.validate()
