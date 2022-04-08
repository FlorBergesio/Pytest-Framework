from pytest import mark

@mark.sports_car
@mark.engine
class EngineTests:

    @mark.smoke
    def test_engine_start(self):
        assert True

    @mark.smoke
    def test_engine_off(self):
        assert True

    def test_engine_self_destruct(self):
        assert True