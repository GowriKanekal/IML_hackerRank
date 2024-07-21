# Enter your code here. Read input from STDIN. Print output to STDOUT

def calc(wx,bx,wy,by):
    # a white ball is drawn from bag x
    p1 = wx/(wx+bx)
    p11 = by / (wy+by+1)

    # black ball is drawn from bag x
    p2 = bx/(wx+bx)
    p22 = (by+1) / (wy+by+1)

    # total probability
    pf = p11*p1 + p22*p2

    print(pf)

calc(5,4,7,6)
