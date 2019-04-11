# -*- coding: utf-8 -*-
import logging

def getLog(name):
    '''
    公共日志类
    '''
    # 创建一个logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler('{}.log'.format(name))
    fh.setLevel(logging.DEBUG)
    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    # 给logger添加handler
    logger.addHandler(fh)
    return logger