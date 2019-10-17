import kwargs as kwargs
import pytest
from config import Read_xlsx
import requests

host = 'http://192.168.10.167:8095'
data = Read_xlsx('case.xlsx').info()
class Test_case(object):
    @pytest.fixture(params=data)
    def login_data(self, request):
        return request.param

    def test_login(self, login_data):
        self.data = login_data[2]
        self.url = host + login_data[3]
        if login_data[4] == "post":
            result = requests.post(self.url, data=self.data)
            assert result.status_code == int(login_data[5])
        else:
            result = requests.get(self.url, params=self.data)
            assert result.status_code == int(login_data[5])

if __name__ == "__main__":
    pytest.main()