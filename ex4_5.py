temp = [7.8, 9.1, 10.2, 11.0, 12.5, 12.4, 14.3, 13.8, 12.9, 12.4]
# 1
# temp = []
# hour = 8
# for h in range(10):
#     t = input(f"{hour}時の気温(℃)を入力 >>")
#     temp.append(t)
#     hour += 1

# 2
for data in temp:
    print(data)

# 3
temp_new = []
for h in range(len(temp)):
    if h == 5:
        temp_new.append("N/A")
    else:
        temp_new.append(temp[h])
print(temp)
print(temp_new)

# 4
total = 0
for data in temp_new:
    if isinstance(data,str):
        continue
    total += data
print(f"平均気温：{total / (len(temp_new) - 1):.2f}")