'''
Implementation of fast (binary) exponentiation algorithm.
'''

def pow(a,b):
    '''Makes checks for trivial cases, determines the sign of the product and whether the inverse is taken; then runs the recursive algorithm and returns the result.'''
    if b==0 or a==1: return 1
    if a==-1: return -1 if b%2 else 1
    if a==0: return 0
    return (-1 if a<0 and b%2 else 1)*(fast_pow_now(abs(a),abs(b),1) if b>0 else 1/fast_pow_now(abs(a),abs(b),1))

def fast_pow_now(a, b, prod):
    '''Recursive algorithm for binary exponentiation in O(log(n)) time complexity.'''
    if b&1: prod*=a
    b>>=1
    if not b: return prod
    return fast_pow_now(a*a, b, prod) 

# User input
while True:
    print("Please enter integers.\nRaise: ")
    try:
        a=int(input())
        print("to the power of: ")
        b=int(input())
    except:
        continue
    break

print(f"The result is: {pow(a,b)}")
