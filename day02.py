# ** 대신 pow 함수
import math

def is_prime(num) -> bool:
    """
    소수 판정 함수  / 소수면 True, 아니면 False
    :param num: < integer >
    :return: < boolean >
    """
    if num >= 2:
        i = 2
        while(i <= int(math.pow(num,0.5)) + 1 ):
            if num % i == 0:
                return False
            i += 1
    else:
        return False

    return True

help(is_prime)

startNum = int(input("Start number : "))
endNum = int(input("End number : "))

i = startNum
while(i <= endNum):
    if is_prime(i):
        print(i)
    i += 1
