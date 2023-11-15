# 1
numbers = [1, 1]
while True:
    next = numbers[-1] + numbers[-2]
    if next > 1000:
        break
    numbers.append(next)
print(numbers)

# 2
ratios = []
for num in range(len(numbers)):
    if num+1 >= len(numbers):
        break
    ratios.append(numbers[num+1] / numbers[num])
print(ratios)

#3
for n in range(len(ratios)):
    ratios[n] = int(ratios[n] * 1000) / 1000
print(ratios)