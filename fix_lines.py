#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
from paragraph import *
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__=='__main__':
    if len(sys.argv)<2:
        print 'Usage: fix_lines.py file.txt'
        sys.exit(0)
    
    with open(sys.argv[1]) as f:
        content = f.readlines()
        b = []
        for c in content:
            try:
                b+=[c.decode('cp949')] #biohackers.net/wiki/PythonAndHangul
            except UnicodeDecodeError as e:
                print e

        #b = b[0:15]
        b1 = join_broken_paragraphs(b)
        b2 = break_joined_paragraphs(b1)
        body_dump(b2)

