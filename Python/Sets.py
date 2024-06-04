cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)           #The union() method returns a new set
print(cities3)

cities.update(cities2)       #update() method adds item into the existing set from another set.
print(cities)

cities3 = cities.intersection(cities2)
print(cities3)

cities.intersection_update(cities2)
print(cities)

cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities.symmetric_difference_update(cities2)
print(cities)

cities3 = cities.difference(cities2)
print(cities3)

