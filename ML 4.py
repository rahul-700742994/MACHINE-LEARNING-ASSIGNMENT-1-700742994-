print("solution 4")
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("length of the it_companies is : ", len(it_companies))
it_companies.add('Twitter')  # adding twitter
print(it_companies)
it_companies.update(['fisher','ford','verizon'])
print(it_companies)
it_companies.remove('Facebook')  # removing facebook from it_companies
print(it_companies)
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B)  # joining A and B
print(C)
D = A.intersection(B)
print("A intersection B is:", D)
E = A.issubset(B)
print("is A subset of B:", E)
F = A.isdisjoint(B)
print("are A and B disjoint sets:", F)
G = A.update(B)  # joining A with B
H = B.update(A)  # joining B with A
print("joining A with B :", G)
print("joining B with A:", H)
I = A.symmetric_difference(B)
print("symmetric difference between A and B is:", I)
del A  # deleting set A
del B  # deleting set B
ages = [22, 19, 24, 25, 26, 24, 25, 24]
set1 = set(ages)  # converting list as set
print(set1)
print(len(ages))
print(len(set1))
diff = len(ages) - len(set1)
print("the difference between length of list and sets is: ", diff)
# the difference between remove and discard is :If the item to remove does not exist in the set, remove() will raise an error,discard() will not raise an error.
