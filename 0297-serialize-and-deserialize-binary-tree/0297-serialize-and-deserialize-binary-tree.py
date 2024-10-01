# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        q=[root]
        serialized=[]
        while q:
            new=[]
            for x in q:
                if x:
                    serialized.append(x.val)
                else:
                    serialized.append(None)
                if x!=None:
                    new.append(x.left)
                    new.append(x.right)
            q=new

        end=len(serialized)-1
        while serialized[end]==None:
            serialized.pop()
            end-=1

        if serialized:
            return ','.join([str(x) for x in serialized])
        else :
            return ''


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        root=TreeNode()
        
        if data=='':
            return None
        
        data=data.split(',')
        for i in range(len(data)):
            if data[i]=='None':
                data[i]='null'
            else:
                data[i]=int(data[i])

        if not data:
            return root
        q=[(0,0,root)]
        while q and data:
            new=[]
            for ndata in q:
                d,p,x=ndata[0],ndata[1],ndata[2]
                if not data:
                    break
                if x==None:
                    x=TreeNode()
                    if d==1:
                        p.left=x
                    else:
                        p.right=x
                x.val=data.pop(0)
                new.append((1,x,x.left))
                new.append((0,x,x.right))
            if data:
                q=new
            else:
                q=[]

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))