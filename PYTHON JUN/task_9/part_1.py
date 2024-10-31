import re

# if re.fullmatch(r'python', 'python'):
#     print(True)
# else:
#     print(False)
#
#
# if re.fullmatch(r'\*python\.', '*python.'):
#     print(True)
# else:
#     print(False)


# my_list = ['123', '1', '12', 'test']
#
# for element in my_list:
#     if re.fullmatch(r'\w[a-z]+', element):
#         print(element)


# my_list = ['123', '1', '12', 'test']
#
# for element in my_list:
#     if re.fullmatch(r'\w[a-z]{1,5}', element):
#         print(element)


# my_list = ['123', '1', '12', 'test']
#
# for element in my_list:
#     if re.fullmatch(r'\d+', element):
#         print(element)


# result = re.fullmatch(r'\d{3}', '123')
# not_result = re.fullmatch(r'\d{3}', '123 - no string')
#
# print(result.group())
# print(not_result)


# result = re.match(r'\d{2}', '123 - no string')
# not_result = re.match(r'\d{2}', 'string')
#
# print(result.group())
# print(not_result)


# result = re.search(r'\d{2}', 'string, 123 - no string')
#
# print(result.group())


# result = re.findall(r'\d{2}', '12 string, 34 - no string 56')
#
# print(result)


def check_email(email: str):
    return bool(re.fullmatch(r'\w{1,30}@\w{1,10}\.\w{1,10}', email))


print(check_email('tttt@ttt.tt'))
