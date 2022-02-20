class MagicList :
	def __init__(self):
		self.data = [0]
	
	def findMin(self):
		M = self.data
		''' you need to find and return the smallest
			element in MagicList M.
			Write your code after this comment.
		'''

		if len(M)==1:
			return None
		else:
			return M[1]
	
	def insert(self, E):
		M = self.data
		''' you need to insert E in MagicList M, so that
			properties of the MagicList are satisfied. 
			Return M after inserting E into M.
			Write your code after this comment.
		'''
		M.append(E)
		i=len(M)-1
		while i>1:
			if M[i//2]<E:
				return M
				break
			else:
				M[i],M[i//2]=M[i//2],M[i]
				i=i//2
		else:
			return M

	def deleteMin(self):
		M = self.data
		''' you need to delete the minimum element in
			MagicList M, so that properties of the MagicList
			are satisfied. Return M after deleting the 
			minimum element.
			Write your code after this comment.
		'''
		j=M.index(min(M[1:]))
		M[j],M[-1]=M[-1],M[j]
		M.pop()
		while j<len(M)-1:
			if 2*j<=len(M)-1 and M[j]>M[2*j]:
				M[j],M[2*j]=M[2*j],M[j]
				j=2*j
			elif 2*j+1<=len(M)-1 and M[j]>M[2*j+1]:
				M[j],M[2*j+1]=M[2*j+1],M[j]
				j=2*j+1
			else:
				break
		return M

	
def K_sum(L, K):
	''' you need to find the sum of smallest K elements
		of L using a MagicList. Return the sum.
		Write your code after this comment.
	'''
	M=MagicList()
	for i in L:
		M.insert(i)
	sum=0
	for i in range (K):
		sum+=min(M.data[1:])
		M.deleteMin()
	return sum
	
if __name__ == "__main__" :
	'''Here are a few test cases'''
	
	'''insert and findMin'''
	M = MagicList()
	M.insert(4)
	M.insert(3)
	M.insert(5)
	x = M.findMin()
	if x == 3 :
		print("testcase 1 : Passed")
	else :
		print("testcase 1 : Failed")
		
	'''deleteMin and findMin'''
	M.deleteMin()
	x = M.findMin()
	if x == 4 :
		print("testcase 2 : Passed")
	else :
		print("testcase 2 : Failed")
		
	'''k-sum'''
	L = [2,5,8,3,6,1,0,9,4]
	K = 4
	x = K_sum(L,K)
	if x == 6 :
		print("testcase 3 : Passed")
	else :
		print("testcase 3 : Failed")


	M = MagicList()
	M.insert(-4)
	M.insert(43)
	M.insert(23)
	M.insert(23)
	M.insert(45)
	M.insert(54)
	M.insert(43)
	M.insert(-34)
	M.insert(-45)
	M.insert(-23)
	M.insert(-23)
	M.insert(43)
	M.insert(67)
	M.insert(4)
	M.insert(7)
	M.insert(5)
	M.insert(2)
	M.insert(0)
	M.insert(76)
	M.insert(90)
	x = M.findMin()
	if x == -45 :
		print("testcase_findmin : Passed")
	else :
		print("testcase_findmin : Failed")

	M.deleteMin()
	x = M.findMin()
	if x == -34 :
		print("testcase_deletemin : Passed")
	else :
		print("testcase_deletemin : Failed")

	L = [2,5,8,3,6,1,0,9,4,32,34,54,5,6,5,7,664,53,2,3,34,54,56,5,2,3,23,23,45,65,76]
	K = 6
	x = K_sum(L,K)
	if x == 10 :
		print("testcase_k_sum : Passed")
	else :
		print("testcase_k_sum : Failed")