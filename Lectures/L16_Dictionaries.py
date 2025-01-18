# dictionaries = a changeable, ordered collection of unique keys: value pairs
# faster as they use hashing, allow us to access  a value quickly

bird = {
    "Name": "Alex",
    "Age": 2,
    "Sex": "Female"
}
print(bird["Name"])  # if this key is not available in dictionary it will throw an error
print(bird.get("Age"))  # if key not available it will return None
print(bird.get('adult', True))  # can provide an alternative answer
bird["Adult"] = True   # Adding a new key value

bird.update({'Breed': 'Ringneck'})         # adds new key and assigns value to it
bird.update({'Breed': 'Alexandrine'})      # updates existing value of any key

print(bird.values())                       # prints all the values
print(bird.keys())                         # prints all the keys in dictionary
print(bird.items())                        # prints the entire dictionary

bird.pop('Sex')                            # removes key and its assigned value

for key, value in bird.items():
    print(key, value)

bird.clear()                               # deletes everything in the dictionary
