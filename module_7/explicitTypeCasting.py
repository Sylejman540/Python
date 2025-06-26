#Example 1
age = 25

age_as_str = bool(age)

print(age_as_str, "of type", type(age_as_str))

#Example 2
print(bool(0))  #Output: False
print(bool(42)) #Output: True

print(bool("")) #Output: False
print(bool("Hello World")) #Output: True

print(bool([])) #Output: False
print(bool(None)) #Output: False