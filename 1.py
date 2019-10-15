import re

#
# line = "Cats are smater than dogs "
# matchObj = re.match(r'(.*) are (.*?) (.*)', line, re.M | re.I)
#
# if matchObj:
#     print(matchObj.group())
#     print(matchObj.group(1))
#     print(matchObj.group(2))
#     print(matchObj.group(3))
#

s = '1102231990xxxxxxxx'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})', s)
print(res.groupdict())
