print(7 in [1,2,34,5,6,9])

name = input("Enter your name: ")

if name in "oka rajeb abdillah":
    print("oka rajeb abdillah")
else:
    raise TypeError("You are not okarajebabdillah")

for i in range(12):
    if i % 2 is 0:
        print(f"{i} is even")
    elif i == 9:
        break
    else:
        continue

a, b = 4, 0

try:
    k= a/b

except ZeroDivisionError:
    print("You cannot divide by zero")

finally: 
    print("This will always execute")

assert b == 0, "b cannot be zero"

def fun():

    yield "Hello"

    yield "World"

    yield "!"

    return "Hello"

for str in fun():
    print(str)

hello = lambda name: f"Hello {name}"

print(hello("oka rajeb abdillah"))