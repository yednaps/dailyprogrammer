def fixDate(inp):
    m = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'
    mth = {j:str(i) for i,j in enumerate(' '.split(m))}

    if '/' in inp:
        (m,d,y)=inp.split('/')
    elif '#' in inp:
        (m,y,d)=inp.split('#')
    elif '*' in inp:
        (d,m,y)=inp.split('*')
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
