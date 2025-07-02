 
        for i in range(len(pre) - 1):
            pre[i].left = None
            pre[i].right = pre[i + 1]
        
        # Last node should point to None
        pre[-1].left = None
        pre[-1].right = None
