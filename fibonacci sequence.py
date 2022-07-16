n = int(input("Which fibonacci number number would you like to know? "))
a = 1
b = 1
c = 0
i = 3
while i <= n:
    c = a + b
    a = b
    b = c
    i = i+1
print (c)
f = int(input("Enter a number to check if it is fibonacci: "))
import math
 
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
 
def isFibonacci(f):
 

    return isPerfectSquare(5*f*f + 4) or isPerfectSquare(5*f*f - 4)
    
if isFibonacci(f) == True:
    print (f,"is a Fibonacci Number")
    
else:
    print (f,"is not a Fibonacci Number")

def nearestFibonacci(num):
     
    if (num == 0):
        print(0)
        return
 

    first = 0
    second = 1
 
    third = first + second
 

    while (third <= num):
         
        first = second
 
        second = third
 
        third = first + second
 

    if (abs(third - num) >=
        abs(second - num)):
        ans =  second
    else:
        ans = third
 
    print(ans, "is the closest Fibonacci Number")
 
if __name__ == '__main__':
     
    N = f
     
    nearestFibonacci(N)
