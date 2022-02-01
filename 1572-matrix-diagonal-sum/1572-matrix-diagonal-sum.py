class Solution:
	def diagonalSum(self, mat: List[List[int]]) -> int:
		n = len(mat)
		mid = n//2
		sum_diag = 0
		for i in range(n):
			sum_diag += mat[i][i]  # Primary Diagonal Sum
			sum_diag += mat[n-i-1][i]  # Secondary Diagonal Sum
		if n & 1:
			sum_diag -= mat[mid][mid]  # Removing repeated center element!
		return sum_diag