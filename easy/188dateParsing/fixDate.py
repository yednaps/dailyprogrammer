def fixDate(inp):
    mth = {'Apr': '3',
 'Aug': '7',
 'Dec': '11',
 'Feb': '1',
 'Jan': '0',
 'Jul': '6',
 'Jun': '5',
 'Mar': '2',
 'May': '4',
 'Nov': '10',
 'Oct': '9',
 'Sep': '8'}
    if '/' in inp:
        (m,d,y)=inp.split('/')
    elif '#' in inp:
        (m,y,d)=inp.split('#')
    elif '*' in inp:
        (d,m,y)=inp.split('*')
#    elif ',' in inp and len(inp) == 10:
#        (m,y,d)=inp.split(' ')
    elif ',' in inp:
        (m,d,y)=inp.split(' ')
        m = mth[m]
        d = d[:-1]
        if len(m) == 1:
            m = '0' + m
    else:
        (y,m,d)=inp.split('-')

    if len(y) == 2:
        if int(y) >= 50:
            y = '19' + y
        else:
            y = '20' + y
    
    return '-'.join([y,m,d])
