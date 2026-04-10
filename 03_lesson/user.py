class User:

    def __init__(self, fstname, lstname):
        self.userName = fstname
        self.userLstName = lstname

    def sayFstName(self):
        print("Имя ", self.userName)

    def sayLstName(self):
        print("Фамилия ", self.userLstName)

    def sayFlName(self):
        print("Имя и Фамилия ", self.userName, self.userLstName)
