import re
from userNode import UserNode
from linkedList import LinkedList


PARSE_REGEX = "(?P<date>\d{4}-\d{2}-\d{2}, \d{2}:\d{2}) - (?P<username>\w+): (?P<message>[^,]+)"
USER_LIST = LinkedList()

def parse(line):
	m = re.match(r"(?P<date>\d{4}-\d{2}-\d{2}, \d{2}:\d{2}) - (?P<username>\w+): (?P<message>[^,]+)", line, re.M|re.I)

	date = m.group('date')
	user = m.group('username')
	message = m.group('message')

	if (USER_LIST.searchUser(user) == False):
		user = UserNode(user)
		user.count += 1
		USER_LIST.add(user)
	else:
		USER_LIST.updateUserCount(user)


def main():
	print("Enter file path:")
	filepath = input()

	f = open(filepath, "r")

	line = f.readline()
	while line:
		parse(line)
		line = f.readline()
	f.close()

	USER_LIST.printList()
main()