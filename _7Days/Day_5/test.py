import re

with open('urls') as fp:
    array = fp.readlines()

reg = "last_id=\d+"

id_list = []
for i in re.findall(reg, str(array)):
    id_list.append(int(i[8:]))

for i in range(len(id_list)):
    print(id_list[i])
    print(id_list[i - 1] - id_list[i])


