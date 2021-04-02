'''
@Project ：auto_test 
@File ：read_ini.py
@Date ：2021/3/29 15:43 
'''
import configparser


def ReadIni(config_file, section, option):
    config = configparser.ConfigParser()
    config.read(config_file)
    value = config.get(section, option)
    return value


if __name__ == '__main__':
    res = ReadIni('config.ini', 'TEST_SERVER', 'URL')
    print(res)