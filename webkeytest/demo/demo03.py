import unittest
from unittest import TestCase, mock
from webkeytest.demo import demo04


class TestLinuxTool(TestCase):

    @mock.patch("demo.demo04.login")
    def test_check_cmd_response(self, mock_login):
        mock_login.return_value = "登陆成功"
        content = demo04.login()
        print(content)



if __name__ == '__main__':
    unittest.main()
