"""
author:Yuegb
date:2021,01,15
"""
import logging

"""
四个器：记录器、处理器、格式化器、过滤器
"""
# 记录器
logger = logging.getLogger('cn.cccb.logGER')
logger.setLevel(logging.DEBUG)
print(logger)
print(type(logger))

# 处理器
strHandler = logging.StreamHandler()
strHandler.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler(filename='logEE.log')
fileHandler.setLevel(logging.INFO)
# 格式化器
formatter = logging.Formatter("%(asctime)s | %(levelname)8s | %(filename)s:%(lineno)s | %(message)s")

# 过滤器
filtor = logging.Filter("cn.cccb.f")

# 为处理器添加格式
strHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# 为记录器添加处理器,添加过滤器

logger.addHandler(strHandler)
logger.addHandler(fileHandler)
#fileHandler.addFilter(filtor)  # 因为fileHandler不符合过滤条件被过滤，因此只有strHandler有输出
# 打印日志
logger.debug('This is debug log')
logger.info('This is info log')
logger.warning('This is warning log')
logger.error('This is error log')
logger.critical('This is critical log')

a = 'a'
try:
    int(a)
except Exception as e:
    logger.exception(e)