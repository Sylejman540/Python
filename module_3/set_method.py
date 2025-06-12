my_set = {1, 2, 3}

#add
my_set.add(7)
print(my_set)

#remove
my_set.remove(7)
print(my_set)

#discard, it deletes a number or anything but if even tho the same exact number u discarded its not in the set it won't give an error
my_set.discard(7)
print(my_set)

#clear
my_set.clear()
print(my_set)

#len
set_length = len(my_set)
print(set_length)

#Examples on how can we use sets
my_list = [1, 2, 2, 3, 4, 5, 5, 5]

unique_set = set(my_list)

unique_list = list(unique_set)

print(unique_list)

user1_interests = {"music", "movies", "travel"}
user2_interests = {"movies", "reading", "cooking"}

common_interests = user1_interests.intersection(user2_interests)

print(common_interests)

#in operator
colors = {"red", "green", "blue"}
color = "red"

print(color in colors)

#not in operator
print(color not in colors)

