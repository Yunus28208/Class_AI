import random

angka_acak = [random.randint(1, 10) for _ in range(20)]

a = angka_acak
x = int(input("Masukkan nilai x yang ingin dicari: ")) 


kemunculan = a.count(x)
indeks_kemunculan = [i for i, nilai in enumerate(a) if nilai == x]

print(a)
print("Kemunculan x:", kemunculan)
print("Indeks kemunculan x:", indeks_kemunculan)

