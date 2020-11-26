import string
import random
#获取a-z A-Z
strings=list(string.ascii_letters)
for i in range(10):
    strings.append(str(i))
    #sample(列表，随机次数)
x=''.join(random.sample(strings,4))
print(x)