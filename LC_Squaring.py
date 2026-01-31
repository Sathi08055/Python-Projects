a=5
b=input("Any number?")
try:
    sum=a+b
    print(sum)
except:
    raise ValueError("It is not a number")