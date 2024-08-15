# def max_num(a=120, b=180):
#     return max(a, b)
#
#
# print(max_num())


# def check_difference(num1=255, num2=120):
#     return num1, num2
#
#     if abs(num1-num2) == 135:
#         print("Yes")
#     else:
#         print("No")

def check_difference(num1, num2):
    if abs(num1-num2) == 135:
        return "Yes"
    else:
        return "No"

result = check_difference(255, 120)
print(result)
