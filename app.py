#%%
# 获取用户输入
input_str = input("请输入数字（用空格分隔）: ")

# 转换输入为数字列表
try:
    numbers = [float(num) for num in input_str.split()]
    numbers.sort()
    print("排序结果:", numbers)
except ValueError:
    print("错误：请确保输入的都是数字！")

import numpy as np
#%%

#%%
msg = "Roll a dicel" 
print(msg) 

print(np.random.randint(1,9))

#%%
# for循环
for n in range(1,10):
    print("2 to the %d power is %d" % (n,2**n))

a = "Hello World"
for c in a:
    print(c)
b = ["Dave", "Mark", "Ann", "Phil"]
for name in b:
    print(name)

c = {'GOOG' : 490.10, 'IBM' : 91.50, 'AAPL' : 123.15}
for key in c:
    print(key, c[key])

#%%
# def函数
def remainder(a, b):
    q = a // b
    r = a - q * b
    return r