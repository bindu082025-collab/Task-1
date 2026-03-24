# Name:M Bindu

#Sum of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total=num1+num2 #Calculating sum
print("The sum is: ",total) # printing the result

# Odd or Even Checker 
a=int(input("Enter a number: "))
if a%2==0:
    print("Even number")
else:
    print("Odd number")

#Factorial Calculation
b=int(input("Enter a number: "))
fact=1
for i in range(1,b+1):
    fact=fact*i
print("Factorial is: ",fact)

#Fibonacci series
num=int(input("Enter number of terms: "))
a=0
b=1
print("Fibonacci series: ")
for i in range(num):
    print(a,end=" ")
    c=a+b
    a=b
    b=c

#String Reverse
W=input("\nEnter a string: ")
rev=W[::-1]
print("Reversed String: ",rev)

#Palindrome Check
W1=input("Enter a string: ")
R=W1[::-1]
if W1==R:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

#Leap year check
year=int(input("Enter a year: "))
if year%4==0:
    if year%100 ==0:
        if year%400==0:
            print("Leap year")
        else:
            print("Not a Leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

#Armstrong number
n=int(input("Enter a number: "))
temp=n
length=len(str(n))
sum1=0
while temp > 0:
    digit=temp%10
    sum1+=digit**length
    temp=temp//10
if sum1==n:
    print("It is a Armstrong number")
else:
    print("It is not an Armstrong number")
