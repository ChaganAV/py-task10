import random

def FindMin(list_monet):
    count = 0
    for m in monets:
        if m>0:
            count+=1
    if (count_monets-count)>count:
        min = count
    else:
        min = count_monets-count
    return min

# через random определим количество монет
count_monets = random.randint(1,10)
monets = []
count = 0
min = 0

# заполним список орлом или решкой
while count < count_monets:
    monets.append(random.randint(0,1))
    count+=1

min = FindMin(monets)

print(f"{count_monets} -> {monets}")
if min == 0:
    print("Ничего переворачивать не нужно!")
else:
    print(min)