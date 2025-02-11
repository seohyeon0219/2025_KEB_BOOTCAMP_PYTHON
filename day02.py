# dan = int(input("Input dan : "))
# for i in range(1, 10):
#     print(f"{dan} * {i} = {dan*i}")

# for dan in range(2, 10, 1):
#    for i in range(1, 10):
#        print(f"{dan} * {i} = {dan*i}")

n = int(input("Input number : "))

is_prime = True

if n >= 2:
    for i in range(2, n):
        if n % i == 0:
            # count = count + 1
            is_prime = False
            break
        print(i, end = ' ')
else:
    if_prime = False

# if count == 0:
if is_prime:
    print(f"{n} is prime number")
else :
    print(f"{n} is not prime number")