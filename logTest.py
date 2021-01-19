"""
author:Yuegb
date:2021,01,15
"""
import logging
"""
print('print log')
# 默认的日志输出级别为warning
logging.basicConfig(filename='logTest.log', filemode='w', level=logging.DEBUG)  # 设置日志输出级别
logging.debug('This is debug log')
logging.info('This is info log')
logging.warning('This is warning log')
logging.error('This is error log')
logging.critical('This is critical log')

"""

"""
logging.basicConfig(level=logging.DEBUG)
logging.debug('姓名: %s','ketty')
logging.debug('姓名: {}'.format('ketty'))
"""
logging.basicConfig(format="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)
logging.debug('姓名: %s','ketty')