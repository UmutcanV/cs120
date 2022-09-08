#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    final_size = 1

    if v.left != None:
        final_size += calculate_sizes(v.left)
    
    if v.right != None:
        final_size += calculate_sizes(v.right)# Your code goes here
    
    v.size = final_size
    
    return final_size

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r):
    n = r.size
    def rec_find(r):

        if not r:
            return None

        l = 0 if not r.left else r.left.size
        r = 0 if not r.right else r.right.size

        if l <= n//2 and r <= n//2:
            return r

        l_vert = rec_find(r.left)
        if l_vert:
            return l_vert
        return rec_find(r.right)
    return rec_find(r)


# # def find_vertex(r): 
  
#     n = calculate_sizes(r) / 2

#    def rec_find(vertex): 
        
#         if not vertex:
#             return None
        
#         l = 
#         if r.left is None and r.right is None:
#             return r

#         if r.left.size <= n and r.right.size <= n:


#     return rec_find(r, n)