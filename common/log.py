import logging


# 日志类
class Logging:
    # def log_template(self, log_path):
    #     # 创建日志器
    #     logger = logging.getLogger('logger')
    #     # 设置日志级别DEBUG级别
    #     logger.setLevel(logging.DEBUG)
    #     # 设置日志格式
    #     fmt = '%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s'
    #     fm = logging.Formatter(fmt=fmt)
    #     # 创建文件处理器
    #     fh = logging.FileHandler(log_path, encoding='utf-8')
    #     # 创建日志处理器，输出到控制台
    #     sh = logging.StreamHandler()
    #     # 控制台添加到日志器中
    #     logger.addHandler(sh)
    #     # 将文件处理器添加到日志器中
    #     logger.addHandler(fh)
    #     # 把格式器放到控制台
    #     sh.setFormatter(fm)
    #     fh.setFormatter(fm)
    #     # logger.removeHandler(fh)
    #     # logger.removeHandler(sh)
    #     return logger

    def log(self, msg):
        logger = logging.getLogger("logger")
        handler = logging.FileHandler(filename='../log/api.log',encoding='utf-8')

        logger.setLevel(logging.INFO)  # 设置日志等级
        # 日志输出格式
        fmt = '%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s'
        formatter = logging.Formatter(fmt)
        handler.setFormatter(formatter)
        # 输入到控制台
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)

        logger.addHandler(handler)
        logger.addHandler(console)

        logger.info(msg)
        # 移除处理器
        logger.removeHandler(handler)
        logger.removeHandler(console)
