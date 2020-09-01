def __init__(self):
	self.tilt = 0

def findTilt(self, root: TreeNode) -> int:
	# null node equals to node whose value is 0
	self.calc(root)
	return self.tilt

def calc(self, root):
	if not root:
		return 0

	l = r = 0
	if root.left:
		l = self.calc(root.left)
	if root.right:
		r = self.calc(root.right)

	self.tilt += abs(l-r)
	return l + r + root.val

"""Input: 
         1
       /   \
      2     3
Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1"""