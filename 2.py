#Создать программу, которая выбирает из текста все даты,
#которые записаны в формате: dd.mm.yyyy и сохранить их в формате datetime
from datetime import datetime
import re
text = str(input())
match = re.findall('(?:[0-2][1-9]|[3][0-1]|[1-2][0]).(?:[1][0-2]|[0][1-9]).[1-2][0-9]{3}', text)
for i in range(0,len(match)):
    print(datetime.strptime(str(match[i]), "%d.%m.%Y").date())

