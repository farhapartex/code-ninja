class NewNode:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data

def insert(temp, key):
    q=[]
    q.append(temp)

    while len(q):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = NewNode(key)
            break
        else:
            q.append(temp.left)
        

        if not temp.right:
            temp.right = NewNode(key)
            break
        else:
            q.append(temp.right)


def inorder(temp):

    if temp is None:
        return
    
    inorder(temp.left)
    print(temp.val,end=" ")
    inorder(temp.right)


if __name__ == '__main__':
    root = NewNode(10)
    root.left = NewNode(11)
    root.left.left = NewNode(12)
    root.right = NewNode(13)
    root.right.left = NewNode(14)
    root.right.right = NewNode(15)

    inorder(root)
    print("")

    key=20

    insert(root, key)

    inorder(root)
    print('')