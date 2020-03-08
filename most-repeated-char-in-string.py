# Find the most repeated character in a string


# Approach 1 - using max()

sentence = "Python is cool."

char_frequency = {}

for char in sentence:
    char_frequency[char] = 1 if char not in char_frequency else char_frequency[char] + 1

# max() returns the item with the highest value or, in this case, the item with the highest value in an iterable
# The key refers to the single argument function to customize the sort order, applied to each item on the iterable
max_key = max(char_frequency, key=char_frequency.get)

print({max_key: char_frequency.get(max_key)})  # prints {'o': 3}


# Approach 2 - using sorted()

sentence = "Python is cool."

char_frequency = {}

for char in sentence:
    char_frequency[char] = 1 if char not in char_frequency else char_frequency[char] + 1

# sorted() takes an iterable and sorts it
# sorted(char_frequency.items()) returns all the key value pairs of the char_frequency dictionary as tuples
# the key=lambda function as a second argument instructs which values to sort based on
# kv refers to the key:value pair
# kv[1] refers to the value of the kv pair, which is the frequency of each character used for sorting
char_frequency_sorted = sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True)

print(char_frequency_sorted[0])  # prints ('o', 3)
