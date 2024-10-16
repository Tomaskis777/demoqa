class Data_Base:
    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f"соеденение с БД: {self.user}, {self.password}, {self.port}")

    @staticmethod
    def clode():
        print("закрытие соеденения с БД")

