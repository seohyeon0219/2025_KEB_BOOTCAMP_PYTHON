# dan = int(input("Input dan : "))
# for i in range(1, 10):
#     print(f"{dan} * {i} = {dan*i}")

# for dan in range(2, 10, 1):
#    for i in range(1, 10):
#        print(f"{dan} * {i} = {dan*i}")

print(type(2**10)) #1024
print(type(16**0.5)) #4.0
#반복문에서 float는 x이므로 형 변환해야 함

def is_prime(num) -> bool: #is_~ -> true or false
    """
    소수 여부를 판정해서 소수면 true, 소수가 아니면 false를 리턴하는 함수
    A function that returns True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if num >= 2:
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                return False
                #is_prime = False
                #break
            #print(i, end=' ')

    else:
        return False
    return True

#main
help(abs) #abs함수에 대한 설명
help(is_prime) #내가 만든 is_prime 함수에 대한 설명
n = int(input("Input number : "))

# if count == 0:
if is_prime(n): #function call
    print(f"{n} is prime number")
else :
    print(f"{n} is not prime number")

