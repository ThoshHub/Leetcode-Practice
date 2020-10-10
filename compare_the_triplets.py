# https://www.hackerrank.com/challenges/compare-the-triplets/problem?h_r=next-challenge&h_v=zen

def compareTriplets(a, b):
	alice_points = 0
	bob_points = 0
	for i in range(3):
		if a[i] > b [i]:
			alice_points += 1
		elif a[i] < b [i]:
			bob_points += 1
	return [alice_points, bob_points]

a = [1, 2, 3]
b = [3, 4, 5]
result = compareTriplets(a, b)
print(result)