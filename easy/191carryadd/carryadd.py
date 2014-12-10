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
