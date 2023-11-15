# temp = [7.8, 9.1, 10.2, 11.0, 12.5, 12.4, 14.3, 13.8, 12.9, 12.4]
# 1
temp = {}
hour = 8
for key in range(10):
    t = float(input(f"{hour}時の気温(℃)を入力 >>"))
    temp[hour] = t
    hour += 1

# 2
for data in temp.values():
    print(data,end=", ")
print()

# 3
temp_new = {}
for key in temp:
    if key == 13:
        temp_new[key] = "N/A"
    else:
        temp_new[key] = temp[key]
print(temp)
print(temp_new)
print()

# 4
total = 0
for data in temp_new.values():
    if isinstance(data,str):
        continue
    total += data
print(f"平均気温：{total / (len(temp_new) - 1):.2f}")