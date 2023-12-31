def div(x,y):
    return x+y

try:
    add(5, 'a')
except TypeError: #You dont need to specify the error, check next example
    print("TypeError occured")
except: #if type error is not the error, then this will run,try add
    print("Something else went wrong")
else:
    print("Check your code again")
finally:
    print("This will always run")
