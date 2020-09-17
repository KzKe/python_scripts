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

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='test.log'
                    )

i = 101111
logging.warning('warning!!! {0}'.format(i))
logging.info('this is info!')
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')


