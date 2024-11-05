import matplotlib.pyplot as plt


with open('data.txt', 'r') as f:
    def my_int(x):
        try:
            return int(x)
        except:
            return x


    data = list(filter(lambda x: type(x) == int, map(my_int, list(f.read()))))

print(data)

plt.plot(data)
plt.show()