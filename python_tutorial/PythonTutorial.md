Main features:
* Readable
* Garbage collected
* Dynamically Typed

# Start the python interpreter
python

# Print
print("Hello, World!")

# Print c/ concatenação
print("Hello, " + "André" + " Ferreira!")

# Creating lists
a = ["orange", "apple", "banana"]
b = []
c = ["orange", "pear", [1, 2, 3, 4]]
print(a)
print a[2]
print b[1]
print c[2]

# Slice lists
a = [0, 1, 2, 3, 4, 5]
a[0:3]
a[2:3]
a[2:]
a[:6]
a[:]

# Inclusion
a = ['apple', 'pear', 'orange']
'pear' in a
'grape' in a

if 'pear' in a:
    print "Tem pêra"

if 'grape' in a:
    print "Tem uva"

# Dictionaries
g = {'name':'André Ferreira', 'city_of_birth':'Queens'}
colors = {'sky':'blue', 'sea':'blue', 'earth':'brown'}
g
g['name']
g['name'] = "Paulo Roberto"

# Exibe todas as chaves de um dict
g.keys()

# Deleta uam chave / valor de um dict
del(g['name'])

# Verifica se existe uma chave no dict
'city_of_birth' in g

# Lists and Collections together
a = {'name': 'Andre Ferreira', 'interests': ['cycling', 'running', 'golf']}
a['interests'][1]
a['interests'].append['swimming']
things = {'animals':['dog','cat','zebra']}

---
# Loops with Lists
fruit = ['apple', 'orange', 'grape']

new_fruit = []

for item in fruit:
    print item

    new_fruit.append(item)

print new_fruit
---

---
# Loops with Dictionaries
person = {'name':"Andre Ferreira", 'favorite_color':'blue', 'hair':'brown'}

for key in person:
    print "key is " + key + " value is " + person[key]
---
