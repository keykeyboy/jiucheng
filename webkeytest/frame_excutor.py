import os
import threading

from webkeytest.test.excel_excutor import ExcelExcutor


class App:
    def run(self):
        # cases = []
        for path, dir, files in os.walk('case_excels/'):
            for file in files:
                excel_path = path + file
                suffix = os.path.splitext(file)[1]
                if suffix == '.xlsx':
                    # cases.append(excel_path)
                    # print(excel_path)
                    # 多线程执行测试用例
                    threading.Thread(target=ExcelExcutor().excel_case_excute, args=[excel_path, ]).start()
                else:
                    print('改文件无法识别' + excel_path)


if __name__ == '__main__':
    app = App()
    app.run()
