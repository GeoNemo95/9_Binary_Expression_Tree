import unittest
from binary_expression_tree import BinaryExpressionTree

class TestBinaryExpressionTree(unittest.TestCase):

    def test_addition(self):
        expression = "2 3 +"
        tree = BinaryExpressionTree.postfix(expression)
        self.assertEqual(tree.infix(), "(2 + 3)")
        self.assertEqual(" ".join(tree.postorder()), expression)
        self.assertAlmostEqual(tree.evaluate(), 5.0)

    def test_nested_operators(self):
        expression = "2 3 4 * - 5 /"
        tree = BinaryExpressionTree.postfix(expression)
        self.assertEqual(tree.infix(), "((2 - (3 * 4)) / 5)")
        self.assertEqual(list(tree.postorder()), expression.split())
        self.assertAlmostEqual(tree.evaluate(), -2.0)

    def test_noncommutative_operand_order(self):
        expression = "2 3 - 4 /"
        tree = BinaryExpressionTree.postfix(expression)
        self.assertEqual(tree.infix(), "((2 - 3) / 4)")
        self.assertEqual(list(tree.postorder()), expression.split())
        self.assertAlmostEqual(tree.evaluate(), -0.25)

    def test_decimal_operand(self):
        expression = "-2.3 4.5 +"
        tree = BinaryExpressionTree.postfix(expression)
        self.assertEqual(tree.infix(), "(-2.3 + 4.5)")
        self.assertEqual(list(tree.postorder()), expression.split())
        self.assertAlmostEqual(tree.evaluate(), 2.2)

    def test_bad_postfix_input(self):
        with self.assertRaises(ValueError):
            BinaryExpressionTree.postfix("2 3 4 -")

        with self.assertRaises(ValueError):
            BinaryExpressionTree.postfix("2 +")

    def test_divide_by_zero(self):
        tree = BinaryExpressionTree.postfix("2 0 /")
        with self.assertRaises(ZeroDivisionError):
            tree.evaluate()


if __name__ == "__main__":
    unittest.main()