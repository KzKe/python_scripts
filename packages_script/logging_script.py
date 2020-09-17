#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :logging_script.py
# @Time      :2020/9/15 9:19 下午
# @Author    :Kangke

'''
Ref: https://www.jianshu.com/p/feb86c06c4f4
默认情况下，logging模块将日志打印到屏幕上(stdout)，
日志级别为WARNING(即只有日志级别高于WARNING的日志信息才会输出)

'''

# import logging
# # from logging import handlers
#
# logger = logging.getLogger(__name__)
# logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
#                     datefmt='%m/%d/%Y %H:%M:%S',
#                     level=logging.INFO,
#                     filename='test.log'
#                     )
#
# i = 101111
# logging.warning('warning!!! {0}'.format(i))
# logging.info('this is info!')
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')

'''
建立
'''

import logging
from logging import handlers
import os


def create_logger(log_path):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # 日志级别关系映射

    logger = logging.getLogger(log_path)
    fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    format_str = logging.Formatter(fmt)  # 设置日志格式
    logger.setLevel(level_relations.get('info'))  # 设置日志级别
    sh = logging.StreamHandler()  # 往屏幕上输出
    sh.setFormatter(format_str)  # 设置屏幕上显示的格式
    th = handlers.TimedRotatingFileHandler(
        filename=log_path, when='D', backupCount=3,
        encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
    th.setFormatter(format_str)  # 设置文件里写入的格式
    logger.addHandler(sh)  # 把对象加到logger里
    logger.addHandler(th)

    return logger


if __name__ == '__main__':
    os.mkdir('./logs/')
    logger = create_logger('./logs/Fasttext.log')
    i = 101111
    logging.warning('warning!!! {0}'.format(i))
    logging.info('this is info!')
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')
