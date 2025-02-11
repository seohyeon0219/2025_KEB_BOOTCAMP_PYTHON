# 소수 찾기 프로그램
def is_prime(num) -> bool:
    """
    소수 판정 함수  / 소수면 True, 아니면 False
    :param num: < integer >
    :return: < boolean >
    """
    if num >= 2:
        i = 2
        while(i <= int(num**0.5) + 1 ):
            if num % i == 0:
                return False
            i += 1
    else:
        return False

    return True

help(is_prime)

n = int(input("Input number : "))
if is_prime(n):
    print(f"{n} is prime number")
else:
    print(f"{n} is NOT prime number")
