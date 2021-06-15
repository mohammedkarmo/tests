import cmath
def fun(a,b,c):
    d=(b**2)-(4*a*c)
    root1 = (-b-cmath.sqrt(d))/(2*a)
    root2 = (-b+cmath.sqrt(d))/(2*a)
    print('the solution are {0} and {1}'.format(root1,root2))
fun(1,3,0)