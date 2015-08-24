#!/usr/bin/python

def body_dump(b):
    for s in b:
        print s

def redo_line_break(s):
    return s

def should_be_joined_to_next(s):
    ''' Returns true if a line should be joined to the next.'''
    ss = s.strip()
    #print ss,'ends with',ss[-3:]

    # if a line is short, must be a subheading
    if len(ss)<20: return False

    if ss.endswith('.'): return False
    if ss.endswith('"'): return False
    if ss.endswith("'"): return False
    #print 'should join'
    return True

def join_broken_paragraphs(b):
    bo = [] # output
    s_buf = '' #sentence buffer
    for ii,s in enumerate(b):
        srs = s.rstrip('\n\r')
        s_buf = s_buf + srs
        must_end_line = not should_be_joined_to_next(s)
        #print '#'+srs,must_end_line

        if must_end_line:
            #print 'end line here'
            bo.append(s_buf+'\r\n')
            s_buf = ''
        else: # accumulate into the buffer
            #print 'join line:',s_buf
            pass
        if ii==len(b)-1:
            if not s_buf == '':
                bo.append(s_buf)
    return bo


def break_paragraph_at(ps, tok, num=0):
    ''' Break paragraphs using a token.'''
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
    h, b, f = data2head_body_foot(data)
    print 'h:'
    body_dump(h)

    b1=join_broken_paragraphs(b)

    b2=break_joined_paragraphs(b1)
    body_dump(b2)


