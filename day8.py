#FIB0NACCI

def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range (2,n):
        c=a+b
        a=b
        b=c
        print(c)

def fib_sec(func):
    def inner (a,b):
        if a>b:
            a,b=b,a
        print(func(a,b))
        
    return inner 



k=fib_sec(fib)
fib(10)
    
    
#EXCEPTION HANDLING

try:
    file=open("day4.py", "r")
    print(file.read())
except exe as e:
    print("wt the hakkkk")
    fd=file.write("heart blinks")
    print(fd)
    file.close()
finally:
    print("hloooo")
