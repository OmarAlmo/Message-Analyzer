import re

PARSE_REGEX = "(?P<date>\d{4}-\d{2}-\d{2}, \d{2}:\d{2}) - (?P<username>\w+): (?P<message>[^,]+)"


def parse(line):
	m = re.match(r"(?P<date>\d{4}-\d{2}-\d{2}, \d{2}:\d{2}) - (?P<username>\w+): (?P<message>[^,]+)", line, re.M|re.I)

	date = m.group('date')
	username = m.group('username')
	message =  m.group('message')

def main():
	print("Enter file path:")
	filepath = input()

	f = open(filepath, "r")

	line = f.readline()
	while line:
		parse(line)
		line = f.readline()
	f.close()

main()