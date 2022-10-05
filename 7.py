# Даны два ящика размерами A1 × B1 × C1 и A2 × B2 × C2.
# Можно ли разместить одну коробку внутри другой, имея параллельные стороны коробок?
A1 = int(input())
B1 = int(input())
C1 = int(input())

A2 = int(input())
B2 = int(input())
C2 = int(input())

if ((A1 == A2 and B1 == B2 and C1 == C2) or (A1 == A2 and B1 == C2 and C1 == B2) or
        (A1 == C2 and B1 == A2 and C1 == B2) or (A1 == B2 and B1 == A2 and C1 == C2) or
        (A1 == B2 and B1 == C2 and C1 == A2) or (A1 == C2 and B1 == B2 and C1 == A2)):
    print('Ящики равны')
elif ((A1 <= A2 and B1 <= B2 and C1 <= C2) or (A1 <= A2 and B1 <= C2 and C1 <= B2) or
      (A1 <= C2 and B1 <= A2 and C1 <= B2) or (A1 <= B2 and B1 <= A2 and C1 <= C2) or
      (A1 <= B2 and B1 <= C2 and C1 <= A2) or (A1 <= C2 and B1 <= B2 and C1 <= A2)):
    print('Первое поле меньше второго')
elif ((A1 >= A2 and B1 >= B2 and C1 >= C2) or (A1 >= A2 and B1 >= C2 and C1 >= B2) or
      (A1 >= C2 and B1 >= A2 and C1 >= B2) or (A1 >= B2 and B1 >= A2 and C1 >= C2) or
      (A1 >= B2 and B1 >= C2 and C1 >= A2) or (A1 >= C2 and B1 >= B2 and C1 >= A2)):
    print('Первое поле больше второго')
else:
    print('Ящики несопоставимы')
