from userNode import UserNode
import re

# Format = YYYY-MM-DD, HH:MM - username: message
FORMAT_1 = r"(?P<date>\d{4}-\d{2}-\d{2}, \d{2}:\d{2}) - (?P<username>\w+): (?P<message>[^,]+)"

# Format = YYYY-MM-DD, HH:MM:SS XP - username: message
FORMAT_2 = r"(?P<date>\d{4}-\d{2}-\d{2}, \d{1}:\d{2}:\d{2} [APM]) - (?P<username>\w+): (?P<message>[^,]+)"

# Format = YYYY-MM-DD, HH:MM - username: message
# r"(?P<date>\d{1,2}/\d{1,2}/\d{2}, \d{2}:\d{2}) - (?P<username>.\w+|\w.+):(?P<message>.+)"
# r"(?P<date>\d{1,2}/\d{1,2}/\d{2}, \d{2}:\d{2}) - (?P<username>.\w+|\w.+)(: )(?P<message>.+)"
FORMAT_3 = r"(?P<date>\d{1,2}/\d{1,2}/\d{2}, \d{2}:\d{2}) - (?P<username>.\w+|\w.+[ :])(?P<message>.+)"

# Format = YYYY-MM-DD, HH:MM:SS XP - username: message
FORMAT_4 = r"(?P<date>[1-31]/[1-12]/\d{2}, \d{2}:\d{2}:\d{2} [AM|PM]) - (?P<username>(\w+)*.+): (?P<message>[^,]+)"


class Parse:
    def parse(line, USER_LIST):
        flag = False

        if re.match(FORMAT_1, line, re.M | re.I):
            m = re.match(FORMAT_1, line, re.M | re.I)
            user = m.group('username')
            flag = True

        elif re.match(FORMAT_2, line, re.M | re.I):
            m = re.match(FORMAT_2, line, re.M | re.I)
            user = m.group('username')
            flag = True

        elif re.match(FORMAT_3, line, re.M | re.I):
            m = re.match(FORMAT_3, line, re.M | re.I)
            user = m.group('username')
            flag = True

        elif re.match(FORMAT_4, line, re.M | re.I):
            m = re.match(FORMAT_4, line, re.M | re.I)
            user = m.group('username')
            flag = True


        if flag:
            if (USER_LIST.searchUser(user) == False):
                user = UserNode(user)
                user.count += 1
                USER_LIST.add(user)
            else:
                USER_LIST.incrementUserCount(user)

