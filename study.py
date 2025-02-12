# # v0.5 day02

# x = 2
# y = x + 5  # NameError: name 'x' is not defined
# print(y)
#
# print(type(3.14))
# print(type(3.14) == float)
# print(isinstance(3.14, float))
# print(isinstance("Inha", float))
# print(isinstance(55, float))
#
# artists = ['BTS', '뉴진스', '핑클', 'SES', 'HOT', '블랙핑크']
# groups = artists
# print(artists, groups)
# artists[2] = '세븐틴'
# print(artists, groups)
# #=========================================================


# # v0.6 day02

# base_number = int(input('Input base number : '))
# exponent_number = int(input('Input exponent number : '))
# print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {base_number**exponent_number}')
#
# money = 5,000,000 # 파이썬에서 쉼표를 사용하면 자동으로 tuple이 생성됨
# print(money)
# print(type(money))  # tuple
# cash = 5_000_000
# print(cash)
# print(type(cash))  # int
# #============================================================


# # v0.7 day02
#
# base_number = int(input('Input base number : '))
# exponent_number = int(input('Input exponent number : '))
# print(type(base_number), type(exponent_number))
# # f-string
# print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {base_number**exponent_number}')
# print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {pow(base_number, exponent_number)}')
#
# # format function
# print('밑은 {0}, 지수는 {1}, 결과 값은 {2}'.format(base_number, exponent_number, pow(base_number, exponent_number)))
# print('밑은 {}, 지수는 {}, 결과 값은 {}'.format(base_number, exponent_number, pow(base_number, exponent_number)))
#
# # c like
# print('밑은 %d, 지수는 %d, 결과 값은 %d' % (base_number, exponent_number, pow(base_number, exponent_number)))
## ==============================================================

# # v0.8 day02
#
# first_number = int(input("First number : "))
# second_number = int(input("Second number : "))
#
# print(f'몫은 {divmod(first_number, second_number)[0]} 나머지는 {divmod(first_number, second_number)[1]}입니다')

# first_number = int(input("First number : "))
# second_number = int(input("Second number : "))
#
# quotient = first_number // second_number
# remainder = first_number % second_number
# print(f'몫은 {quotient} 나머지는 {remainder} 입니다')
## =================================================================

# # v0.9 day02
#
# dec = 65
# octal = 0o101
# hexadecimal = 0x41
# binary = 0b01000001
# print(dec, octal, hexadecimal, binary)
# print(chr(dec), chr(octal), chr(hexadecimal), chr(binary))
# print(bin(dec), bin(octal), bin(hexadecimal), bin(binary))
# print(ord('B'), ord('Z'), ord('a'), ord('2'))  # 66, 90, 97, 50
# # ======================================================================

# # v1.0 day02
#
# # (100°F − 32) × 5/9 = 37.778°C
# fahrenheit = float(input('Input Fahrenheit : '))
# print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')
# # =======================================================================

# # v1.1 day02
#
# # (100°F − 32) × 5/9 = 37.778°C
# # (0°C × 9/5) + 32 = 32°F
#
# menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Quit program : ")
#
# if menu == '1':
#     fahrenheit = float(input('Input Fahrenheit : '))
#     print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')
# elif menu == '2':
#     celsius = float(input('Input Celcius : '))
#     print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
# # ===========================================================================

# # v1.2 day02
#
# # (100°F − 32) × 5/9 = 37.778°C
# # (0°C × 9/5) + 32 = 32°F
# menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Quit program : ")
#
# if menu == '1':
#     fahrenheit = float(input('Input Fahrenheit : '))
#     print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')
# elif menu == '2':
#     celsius = float(input('Input Celsius : '))
#     print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
# else:
#     print('Terminate Program.')
#
# # temp = [0]
# # temp = []
# # if temp:
# #     print("원소가 존재하는 리스트")
# # else:
# #     print("비어있는 리스트")
# # ===================================================

# # v1.3 day02
# letter = input('Input alphabet letter : ')
# # vowels = {'a', 'e', 'i', 'o', 'u'}  # set
# vowels = "aeiuo"  # str
# print(type(vowels))
# if letter in vowels:  # in
#     print(f'{letter} is a vowel~')
# else:
#     print(f'{letter} is a consonant!')
# # ===================================================

# # v1.4 day02

# l = [1, 3, 3, 2, 4]  # list
# s = {1, 3, 3, 2, 4}  # set
# print(l, s)  # [1, 3, 3, 2, 4] {1, 2, 3, 4}
# # =======================================================

# # v1.5 day03
#
# # Assignment (loop)
# # (100°F − 32) × 5/9 = 37.778°C
# # (0°C × 9/5) + 32 = 32°F
#
# while True:
#     menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Quit program : ")
#
#     if menu == '1':
#         fahrenheit = float(input('Input Fahrenheit : '))
#         print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')
#     elif menu == '2':
#         celsius = float(input('Input Celsius : '))
#         print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
#     elif menu == '3':
#         print('Terminate Program.')
#         break
## =================================================

# v1.6 day6
university = "Inha\nUniversity!"
#university = r"Inha\nUniversity!"  # raw string
print(university)

