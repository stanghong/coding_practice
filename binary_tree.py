# 226. Invert Binary Tree

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        q=deque([root])
        qsize=len(q)

        # for _ in range(qsize):
        while q:
            cur=q.popleft()
            cur.left, cur.right =cur.right, cur.left
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right)
        
        return root

 #104 max depth
def maxDepth(self, root: Optional[TreeNode]) -> int:
    #dfs
      def dfs(root):
        if not root: 
          return 0
        ldep=dfs(root.left)
        rdep=dfs(root.right)
        return max(ldep, rdep)+1

      return dfs(root)
