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

# 230. Kth Smallest Element in a BST
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #dfs traverse and count steps
        #O N and O 1
        if not root: return None
        lst=[]
        def dfs(cur):
            if not cur:
                return 
            dfs(cur.left)
            lst.append(cur.val)
            dfs(cur.right)
            return lst
        lst = dfs(root)
        # print(lst)
        return lst[k-1]


# 105. Construct Binary Tree from Preorder and Inorder Traversal

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #pre order  3 left, right
        # in order  left 3 right

        def helper(preorder, inorder):
            if not preorder or not inorder:
                return
            root=TreeNode(preorder[0])
            mid=inorder.index(preorder[0])
            root.left=helper(preorder[1:mid+1],inorder[:mid])
            root.right=helper(preorder[mid+1:], inorder[mid+1:])
            return root
        root=helper(preorder, inorder)
        return root


# 124. Binary Tree Maximum Path Sum
import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # recursion 
        # tree left max, right max and non root max
        max_path= -math.inf

        def gain_from_subtree(root):

            nonlocal max_path

            if not root: return 0  # tree traversal and max_sum
            gain_from_left=gain_from_subtree(root.left)
            gain_from_right=gain_from_subtree(root.right)
            gain_from_left=max(gain_from_left, 0)
            gain_from_right=max(gain_from_right, 0)

            max_path=max(max_path, gain_from_left +root.val+gain_from_right) #global max_path
            return max(gain_from_left +root.val, gain_from_right +root.val)
        
        max_sum=gain_from_subtree(root)
        return max(max_sum, max_path)
