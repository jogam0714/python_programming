# for문

#for x in iterable객체:
#    ...

for i in range(5):          # 0 ~ 4
    print(i, end = " ")

a = range(5)
print(a.start, a.stop, a.step)

# 1 ~ 5
for i in range(1, 6):
    print(i, end=" ")
print()

# 1 ~ 10
for i in range(1, 10 , 2):
    print(i, end=" ")
print()

# 5, 4, 3, 2, 1 거꾸로
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# 1 ~ 10까지 합
tot = 0
for i in range(1, 11):
    tot += i
else:
    print(f"sum = {tot}")

print(sum(range(1, 11)))

s = "hi10!$한글韓昇和👍"

for c in s:
    print(c, end=" ")

print(len(s))

tot = 0
# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j:<5d}", end=" ")
    print()
else:
    print("End")