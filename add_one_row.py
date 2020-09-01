# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        queue = collections.deque([root])
        print(queue)
        level = 1
        while queue:
            size = len(queue)
            # level order traversal
            for i in range(size):
                curr = queue.popleft()
                # insert nodes if we reach 1 level before d
                if level == d-1:
                    old_left, old_right = curr.left, curr.right
                    curr.left, curr.right = TreeNode(v), TreeNode(v)
                    curr.left.left, curr.right.right = old_left, old_right
                else:
                    if curr.left: 
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            # return root once we've appended
            if level == d-1:
                return root
            level += 1
        return None