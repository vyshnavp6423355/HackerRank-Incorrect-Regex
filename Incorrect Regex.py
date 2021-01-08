import re
T = int(input())
for i in range(0, T):
    regex_input = input()
    try:
        regex = re.compile(regex_input)
    except re.error:
        print(False)
    else:
        print(True)
