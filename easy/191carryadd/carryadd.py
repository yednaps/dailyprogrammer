def carryPrint(inp):
    inpint = map(int,inp.split('+'))
    res = ''
    car = ' '

    for i in range(len(max(inp.split('+')))+1):
        lu = [j%10 for j in inpint]
        car = str(sum(lu)/10) + car
        res = str(sum(lu)%10) + res
        inpint = [j/10 for j in inpint]+[sum(lu)/10]

    w = len(res) + 2
    out = [car[1:],'-'*w] + inp.split('+')[:-1] + \
          ['+  '+inp.split('+')[-1],'-'*w,res]
    for i in out:
        print('{:>{width}}'.format(i,width=w))

def carryPrintReal(inp):
    inpreal = inp.split('+')
    inprealsp = [i.split('.') for i in inpreal]
    maxdec = len(max([i[1] for i in inprealsp]))
    inpreal = [str(i)+'.'+str(j)+'0'*(maxdec-len(j)) for i,j in inprealsp]
    inpint = [int(str(i)+str(j)+'0'*(maxdec-len(j))) for i,j in inprealsp]
    res = ''
    car = ' '

    for i in range(len(max(inp.split('+')))+1):
        lu = [j%10 for j in inpint]
        car = str(sum(lu)/10) + car
        res = str(sum(lu)%10) + res
        inpint = [j/10 for j in inpint]+[sum(lu)/10]

    res[:(-1*maxdec)]+'.'+res[(-1*maxdec):]
    car[:(-1*maxdec)]+'.'+res[(-1*maxdec):]
    w = len(res) + 2
    out = [car[1:],'-'*w] + inpreal[:-1] + \
          ['+  '+inpreal[-1],'-'*w,res]
    for i in out:
        print('{:>{width}}'.format(i,width=w))
