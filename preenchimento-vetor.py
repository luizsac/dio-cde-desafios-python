n = 10*[0]
val = int(input())
for i in range(len(n)):
    n[i] = val
    val *= 2
    print(f"N[{i}] = {n[i]}")
