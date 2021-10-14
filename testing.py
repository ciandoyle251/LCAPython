# import unittest

# from main import findLCA, inorder, insert, newNode
# root = newNode(1)
# for i in range(2,21):
#     insert(root, i)

# inorder(root)

            #                       1
            #               /               \                              
            #           2                       3
            #       /       \               /       \
            #      4         5             6         7
            #     / \       / \           / \       / \
            #    8   9     10  11        12  13    14  15
            #   /\   /\    /\  /\        /\  /\    /\  /\
            # 16 17 18 19  20 


from logging import root
import unittest

from main import findLCA, inorder, insert, newNode


class testBinTree(unittest.TestCase):
    root = newNode(1)
    for i in range(2,21):
        insert(root, i)



    test1 = 2


    def test_inputs(self):

        print("run")
        self.assertEquals(2, findLCA(self.root, 19, 20))#trivial test
        self.assertEqual(1, findLCA(self.root, 16, 15))#more complicated test
        self.assertEqual(4, findLCA(self.root, 16, 4))#seperate leveled solutions
        self.assertEqual(9, findLCA(self.root, 9, 9))#duplicate inputs