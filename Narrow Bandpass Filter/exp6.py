
pi = 3.1415926

def solve(r3, c):
    rhs = 4*pi*pi*1000000*r3*c*c
    par = 1/rhs
    q = pi*1000*r3*c
    # a = 2*r3/r1
    return q, par, r3
# q, par=solve(3e5, 15e-9)
def r1(r2):
    q, par1, r3=solve(0.56e5, 100e-9)
    print(par1)
    r1= par1*r2/(r2-par1)
    a = r3/(r1*2)
    print(a)
    print(r1)
    print(q)
r1(47)

