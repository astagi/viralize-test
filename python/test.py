import tree
import unittest

class TestTree(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_has_not_cycles(self):
        c = tree.Node(3)
        d = tree.Node(4, c)
        e = tree.Node(5, c)
        t = tree.Node(6, e, d)
        self.assertFalse(tree.has_cycles(t))

        c = tree.Node(3)
        d = tree.Node(4, c)
        e = tree.Node(5, c)
        t = tree.Node(6, e, d)
        self.assertFalse(tree.has_cycles(t))

    def test_has_cycles(self):
        c = tree.Node(3)
        d = tree.Node(4, c)
        e = tree.Node(5, c)
        t = tree.Node(6, e, d)
        c.right = t
        self.assertTrue(tree.has_cycles(t))

        c = tree.Node(3)
        d = tree.Node(4, c)
        e = tree.Node(2, c, d)
        t = tree.Node(1, e)
        d.right = t
        self.assertTrue(tree.has_cycles(t))

        c = tree.Node(4)
        d = tree.Node(3, d)
        e = tree.Node(2, c)
        t = tree.Node(1, e)
        c.right = d
        self.assertTrue(tree.has_cycles(t))

        c = tree.Node(3)
        d = tree.Node(4, c)
        e = tree.Node(2, c, d)
        t = tree.Node(1, e)
        d.right = e
        self.assertTrue(tree.has_cycles(t))

    def test_visit(self):
        visit_expected = [6, 5, 4, 3, 1, 2]
        a = tree.Node(1)
        b = tree.Node(2)
        c = tree.Node(3, a, b)
        d = tree.Node(4, c)
        e = tree.Node(5)
        t = tree.Node(6, e, d)
        for expected, node in zip(visit_expected, tree.visit(t)):
            self.assertEqual(expected, node.data)
