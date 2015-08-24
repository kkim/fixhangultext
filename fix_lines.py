#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
import logging

from paragraph import *
reload(sys)
sys.setdefaultencoding('utf-8')

import argparse



def to_unicode(lines):
    b = []
    for c in lines:
        try:
            b+=[c.decode('cp949')] #biohackers.net/wiki/PythonAndHangul
        except UnicodeDecodeError as e:
            print e
    return b

def fix_lines(lines):
    lines = join_broken_paragraphs(lines)
    lines = break_joined_paragraphs(lines)
    return lines


if __name__=='__main__':

    parser = argparse.ArgumentParser(description='dump unicode of a file')
    parser.add_argument('--nofix',help='dump unicode without line fixing',
                        action='store_true')
    parser.add_argument("filename",help="input text file name")
    parser.parse_args()

    logging.basicConfig(filename='fix_hangul_doc.log',level=logging.INFO)
    logging.info(' '.join(sys.argv))

    args = parser.parse_args()

    with open(args.filename) as f:
        lines = f.readlines()
        lines = to_unicode(lines)
        if not args.nofix:
            lines = fix_lines(lines)
        body_dump(lines)

