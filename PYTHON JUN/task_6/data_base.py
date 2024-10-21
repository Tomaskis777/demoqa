class Data_Base:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f"соеденение с БД: {self.user}, {self.password}, {self.port}")

    @staticmethod
    def clode():
        print("закрытие соеденения с БД")


db = Data_Base('Иван', 1234, 35)
db2 = Data_Base('Петр', 4321, 53)
print(id(db), id(db2))

db.connect()
db2.connect()
