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
# 572. Subtree of Another Tree

def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#leaf is isSubtree
        self.subcur=subRoot
        cur=root
        def isSameTree(ltree, rtree):
            if not ltree and not rtree:
                return True
            if not ltree or not rtree:
                return False
            if ltree.val != rtree.val: #note 
                return False

            left=isSameTree(ltree.left, rtree.left)
            right=isSameTree(ltree.right, rtree.right)
            return left and right


        # Helper function to traverse main tree and check subtrees
        def helper(cur):
            if not cur :
                return False
            # Check current subtree against subRoot
            if  isSameTree(cur, self.subcur): 
                return True

            # Check left and right children
            left = helper(cur.left)
            right = helper(cur.right)

            return left or right #notice using or logic


        return helper(root)

#102. Binary Tree Level Order Traversal
# BFS
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS
        #popque
        #pushque
        res=[]
        if not root: return []
        q=deque([root])
        while q:
            temp=[]
            qsize=len(q)

            for _ in range(qsize):
                cur=q.popleft()
                temp.append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            res.append(temp)
        return res
# 199. Binary Tree Right Side View
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS
        res=[]
        if not root: return []
        q=deque([root])

        while q:
            qsize=len(q)
            temp=[]
            for _ in range(qsize):
                cur=q.popleft()
                temp.append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            res.append(temp[-1])
        return res

#good node 1448
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maxnum):
            if not root:
                return 0
            good=0
            
            if root.val>=maxnum:
                good=1
            maxnum=max(root.val,maxnum)
            gleft=dfs(root.left, maxnum)
            gright=dfs(root.right, maxnum)
            return good+gleft+gright
        
        
        return dfs(root, -inf)
        #return 1 for  one node
