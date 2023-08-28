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
