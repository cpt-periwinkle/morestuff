# Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and bound strategy

def knapSack(W, wt, val, n):
	K = [[0 for x in range(W + 1)] for x in range(n + 1)]
	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif wt[i-1] <= w:
				K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
			else:
				K[i][w] = K[i-1][w]
	return K[n][W]


n = int(input("Enter number of values: "))
val = []
wt = []
for i in range(n):
	val.append(int(input("Enter value of weight: ")))
	wt.append(int(input("Enter weight: ")))
W = int(input("Enter maximum weight: "))
print("Maximum total value : ", knapSack(W, wt, val, n))