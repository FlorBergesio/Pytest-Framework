from pytest import mark

@mark.sports_car
@mark.doors
class DoorTests:

    @mark.smoke
    def test_all_doors_locked(self):
        assert True