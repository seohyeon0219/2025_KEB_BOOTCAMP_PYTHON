#1
def bomb_repetition(n):
    for i in range(n, 0, -1):
        print(i)
    print("펑")

def bomb_recursion(n):
    if n == 0:
        print("펑")
    else:
        print(n)
        bomb_recursion(n-1)

#2 교수님 코드
def countdown_loop(n):
    for i in range(n, -1, -1):
        if i == 0:
            print("펑~")
        else:
            print(i)


def countdown_recursion(n):
    if n < 0:
        return
    if n == 0:
        print("펑!")
    else:
        print(n)
    countdown_recursion(n-1)


n = int(input())
#countdown_loop(n)
countdown_recursion(n)