dict1 = {"name": "John", "age": 20, "state": "TX"}
dict2 = {"city": "Austin", "country": "USA"}

dict1.update(dict2)

print(dict1)

# join more than 2 dictionaries

d1 = {"name": "Jack", "age": 24}
d2 = {"job_title": "SRE", "location": "Texas"}
d3 = {"company": "Apple"}
d = {**d1, **d2, **d3}

print(d)

# join 2 dicts that have a few common items

d1 = {"Jack": 20, "John": 23}
d2 = {"Jill": 24, "John": 33}

d1.update(d2)

# when both dictionaries have a common key, then the first dict value will be overridden by the second dict value
print(d1)
