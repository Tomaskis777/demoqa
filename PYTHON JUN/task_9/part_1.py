import re

if re.fullmatch(r'python', 'python'):
    print(True)
else:
    print(False)


if re.fullmatch(r'\*python\.', '*python.'):
    print(True)
else:
    print(False)