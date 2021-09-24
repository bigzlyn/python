# 循环
# 用户输入字符
c = input("请输入一个字符: ")

# 用户输入ASCII码，并将输入的数字转为整型
a = int(input("请输入一个ASCII码: "))

print(c + " 的ASCII 码为", ord(c))
print(a, " 对应的字符为", chr(a))

len = int(input("请输入循环次数: "))

for i in range(len):
    print(i)
else:
    print("else")

while i < len:
    print(i)
    i += 1
    if i == 4:
        print(i, "+++")
        print(i, "---")
else:
    print("")

i = 0
name = "biyn%s" % i
print(name)


def sum1(a, b) -> int:
    a = a + 3
    b = b + 3
    print("求和")
    return a + b


print(sum1(1, 2))


def loop1():
    for i in range(10):
        print("hello world%s" % i)
    # return


def loop2():
    i = 0
    while i < 10:
        print("hello world%s" % i)
        i += 1


loop2()