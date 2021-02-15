#largest

n1=float(input("Enter the first number: "));
n2=float(input("Enter the second number: "));
n3=float(input("Enter the Third number: "));
def largest():     
     if(n1>=n2) and (n1>=n2):
         largest=n1
     elif(n2>=n1) and (n2>=n3):
         largest=num2
     else:
         largest=n3
         print("Largest number is",largest)
largest()
pass

#sum of digits

n1=int(input("Enter the first number: "));
n2=int(input("Enter the second number: "));
n3=int(input("Enter the Third number: "));
def sum(a,b,c):
    sum=a+b+c
    return sum
print("the sum of three numbers is:",sum(n1,n2,n3))




#hcf of two numbers
def hcf(a,b):
    if a>b:
        small=b
    else:
        small=a
    for x in range(1,small+1):
        if((a%x==0)and (b%x==0)):
            result=x
    return result  
n2=int(input("Enter the second number: "));
n1=int(input("Enter the first number: "));
print("the hcf of n1 and n2 is",hcf(n1,n2))

#LCM OF TWO NUM

def lcm(a,b):
    if a>b:
        big=a
    else:
         big=b   
    while(True):
        if((big % a==0) and (big % b==0)):
            lcm=big
            break
        big+=1
    return lcm
n1=int(input("enter n1:")) 
n2=int(input("enter n2:")) 
print("the lcm of two num is:",lcm(n1,n2))

#leap year

def check(y):
    if(y % 100)==0:
        if(y % 4)==0:
            if(y % 400)==0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
y=int(input("enetr the year")) 
if(check(y)):
    print("leap year")
else:
    print("not a leap year")           


#type of triangle

s1=int(input("Enter the first number: "));
s2=int(input("Enter the second number: "));
s3=int(input("Enter the Third number: "));
def triangle(a,b,c):
    if(a==b and a==c):
        print("triangle is equilateral")
    elif(a==b or b==c or a==c):
        print("triangle is isosceles")
    else:
        print("trianle is scalar")
triangle(s1,s2,s3)

#roots of quadratic equation


import math
def equation(a,b,c):
    dis=b*b-4*a*c
    sv=math.sqrt(abs(dis))
    if dis > 0:
        print("real and diff roots")
        print((-b + sv)/(2 * a))
        print((-b - sv)/(2 * a))
    elif dis==0:
        print("roots are same")
        print(-b/(2*a))
    else:
        print("complex roots")

s1=int(input("Enter the first number: "));
s2=int(input("Enter the second number: "));
s3=int(input("Enter the Third number: "));
equation(s1,s2,s3)

#vowel or consonent


jch=input("enter a character")
def voc(l):
    if l in ('a','e','i','o','u'):
        print("%s is vowel:" %l)
    else:
        print("%s is consonent:" %l)
voc(ch)

#fibo series

numterms = int(input("How many terms? "))
num1,num2 = 0, 1
c = 0
if numterms <= 0:
   print("Please enter a positive integer")
elif numterms == 1:
   print("Fibonacci sequence upto",numterms,":")
   print(num1)
else:
   print("Fibonacci sequence:")
   while c < numterms:
       print(num1)
       nth = num1 + num2
       
       num1 = num2
       num2 = nth
       c+= 1

#factorial of number

def fact(n):
    if n== 1:
        return n
    else:
        return n* fact(n- 1)
n = int(input("Enter a Number: "))
if n< 0:
    print("Factorial cannot be found for negative numbers")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", n, "is: ", fact(n))
 
 
 #prime number within in a range

l  = 900
u= 1000
print("Prime numbers in the interval is")
for n in range(l, u+ 1):
   # all prime numbers are greater than 1
   if n > 1:
       for i in range(2, n):
           if (n % i) == 0:
               break
       else:
           print(n)

 #choice based arithmetic


c= int(input("Enter your choice:n"))  
if (c>=1 and c<=4):
  print("Enter two numbers: ")
  n1 = int(input())
  n2 = int(input())

  if c == 1: # To add two numbers
    res = n1 + n2
    print("Result = ", res)

  elif c== 2: # To subtract two numbers
    res = n1 - n2
    print("Result = ", res)

  elif c== 3: # To multiply two numbers
    res = n1 * n2
    print("Result = ", res)

  elif  c== 4: # To get quotient with decimal value
    res = n1 / n2
    print("Result = ", res)

  elif c == 5:
    exit()
else:
  print("Wrong input..!!")

#sum of triangle



def tri(p):
    r=0
    while p>0:
        c=1
        while c<=p:
            r+=c
            c+=1
        p==1
    return r   


#digital root
def dig(n):
    m=n
    res=0
    while  m>0:
        rem=m%10
        m//=10
        res+=rem
    while res // != 0:
        res = dig(n)
     return res  
n=int(input("enter n"))     

#to find ncr   

def nCr(n, r): 
    return (fact(n) / (fact(r)  
                * fact(n - r))) 
def fact(a): 
   k= 1
   for i in range(2, a+1): 
       k = k* i 
   return k
n = int(input("enyet n"))
r = int(input("enter r"))
print(int(nCr(n, r))) 


#pascal triangle //
def pascal_triangle(n):
    for i in range(0, m):
        for j in range(0, i+1):
            print(int(ncr(i,j)), end=' ')
        print("\n")


#sum of the factors //
def f_s(m):
    r = 0
    for x in range(1, m+1):
        if m % x == 0:
            r += x
    return r


#armstrong number //
def arm_number(a):
    r = 0
    c = a
    0X = 0
    while c>0:
        c //= 10
        x += 1
    c = a
    while c>0:
        rem = c%10
    c //= 10
        r += pow(rem, x)

    return r == a


#quadrant of a point on plane //
def quad(a,b):
    if a == 0 or b == 0:
        return None

    if a > 0:
        if b > 0:
            return 1
        else:
            return 4
    elif a < 0:
        if b > 0:
            return 2
        else:
            return 3

#generate super prime nos 
def sup_pri(a):
    l = prime_all(2, a)[0]
    l2 = []
    for x in range(len(l)):
        if isprime(x+1):
            l2.append(l[x])
    return l2

#number triangle //
def num_triangle(a):
    for x in range(1,a+1):
        for y in range(1,x+1):
            print(y, end=" ")
        print("\n")


#number pyramid //
def num_pyr(a):

    c = a - 1

    for x in range(1, a+1):
        for y in range(0, c):
            print(end=" ")
        c -= 1
        for y in range(1, x+1):
            print(y, end=".")
        
        print("\n")


