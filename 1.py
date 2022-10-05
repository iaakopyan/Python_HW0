a = str(input())
b = []
slovo = ""
for elem in a:
    if elem.isalpha():  #
        slovo += elem
    if len(slovo) > 2 and (not elem.isalpha() or a.index(elem) == len(a) - 1):
        for bukva in range(len(slovo) - 2):
            b.append(slovo[bukva:3 + bukva:1])
        slovo = ""
    elif len(slovo) < 3 and not elem.isalpha():
        slovo = ""
for i in b:
    print(i, sep="\n")
