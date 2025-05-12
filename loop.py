import time

# get the range of loop
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
step = int(input("Enter the step: "))

for i in range(start, end, step):
    # adding delay
    time.sleep(1)

    print(i)