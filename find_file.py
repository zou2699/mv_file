#!/usr/bin/env python
# encoding: utf-8
# Author: zouhl
# Created Time : 2017年11月17日 星期五 13时34分55秒
# File Name: find_file.py
# Description:


import os
import sys
import shutil
import yaml

config_file = open(os.path.dirname(os.path.abspath(__file__)) + '/config.yaml')
config = yaml.safe_load(config_file)
config_file.close()

# 文件根目录
#root_dir = '/root/mycode/find_file/'
root_dir = config['root_dir']
# 输出目录
#output_dir = '/root/mycode/find_file/py'
output_dir = config['output_dir']
# 文件类型
#file_type = '.c'
file_type = config['file_type']
files = {}
count = 0
print root_dir,"===",output_dir, '----', file_type

for parent, dirnames, filenames in os.walk(root_dir):
    #print '123',parent
    if parent == root_dir or parent == output_dir:
        continue
    for f in filenames:
        if f.endswith(file_type):
            old_path = os.path.join(parent, f)
            output_file = os.path.join(output_dir, f)
            # print old_path
            # print output_file
            files[old_path] = output_file
            # shutil.move(old_path, output_dir)
if files:
    for k, v in files.iteritems():
        print k,v
else:
    print "在根目录%s下没有找到%s" % (root_dir, file_type)
    sys.exit()

a = raw_input('yes/no ?')
if a == 'yes':
    for k, v in files.iteritems():
        shutil.move(k,v)
        count += 1
    print '移动完成,共%s个' % count

