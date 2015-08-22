#!/usr/bin/python

def body_dump(b):
    for s in b:
        print s

def redo_line_break(s):
    return s

def should_be_joined_to_next(s):
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



def end_paragraph_by(ps,tok):
    ''' Break paragraphs by ending rule.'''
    po=[]
    for ii,p in enumerate(ps):
        ss=p.split(tok)
        for jj in range(len(ss)-1):
            po.append(ss[jj]+tok)
        if len(ss[-1].strip())>0:
            po.append(ss[-1])
    return po

def start_paragraph_by(ps,tok):
    ''' Break paragraphs by starting rule.'''
    po=[]
    for ii,p in enumerate(ps):
        ss=p.split(tok)
        if len(ss[0].strip())>0:
            po.append(ss[0])
        for jj in range(1,len(ss)):
            po.append(tok+ss[jj])
    return po


def break_joined_paragraphs(b):
    bo = end_paragraph_by(b,'" ')
    bo = start_paragraph_by(bo,' "')
    return bo



if __name__=='__main__':
    h, b, f = data2head_body_foot(data)
    print 'h:'
    body_dump(h)

    b1=join_broken_paragraphs(b)

    b2=break_joined_paragraphs(b1)
    body_dump(b2)


