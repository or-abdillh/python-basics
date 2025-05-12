def isYourAdult(age):

    return "You are an adult." if age > 18 else "You are a minor."

# get the age
age = int(input("Enter your age: "))

# check if the age is greater than 18
print(isYourAdult(age))

def fun(**args): 
    print(args.get("name"))

fun(name="oka rajeb abdillah", age=23, address="Jakarta")