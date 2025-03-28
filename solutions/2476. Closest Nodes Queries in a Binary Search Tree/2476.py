class Solution:
  def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
    sortedVals = []
    self._inorder(root, sortedVals)

    def getClosestPair(q: int) -> List[int]:
      i = bisect_left(sortedVals, q)
      # q is presented in the tree, so just use [q, q].
      if i != len(sortedVals) and sortedVals[i] == q:
        return [q, q]
      # q isn't presented in the tree, so find the cloest one is possible.
      return [-1 if i == 0 else sortedVals[i - 1],
              -1 if i == len(sortedVals) else sortedVals[i]]

    return [getClosestPair(q) for q in queries]

  # Inorder walk the BST to collect sorted numbers.
  def _inorder(self, root: Optional[TreeNode], sortedVals: List[int]) -> None:
    if root == None:
      return
    self._inorder(root.left, sortedVals)
    sortedVals.append(root.val)
    self._inorder(root.right, sortedVals)
