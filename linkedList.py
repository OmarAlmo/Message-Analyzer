class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        return

    def add(self, user):
        if self.head is None:
            self.head = user
        else:
            self.tail.next = user

        self.tail = user

        return

    def searchUser(self, user):

        currentUser = self.head

        while currentUser != None:
            if currentUser.hasUser(user):
                return True
            else:
                currentUser = currentUser.next

        return False

    def incrementUserCount(self, user):
        currentUser = self.head
        while currentUser != None:
            if currentUser.hasUser(user):
                currentUser.count += 1
                break
            else:
                currentUser = currentUser.next

    def getTotalCount(self):
        currentUser = self.head
        totalCount = 0
        while currentUser != None:
            totalCount += currentUser.count
            currentUser = currentUser.next
        return totalCount

    def printList(self):
        current = self.head
        total = self.getTotalCount()
        while current != None:
            print("{}: count = {}; percent => {}%.".format(current.user, current.count, round(current.count/total * 100, 2)))

            current = current.next