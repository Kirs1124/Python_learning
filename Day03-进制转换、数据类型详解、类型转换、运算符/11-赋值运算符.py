#  = 等号在计算机编程里，我们称之为赋值运算符，和数学里的等号有一定的区别

# 数学
# 1 + 1 = 2
# 4 = 4

# 计算机编程里，等号(赋值运算符)作用是将等号右边的值赋值给等号的左边
# 等号的左边一定不能是常量或者表达式
a = 4

# 10 = x
# 3 + 3 = m
m = 3 + 3

x = 1
# x = x + 2
# 复合赋值运算符
x += 2
print(x)  # 3

x -= 1
print(x)  # 2

x *= 3
print(x)  # 6

x /= 2
print(x)  # 3.0

x **= 5
print(x)  # 243.0

x //= 2
print(x)  # 121.0

x %= 2  # x = x % 2
print(x)  # 1.0
