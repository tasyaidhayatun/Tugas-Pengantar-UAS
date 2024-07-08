# Soal 1
result = "Honey" + "Boo" * 3
print(result)

#Outputnya adalah: 'HoneyBooBooBoo'

# Soal 2
capitals = {}
capitals['Murica'] = 'Warshington'
capitals['Germany'] = 'Bonn'
capitals['France'] = 'Paris'
capitals['Engalnd'] = 'London'
capitals['Germany'] = 'Berlin'

result = capitals['Germany']
print(result)

#Outputnya adalah: 'Berlin'

# Soal 3
a = "23"
b = 9
print(a + b)

#Output dari kode ini menghasilkan TypeError: can only concatenate str (not "int") to str 

# Soal 4
letters = ["a", "b", "o", "c", "p"]

#a. >>>letters[1]
result_a = letters[1]
print(result_a)

#b. >>>letters[len(letters)-2]
result_b = letters[len(letters)-2]
print(result_b)

#c. >>>letters + ["x"]
result_c = letters + ["x"]
print(result_c)

#d. >>>letters
result_d = letters
print(result_d)

#Output:
#a. 'b'
#b. 'c'
#c. ['a', 'b', 'o', 'c', 'p', 'x']
#d. ['a', 'b', 'o', 'c', 'p']

# Soal 5
result = ' '.join('h a n d s'.split())
print(result)

#Outputnya adalah: 'h a n d s'

# Soal 6
import json

json_string = """
[
    {"1": "one", "2": "two", "3": "three"},
    {"1": "un", "2": "deux", "3": "trois"},
    {"1": "eins", "2": "zwei", "3": "drei"}
]
"""

result = json.loads(json_string)[1]["2"]
print(result)

#Outputnya adalah: 'deux'

# Soal 7
def pembagi_indeks1(nums, divisor):
    for i in range(len(nums)):
        if nums[i] % divisor == 0:
            return i
    return -1

vals = [100, 66, 55, 64, 41, 35, 18, 64]
result = pembagi_indeks1(vals, 5)
print(result)  

#Outpunya adalah: 0

#Soal 8
def mystery(n, m):
    p = 0
    e = 0
    while e < n:
        p += 1
        e += 1
    return p

print(mystery(4, 3)) # Outputnya adalah 4

#Pelacakan nilai p dan e dari setiap iterasi:
#Iterasi 1: p = 1, e = 1
#Iterasi 2: p = 2, e = 2
#Iterasi 3: p = 3, e = 3
#Iterasi 4: p = 4, e = 4
#Nilai Akhir: p = 4, e = 4 
