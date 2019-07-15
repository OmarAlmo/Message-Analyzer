class UserNode:
    def __init__(self, user):
        self.user = user
        self.count = 0

        self.next = None

    def getCount(self):
        return self.count

    def getuser(self):
        return self.user

    def setCount(self, new_count):
        self.count = new_count

    def setuser(self, newUser):
        self.user = newUser


    def hasUser(self, user):
        if self.user == user:
            return True
        else:
            return False