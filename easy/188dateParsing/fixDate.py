def fixDate(inp):
    if '/' in inp:
        (m,d,y)=inp.split('/')
    elif '#' in inp:
        (m,y,d)=inp.split('#')
    elif '*' in inp:
        (d,m,y)=inp.split('*')
#    elif ',' in inp and len(inp) == 10:
#        (m,y,d)=inp.split(' ')
    elif ',' in inp:
        (m,y,d)=inp.split(' ')
        d = d[:-1]
    else:
        (y,m,d)=inp.split('-')

    if len(y) == 2:
        if int(y) >= 50:
            y = '19' + y
        else:
            y = '20' + y
    
    return '-'.join([y,m,d])
