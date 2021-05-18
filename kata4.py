lst = [-7,10]
resultado = []
for num in lst:
    for i in range(2, abs(num)+1):
        if num%i == 0 and i%2 != 0 and all(i%x != 0 for x in resultado) and i not in resultado:
            resultado.append(i)
        elif i == 2 and num%i == 0 and 2 not in resultado:
            resultado.append(i)


toma = []
for r in resultado:
    z = 0
    for y in lst:
        if y%r == 0:
            z += y
    toma.append([r,z])

print(sorted(toma))    

 
 