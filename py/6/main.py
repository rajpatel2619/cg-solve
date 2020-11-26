from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

def jacobi(A,b,N=25,x=None):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Create an initial guess if needed                                                                                                                                                            
    if x is None:
        x = zeros(len(A[0]))

    # Create a vector of the diagonal elements of A                                                                                                                                                
    # and subtract them from A                                                                                                                                                                     
    D = diag(A)
    R = A - diagflat(D)

    # Iterate for N times                                                                                                                                                                          
    for i in range(N):
        x = (b - dot(R,x)) / D
    return x

A = array([[50,1,10,-5],[0.0,20.2,20,1],[2,-2,19,6],[-4,7,1,32]])
b = array([4.0,2.0,-3,0.1])
guess = array([1.0,1.0,1.0,1.0])

sol = jacobi(A,b,N=25,x=guess)

print ("A:")
pprint(A)


print ("b:")
pprint(b)


print ("x:")
pprint(sol)