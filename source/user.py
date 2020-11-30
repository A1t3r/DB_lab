class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def get_user_information(self):
        return self.name + ":" + self.password