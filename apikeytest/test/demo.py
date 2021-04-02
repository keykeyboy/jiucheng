'''
@Project ：auto_test 
@File ：demo.py
@Date ：2021/3/26 15:14 
'''

import requests
import json

data = {
    'username': 'admin',
    'password': '123456',
    'test':'test'
}
try:
    response = requests.post(url='http://39.98.138.157:5000/api/login', json=data, timeout=1)
    result = response.text
    # assert response.status_code == 200
    result_json = json.loads(result)
    print(type(result_json))
    print(result_json)
    # print(result_json['msg'])
    # assert result_json['msg'] == 'success'
    print(response.raise_for_status())
except Exception as e:
    print('URL输入不正确')

