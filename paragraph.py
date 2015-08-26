#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

def body_dump(b):
    for s in b:
        print s

def redo_line_break(s):
    return s

def should_continue(s):
    ''' Returns true if a line should be joined to the next.

    >>> should_continue(u'안녕하세요? 저는 줄 정리가 안된 한글문서를 정리해줍니다.')
    False
    >>> should_continue(u'안녕하세요? 저는 줄 정리가 안된 한글문서를?')
    False
    >>> should_continue(u'안녕하세요? 저는 줄 정리가 안된 한글문서를,')
    True
    '''
    ss = s.strip()

    # if a line is short, must be a subheading
    if len(ss)<25: return False

    if ss.endswith('.'): return False
    if ss.endswith('?'): return False
    if ss.endswith('"'): return False
    if ss.endswith("'"): return False
    return True

def should_begin(s):
    ''' Returns true if a line starts from here.

    >>> should_begin(u'   여행의 시작')
    True
    >>> should_begin(u'3. 여행의 시작')
    True
    >>> should_begin(u'- 여행의 시작')
    True
    >>> should_begin(u'여행의 시작')
    False
    '''
    if s.startswith('   '): return True
    if s.startswith('- '): return True
    if re.match('^\d+\.',s.strip()): return True
    return False

def join_broken_paragraphs(b):
    bo = [] # output
    s_buf = '' #sentence buffer
    for ii,s in enumerate(b[:-1]):
        srs = s.rstrip('\n\r')
        s_buf = s_buf + srs
        must_end_line = not should_continue(s) or should_begin(b[ii+1])
        #print '#'+srs,must_end_line

        if must_end_line:
            #print 'end line here'
            bo.append(s_buf+'\r\n')
            s_buf = ''
        else: # accumulate into the buffer
            #print 'join line:',s_buf
            pass
    if not s_buf == '':
        bo.append(s_buf)
    return bo


def break_paragraph_at(ps, tok, num=0):
    ''' Break paragraphs using a token.

    >>> break_paragraph_at(['"How are you?" Asked John.'], '?" ',2)
    ['"How are you?"', ' Asked John.']
    >>> break_paragraph_at(['John asked. "How are you?"'], '. "',1)
    ['John asked.', ' "How are you?"']
    '''
    po=[]
    tok1 = tok[:num]
    tok2 = tok[num:]
    for ii,p in enumerate(ps):
        ss=p.split(tok)
        po.append(ss[0])
        for jj in range(1,len(ss)):
            po[-1]=po[-1]+tok1
            po.append(tok2+ss[jj])
    return po

def break_joined_paragraphs(b):
    b = break_paragraph_at(b,'?"',2)
    b = break_paragraph_at(b,'!"',2)
    b = break_paragraph_at(b,'."',2)
    b = break_paragraph_at(b,'. "',1)
    return b



if __name__=='__main__':
    import doctest
    doctest.testmod()
#   h, b, f = data2head_body_foot(data)
#   print 'h:'
#   body_dump(h)

#   b1=join_broken_paragraphs(b)

#   b2=break_joined_paragraphs(b1)
#   body_dump(b2)


