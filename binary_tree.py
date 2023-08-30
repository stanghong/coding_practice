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
#bfs
      maxdep=0
      q=deque([root])
      if not root: return 0
      while q:
        qsize=len(q)
        for _ in range(qsize):
          cur=q.popleft()
          if cur.left: q.append(cur.left)
          if cur.right:q.append(cur.right)
        maxdep+=1
      
      return maxdep
# 100. Same Tree
        def helper(p, q):
            if not p and not q: 
                return True
            if not p or not q:
                return False
            if p.val !=q.val:
                return False
            

            leftSame = helper(p.left, q.left)  #recursion returns the T/F from above logic
            rightSame = helper(p.right, q.right)

            return leftSame and rightSame
# 110. Balanced Binary Tree
   def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #note self.balanced and return max(leftDep, rightDep)+1
        self.balanced=True

        def helper(root):
            if not root:
                return 0
           
            leftDep=helper(root.left)
            rightDep=helper(root.right)

            if abs(leftDep-rightDep) >1:
                self.balanced= False
            
            return max(leftDep, rightDep) +1 # bottom up?


        helper(root)
        return self.balanced
