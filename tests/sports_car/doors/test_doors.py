from pytest import mark

@mark.smoke
@mark.sports_car
@mark.doors
def test_all_doors_locked():
    assert True