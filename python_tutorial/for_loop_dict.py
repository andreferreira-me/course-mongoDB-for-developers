person = {'name':"Andre Ferreira", 'favorite_color':'blue', 'hair':'brown'}

for key in person:
    print "key is " + key + " value is " + person[key]

# Another example
people = {'name': 'Bob', 'hometown': "Palo Alto", 'favorite_color': 'red'}

for item in people:
    if (item == 'favorite_color'):
        print people[item]
