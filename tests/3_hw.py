# def max_num(a=120, b=180):
#     return max(a, b)
#
#
# print(max_num())
#
#
# def check_difference(num1, num2):
#     if abs(num1-num2) == 135:
#         return "Yes"
#     else:
#         return "No"
#
# results = check_difference(255, 120)
# print(results)


# def year_seasons(season_of_year):
#     if season_of_year == 12 or season_of_year == 1 or season_of_year == 2:
#         print('Зима')
#     elif 3 <= season_of_year <= 5:
#         print('Весна')
#     elif 6 <= season_of_year <= 8:
#         print('Лето')
#     elif 9 <= season_of_year <= 11:
#         print('Осень')
#     else:
#         print('Введите корректный месяц')
#
#
# year_seasons(1)


# def another_number(a=15, b=25, c=55):
#     # return (a, b, c)
#     if (a, b, c) ==> 10:
#         return "Yes"
#     else:
#         return "No"
#
# print(results)


def check_numbers(num1, num2, num3):
    if num1 > 10 and num2 > 10 and num3 > 10:
        return "yes"
    else:
        return "no"


result = check_numbers(15, 22, 55)
print(result)
