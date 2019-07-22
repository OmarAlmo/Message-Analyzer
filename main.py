from linkedList import LinkedList
from parse import Parse

USER_LIST = LinkedList()

def main():

	print("Enter file path:")
	filepath = input()

	f = open(filepath, "r")

	line = f.readline()
	while line:
		Parse.parse(line, USER_LIST)
		line = f.readline()
	f.close()

	print("Final List:\n")
	USER_LIST.printList()
main()