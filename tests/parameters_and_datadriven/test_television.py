from pytest import mark

@mark.parametrize('tv_brand', [
    ('Samsung'),
    ('Sony'),
    ('LG')
])
def test_television_turns_on_with_parameters(tv_brand):
    print(f"{tv_brand} turns on as expected")

@mark.skip(reason="Won't work until webdrivers are properly setup")
def test_browser_can_navigate_to_training_ground(browser):
    browser.get('http://techstepacademy.com/training-ground')

def test_television_turns_on_from_json(test_data):
    print(f"{test_data} turns on as expected")