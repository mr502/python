class TestApi:
    def test_get_user_info(self, api):
        user_info = api.get_user_info()
        assert user_info['username'] == 'test'
        assert user_info['email'] == ''
        assert user_info['first_name'] == ''
