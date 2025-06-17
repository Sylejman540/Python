count = 1

while count <= 5:
    print("Iteration: ", count)
    count += 1

print(count)

#break
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
target = 4

for number in numbers:
    print(number)
    if number == target:
        print("Target found!")
        break

scores = [27, 28, 29, 51, 56, 93, 54]

for score in scores:
    print("Score:", score)
    if score >= 50:
        print("Score above 50:", score)
