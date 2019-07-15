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

        current_node = self.head

        while current_node is not None:
            if current_node.hasUser(user):
                return True
            else:
                current_node = current_node.next

        return False

    def updateUserCount(self, user):
        current_node = self.head

        while current_node is not None:
            if current_node.hasUser(user):
                current_node.count += 1
                break
            else:
                current_node = current_node.next

    def printList(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.user + ' => count: ' + str(current_node.count))
            current_node = current_node.next

        return