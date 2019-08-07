from userNode import UserNode
import re

# Format = YYYY-MM-DD, HH:MM - username: message
FORMAT_1 = r"(?P<date>\d{4}-\d{2}-\d{2}, \d{2}:\d{2}) - (?P<username>.+?[$:])(?P<message>.+)"

# Format = YYYY-MM-DD, HH:MM:SS XP - username: message
FORMAT_2 = r"(?P<date>\d{4}-\d{2}-\d{2}, \d{1|2}: \d{2}:\d{2} [AM|PM]) - (?P<username>.+?[$:])(?P<message>.+)"

# Format = MM/DD/YY, HH:MM - username: message
FORMAT_3 = r"(?P<date>\d{1,2}/\d{1,2}/\d{2}, \d{2}:\d{2}) - (?P<username>.+?[$:])(?P<message>.+)"

# Format = MM-DD-YY, HH:MM:SS AM|PM - username: message
FORMAT_4 = r"(?P<date>\d{1,2}/\d{1,2}/\d{2}, \d{2}:\d{2}:\d{2} [AM|PM]) - (?P<username>.+?[$:])(?P<message>.+)"


class Parse:
    def parse(line, userList):
        flag = False

        if re.match(FORMAT_1, line):
            m = re.match(FORMAT_1, line)
            user = m.group('username')[:-1]
            flag = True

        elif re.match(FORMAT_2, line):
            m = re.match(FORMAT_2, line)
            user = m.group('username')[:-1]
            flag = True

        elif re.match(FORMAT_3, line):
            m = re.match(FORMAT_3, line)
            user = m.group('username')[:-1]
            flag = True

        elif re.match(FORMAT_4, line):
            m = re.match(FORMAT_4, line)
            user = m.group('username')[:-1]
            flag = True


        if flag:
            if (userList.searchUser(user) == False):
                user = UserNode(user)
                user.count += 1
                userList.add(user)
            else:
                userList.incrementUserCount(user)

