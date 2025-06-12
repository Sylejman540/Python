#union
set1 = {1, 2, 3}

set2 = {3, 4, 5}

union_result_method = set1.union(set2)

print(union_result_method)

#intersection
intersection_result_method = set1.intersection(set2)
intersection_result_operator = set1 & set2

print(intersection_result_method)
print(intersection_result_operator)

#difference
difference_result_method = set1.difference(set2)
difference_result_operator = set1 - set2

print(difference_result_operator)
print(difference_result_method)

difference_result_method2 = set2.difference(set1)
difference_result_operator2 = set2.difference(set1)

print(difference_result_operator2)
print(difference_result_method2)

#synmetric method
sd_result_method = set1.symmetric_difference(set2)
sd_result_operator = set1 ^ set2

print(sd_result_method)
print(sd_result_operator)