# Assignment
# v2.7) Bug fix (아무거나 및 종료) 정수형 리터럴 제거

import random

# d_s_p = {"위스키" : ['초콜릿',50_000]}
# print(d_s_p["위스키"][1])

drinks = ['위스키','와인','소주','고량주']
foods = ["초콜릿","치즈","삽겹살","양꼬치"]
prices = [50000, 30000, 5000, 7500]
amounts = [0 for i in range(len(drinks))]

drinks.append('사케')
foods.append('광어회')
# prices.append(25000)
# amounts.append(0)

foods[0] = '낙곱새'
# drinks.append("데낄라")
# foods.append("소금")
# prices.append(35000)

total_price=0

def print_menu_total_price(n):
    global total_price
    print(f'{drinks[n]}에 어울리는 안주는 {foods[n]}입니다.')
    print(f'가격: {prices[n]}')
    amounts[n]= amounts[n]+1
    total_price = total_price + prices[n]

menu_list = '다음 술 중에 고르세요.\n'
for i in range(len(drinks)):
    menu_list = menu_list + f'{i+1}) {drinks[i]}'
menu_list = menu_list + f'{len(drinks)+1}) 아무거나 {len(drinks)+2}) 종료 : '

# while True:
    # menu = input(f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) {drinks[4]}   6) 아무거나   7) 종료 : ')
    # if menu == '1':
    #     print(f'{drinks[0]}에 어울리는 안주는 {foods[0]} 입니다')
    # elif menu == '2':
    #     print(f'{drinks[1]}에 어울리는 안주는 {foods[1]} 입니다')
    # elif menu == '3':
    #     print(f'{drinks[2]}에 어울리는 안주는 {foods[2]} 입니다')
    # elif menu == '4':
    #     print(f'{drinks[3]}에 어울리는 안주는 {foods[3]} 입니다')
    # elif menu == '5':
    #     print(f'{drinks[4]}에 어울리는 안주는 {foods[4]} 입니다')
    # elif menu == '6':
    #     random_index = random.randint(0, len(drinks)-1)
    #     print(f'{drinks[random_index]}에 어울리는 안주는 {foods[random_index]} 입니다')
    # elif menu == '7':
    #     print(f'다음에 또 오세요')
    #     break
    #
while True:
    menu = int(input(menu_list))
    if 1 <= menu <= len(drinks):
        print_menu_total_price(menu-1)
    elif menu == len(drinks)+1:
        random_index = random.randint(0,len(drinks)-1)
        print(f'{drinks[random_index]}에 어울리는 안주는 {foods[random_index]}')
    elif menu == len(drinks)+2:
        print(f'다음에 또 오세요.')
        break

for k in range (len(drinks)):
    if amounts[k] != 0:
        print(f'주류명 : {drinks[k]} 수량 : {amounts[k]} 단가 : {prices[k]} 소계 : {prices[k] * amounts[k]}')

print(f'총 금액 : {total_price}원')



# ==========================================================================================

import random

# def printMenu(menu): #input()을 통해서는 항상 str(문자열)로만 반환됨 #def
#     choice = int(menu)
#     print(f'{drinks[choice-1]}에 어울리는 안주는 {foods[choice-1]} 입니다')
#
# drinks = ["위스키","와인","소주","고량주","사케"]
# foods = ["초콜릿","치즈","삼겹살","양꼬치","광어"]

# dictionary 함수 리스트로 구현
{
# print(drinks_foods.pop("고량주"))
# for index, value in enumerate(drinks):
#     if value=="고량주":
#         print(foods[index])
#         foods.remove(foods[index])
#         drinks.remove(value)
#         break

# #del drinks_foods["위스키"]
# for index, value in enumerate(drinks):
#     if value=="위스키":
#         foods.remove(foods[index])
#         drinks.remove(value)
#         break

#drinks_foods["사케"] = "광어회"
# count= 0
# for index, value in enumerate(drinks):
#     if value=="사케":
#         foods[index] = "광어회"
#         break
#     count += 1
# if count == len(drinks):
#     drinks.append("사케")
#     foods.append("광어회")
}

# while True:
#     menu = 0
#     menuText = "다음 술중에 고르세요.\n"
#     for index, value in enumerate(drinks): # 리스트의 인덱스와 값을 동시에 가져올 수 있음
#         menuText += str(index + 1) + ") " +  value + "  "
#     menuText +=  str(len(drinks) + 1) + ")  아무거나 " + str(len(drinks) + 2) + ")  종료 : "
#
#     menu = input(menuText)
#
#     if menu == str(len(drinks) + 1):
#         menu = random.randint(1,len(drinks)) # random.randint(a,b) -> a부터 b 중 랜덤한 정수를 생성
#         printMenu(menu)
#     elif menu == str(len(drinks) + 2):
#         print(f'다음에 또 오세요')
#         break
#     else:
#         printMenu(menu)


# for x,y in enumerate(drinks):
#     print(x)
#     print(y)

