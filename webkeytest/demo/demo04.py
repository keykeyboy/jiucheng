# import re
#
#
# def send_shell_cmd():
#     return "Response from send_shell_cmd function"
#
#
# def check_cmd_response():
#     response = send_shell_cmd()
#     print("response: {}".format(response))
#     return re.search(r"mock_send_shell_cmd", response)

from common.mock_server import MockServer
from unittest import mock


def login():
    pass


return_value = '12312312'
login = MockServer(return_value)
text = login()
print(text)
