def add (number):
    print(number,"in add")
    number = number+1
    return number

def times (number):
    print(number,"in times")
    number = number*2
    return number

def hundred (number):
    print(number,"in hundred")
    number = 100
    return number

x = 5
x = hundred(x)
x = times(x)
x = add(x)
print(x)