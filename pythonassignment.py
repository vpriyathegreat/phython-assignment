"assignment 1.0"

#star
#get n, n is the previous even number
#x=n-2
#stop

#start
#get n, n is the previous odd number
#x= n+2
#stop



x=20
y=4
print (x//y)

x=8
y=6
print(x//y)

x= 90
y=10
print (x//y)

"assignment 1.1"
#1
x= 10
y=10
print ( (x>y)or( x!=y))

x=8
y=2
print ( (x>y)and  ( x==y))

#2
x = 7
y=8
print( x>y)

x= 5
y=2
print ( x<y)

x=1
y =1
print (x<=y)

x=7
y=8
print (x>=y)


"assignment 1.2"
#1
def addition(a,b):
    print (a+b)

def subraction( a,b):
    print (a-b)


print ( "select operation")
print ("1. addition")
print ( "2.subraction")

while True :

    
    choice = input("Enter choice(1/2): ")

    
    if choice in ('1', '2'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", addition(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subraction(num1, num2))
        else:
            print("Invalid Input")



#2
def multiply(a,b,c,d):
    print(a*b*c*d)
multiply( 2,2,3,4)

def addition(a,b,c):
    print(a+b+c)
addition( 2,2,2)
            
            
        
 
 

