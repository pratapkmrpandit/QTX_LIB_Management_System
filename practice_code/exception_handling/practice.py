n=0
try:
    res=10/n
    print(res)
except ZeroDivisionError:               # here we use exception handling that handle the exception 
    print("not divisiable by zero")     # exception i.e netowrk error , file not found , invalid input

a=10
b=10
try:
    res=a/b
    print(res)
except ZeroDivisionError:
    print("not divisiable by zero")
else:                                   # here we use else this else excecute when try block exceute properly
    print("exception does not occur")
finally:                                # here finally excecute when exception cause or not occur in both time
    print("end of code")

a=10
b="python"
try:
    res=a/int(b)
    print(res)
except ValueError:                      # here i am using the ValueError it occur due to value
    print("not divisible by str")

a=["10","ten",20]
try:
    s=int(a[0])+int(a[5])
    print(s)
except (ValueError,TypeError) as e:      # here both ValueError and TypeError occur it print the error 
    print("Error",e)
except IndexError:                       # here i use IndexError so if it cross the index this line of code excecute
    print("out of index")