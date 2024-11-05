# with open('data.txt', 'w+') as f:
#
#     f.write('test file\n')
#
#     data = ['test\n', 'line\n', 'write\n']
#     f.writelines(data)
#
# # f = open('data.txt', 'w+')
# # f.close()
#
# with open('data.txt', 'r') as f:
#
#     data = f.read()
# print(data)


with open('data.txt', 'r') as f:
    def my_int(x):
        try:
            return int(x)
        except:
            return x


    data = list(filter(lambda x: type(x) == int, map(my_int, list(f.read()))))

print(data)
