# 3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you'd like.
#            Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.


countries=['Switzerland','Germany','Canada','India','Japan']
print(countries)

#append
countries.append('Brazil')
print(countries)

#insert
countries.insert(3,'Egypt')
print(countries)

#delete
del countries[1]
print(countries)

#pop
countries.pop()
print(countries)

#remove
countries.remove('Japan')
print(countries)

#sorted
print(sorted(countries))

#reverse
countries.reverse()
print(countries)

#sort
countries.sort()
print(countries)

#length
print("Length is ",len(countries))

