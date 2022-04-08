from pytest import mark

@mark.smoke
@mark.sports_car
@mark.engine
def test_engine_start():
    assert True