# QUESTION 1
print("solution 1")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(min(ages))
print(max(ages))
ages.append(max(ages))
ages.append(min(ages))
print(ages)
ages.sort()
print(ages)
mid = len(ages) // 2
res = (ages[mid] + ages[~mid]) / 2
print("median of the list is :", res)
average = sum(ages) / len(ages)
print("average of the list is :", average)
range = max(ages) - min(ages)
print("range of the list is :", range)