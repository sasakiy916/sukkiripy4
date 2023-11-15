for i in range(1,10):
    if i % 2 == 0:
        continue
    for j in range(1,10):
        result = i * j
        if result > 50:
            continue

        print(f"{result}",end=" ")
    print()