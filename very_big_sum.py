# https://www.hackerrank.com/challenges/a-very-big-sum/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def aVeryBigSum2(ar):
	result = 0
	second_line = ar.splitlines()[1]
	int_list = second_line.split(" ", -1) # https://www.w3schools.com/python/ref_string_split.asp
	# print(int_list)
	for i in int_list:
		result += int(i)
	return result

def aVeryBigSum(ar):
	result = 0
	for i in ar[1:]:
		result += i
	return result

a = "5" +"\n1000000001 1000000002 1000000003 1000000004 1000000005"
# print(aVeryBigSum2(a))

b = [5, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
print(aVeryBigSum(b))