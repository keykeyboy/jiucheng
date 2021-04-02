'''
@Project ：auto_test 
@File ：test_demo03.py
@Date ：2021/4/2 11:05 
'''
import pytest


def setup_function():
    print('setup_function')


def teardown_function():
    print('teardown_function')

def setup_module():
    print('setup_module')

def teardown_module():
    print('teardown_module')


def test_demo02():
    print('test_02')


def test_demo03():
    print('test_03')


class TestDmo03:
    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def setup_class(self):
        print('setupclass')

    def teardown_class(self):
        print('teardownclass')

    def setup_method(self):
        print('setupmethod')

    def teardown_method(self):
        print('teardownmethod')

    def test_demo01(self):
        print('test_01')


if __name__ == '__main__':
    pytest.main(['-s', 'test_demo03.py', '-q'])
