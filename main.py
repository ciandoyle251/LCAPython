class newNode():
 
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None
         
""" Inorder traversal of a binary tree"""
def inorder(temp):
 
    if (not temp):
        return
 
    inorder(temp.left)
    print(temp.key,end = " ")
    inorder(temp.right)
 
 
"""function to insert element in binary tree """
def insert(temp,key):
 
    if not temp:
        root = newNode(key)
        return
    q = []
    q.append(temp)
 
    # Do level order traversal until we find
    # an empty place.
    while (len(q)):
        temp = q[0]
        q.pop(0)
 
        if (not temp.left):
            temp.left = newNode(key)
            break
        else:
            q.append(temp.left)
 
        if (not temp.right):
            temp.right = newNode(key)
            break
        else:
            q.append(temp.right)



def findPath( root, path, k):
 
    # Baes Case
    if root is None:
        return False
 
    # Store this node is path vector. The node will be
    # removed if not in path from root to k
    path.append(root.key)
 
    # See if the k is same as root's key
    if root.key == k :
        return True
 
    # Check if k is found in left or right sub-tree
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))):
        return True
 
    # If not present in subtree rooted with root, remove
    # root from path and return False
      
    path.pop()
    return False
 
# Returns LCA if node n1 , n2 are present in the given
# binary tre otherwise return -1
def findLCA(root, n1, n2):
 
    # To store paths to n1 and n2 fromthe root
    path1 = []
    path2 = []
 
    # Find paths from root to n1 and root to n2.
    # If either n1 or n2 is not present , return -1
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1
 
    # Compare the paths to get the first different value
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]
     
# Driver code
if __name__ == '__main__':
    root = newNode(1)
    ##root = newNode(10)
    # print("Inorder traversal before insertion:", end = " ")
    # inorder(root)
 
    key = 12
    insert(root, key)



 
    print(findLCA(root, 12, 1))
    # print("Inorder traversal after insertion:", end = " ")
    # inorder(root)