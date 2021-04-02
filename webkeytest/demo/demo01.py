import threading
import time
import os

from webkeytest.test.excel_excutor import ExcelExcutor


class Demo:

    def case_run(self):
        cases = []
        for path, dir, files in os.walk('../case_excels/'):
            for file in files:
                excel_path = path + file
                suffix = os.path.splitext(file)[1]
                if suffix == '.xlsx':
                    cases.append(excel_path)
                    print(excel_path)
                    # 多线程执行测试用例
                    threading.Thread(target=ExcelExcutor().excel_case_excute, args=[excel_path, ]).start()
                else:
                    print('改文件无法识别' + excel_path)
        # print(os.walk('../cases/addcart_case.py'))

    def funct_01(self):
        time.sleep(3)
        print('我是fun_01')

    def funct_02(self, name, value):
        print('funct02 name={},value={}'.format(name, value))

    def fuc_03(self):
        print('funct03')

    def funct_04(self, name, value):
        print('funct04 name={},value={}'.format(name, value))

    def run(self):
        for i in range(0, 1):
            threading.Thread(target=self.funct_01).start()
            threading.Thread(target=self.funct_02, args=(1, 2)).start()
        for i in range(0, 1):
            threading.Thread(target=self.funct_01).start()
            threading.Thread(target=self.funct_02, args=(1, 2)).start()
        for i in range(0, 1):
            threading.Thread(target=self.funct_01).start()
            threading.Thread(target=self.funct_02, args=(1, 2)).start()


if __name__ == '__main__':
    Demo().case_run()
