from pytest import mark

@mark.sports_car
@mark.lights
class LightsTests:

    @mark.smoke
    def test_all_lights_switched_on():
        assert True