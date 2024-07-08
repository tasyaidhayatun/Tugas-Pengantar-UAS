# Diberikan variabel-variabel berikut:
p = 11
q = 5
r = 4

#a: ((p - r) == (r + q))
result_a = ((p - r) == (r + q))
print(f"Hasil dari ((p - r) == (r + q)) adalah: {result_a}")

#b: (((p % 3) + q) != (r % 2))
result_b = (((p % 3) + q) != (r % 2))
print(f"Hasil dari (((p % 3) + q) != (r % 2)) adalah: {result_b}")

#c: ((q - 3) == (p % 2 + q))
result_c = ((q - 3) == (p % 2 + q))
print(f"Hasil dari ((q - 3) == (p % 2 + q)) adalah: {result_c}")

#d: ((r + q) != ((p * 2) % 2))
result_d = ((r + q) != ((p * 2) % 2))
print(f"Hasil dari ((r + q) != ((p * 2) % 2)) adalah: {result_d}")

#e: ((((q % 3) + p) > (r % 2)))
result_e = ((((q % 3) + p) > (r % 2)))
print(f"Hasil dari ((((q % 3) + p) > (r % 2))) adalah: {result_e}")

#f (((r + p)) <= (q * 5))
result_f = (((r + p)) <= (q * 5))
print(f"Hasil dari (((r + p)) <= (q * 5)) adalah: {result_f}")