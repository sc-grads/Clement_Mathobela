#################################
## Data Serialization and Deserialization with Pickle
#################################

import pickle

# Declaring a dictionary
friends = {"Dan": (20, "London", 13242252), "Maria": [25, "Madrid", 34232424]}

# Serializing the dictionary to binary file called `friends.dat`
with open('friends.dat', 'wb') as f:  # b -> binary mode
    pickle.dump(friends, f)

# Deserializing into a Python Object
with open('friends.dat', 'rb') as f:
    obj = pickle.load(f)

    print(type(obj))  # => dict
    print(obj)  # => {'Dan': (20, 'London', 13242252), 'Maria': [25, 'Madrid', 34232424]}