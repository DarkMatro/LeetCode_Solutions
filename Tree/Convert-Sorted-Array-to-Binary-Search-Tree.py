from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(val=nums[0])
        else:
            mid = len(nums) // 2
            left = self.sortedArrayToBST(nums[:mid])
            right = self.sortedArrayToBST(nums[mid + 1:])
            return TreeNode(val=nums[mid], left=left, right=right)
