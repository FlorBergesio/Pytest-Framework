from pytest import mark

@mark.smoke
@mark.sports_car
@mark.lights
def test_all_lights_switched_on():
    assert True