# slicing
# print(university[:3]) # [:3]이면 3번째 인덱스 전까지 이기 때문에 Inh 까지만 출력됨
# print(university[:4])
print(university[:-11])
print(len(university)) # 공백도 포함!
# print(university[0:len(university)])
# print(university[:16])
# print(university[::2])
#
# number1 = input("First number : ")
# number2 = input("Second number : ")
# print(number1 + number2)  # concatenation
# print(number1 * 3)  # duplicate
# print(number1 + 3)  # TypeError: can only concatenate str (not "int") to str









# # v4.0 day04
# sugang = dict(python="kim", cpp="sung", db="kang") #dict은 p ython = "kim" 공란이 있으면 불가능, 1="kim" 키 값이 숫자면 불가능, 문자열만 가능
# sugang = {'python':'kim', 'cpp':'sung', 'db':'kang'}
# print(sugang)
# sugang['datastructure'] = 'kim'  # add
# print(sugang)
# sugang['datastructure'] = 'park'  # update
# print(sugang)
# # print(sugang['db'])
# # print(sugang.get('db'))
# # print(sugang.get('opensource'))
# # print(sugang.get('opensource', 'not exist'))
# for subject, professor in sugang.items():
#     print(f'{subject} 과목 담당교수는 {professor}입니다')
#
# #for k in sugang.keys():
# for k in sugang:
#     print(k)
#
# for v in sugang.values():
#     print(v)
#
# for s in sugang.items():
#     print(s)
##======================================================

#v4.1 day4
#
# drinks_foods = {"위스키": "초콜릿", "와인": "치즈", "소주": "삽겹살", "고량주": "양꼬치"}
#
# # drink = input(drinks_foods.keys())
# drinks_foods_keys = list(drinks_foods)
# # print(drinks_foods_keys)
#
# while True:
#     menu = input(f'다음 술중에 고르세요.\n1) {drinks_foods_keys[0]}   2) {drinks_foods_keys[1]}   3) {drinks_foods_keys[2]}   4) {drinks_foods_keys[3]}   5) 종료 : ')
#     if menu == '1':
#         print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[0]]} 입니다')
#     elif menu == '2':
#         print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[1]]} 입니다')
#     elif menu == '3':
#         print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[2]]} 입니다')
#     elif menu == '4':
#         print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[3]]} 입니다')
#     elif menu == '5':
#         print(f'다음에 또 오세요')
#         break
# #------------------------------------

# #v4.2 day02
# import random
# drinks_foods = {"위스키": "초콜릿", "와인": "치즈", "소주": "삽겹살", "고량주": "양꼬치"}
# # print(drinks_foods)
# # print(drinks_foods.pop("고량주"))
# # print(drinks_foods)
#
# del drinks_foods["위스키"]
# #drinks_foods["사케"] = "광어회"
# japan_drinks_foods = {"사케": "광어회", "위스키": "낙곱새"}
# drinks_foods.update(japan_drinks_foods)
# print(drinks_foods)
# #drink = input(drinks_foods.keys())
# drinks_foods_keys = list(drinks_foods)
# # print(drinks_foods_keys)
# # #print(drinks_foods_keys.pop(0)) //pop(0) -> 맨 앞 키 값 지움
# # print(drinks_foods_keys.remove("위스키"))
# # print(drinks_foods_keys)
# #print(random.choice(drinks_foods_keys))
#
# while True:
#     menu = input(f'다음 술중에 고르세요.\n1) {drinks_foods_keys[0]}   2) {drinks_foods_keys[1]}   3) {drinks_foods_keys[2]}   4) {drinks_foods_keys[3]}   5) {drinks_foods_keys[4]}   6) 아무거나   7) 종료 : ')
#     if menu == '1':
#         print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[0]]} 입니다')
#     elif menu == '2':
#         print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[1]]} 입니다')
#     elif menu == '3':
#         print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[2]]} 입니다')
#     elif menu == '4':
#         print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[3]]} 입니다')
#     elif menu == '5':
#         print(f'{drinks_foods_keys[4]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[4]]} 입니다')
#     elif menu == '6':
#         random_drink = random.choice(drinks_foods_keys)
#         print(f'{random_drink}에 어울리는 안주는 {drinks_foods[random_drink]} 입니다')
#     elif menu == '7':
#         print(f'다음에 또 오세요')
#         break
# #-----------------------------------------
#
# import random
#
# star = ['테란','저그','프로토스']
# print(random.choice(star))
# print(random.randint())
# print(star[random.randint()])

#-----------------------------------------
#v4.3 day05
# Assignment ex 8.10
# squares = {n: pow(n, 2) for n in range(10)}
#squares = {n: n**2 for n in range(10)}
# squares = {n: n*n for n in range(10)}
# print(squares)

# univ = 'inha university'
# counts_alphabet = {letter: univ.count(letter) for letter in univ}  # dictionary comprehension
# print(counts_alphabet, len(counts_alphabet))
#
# univ = 'inha university'
# counts_alphabet = dict() #dictionary key 값은 중복이 될 수 없음
# for letter in univ:
#     counts_alphabet[letter] = univ.count(letter)
# print(counts_alphabet)
