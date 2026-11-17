from collections import deque
from stack import Stack

class LinkedBinaryTree:
    class _Node:
        def __init__(self, element, parent=None):
            self.element = element
            self.parent = parent
            self.left = None
            self.right = None
 
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node
 
        def element(self):
            return self._node.element
 
    def __init__(self):
        self._root = None
 
    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None
 
    def _validate(self, p):
        if not isinstance(p, self.Position) or p._container is not self:
            raise ValueError("Position does not belong to this tree")
        return p._node

    def is_empty(self):
        return self._root is None
 
    def root(self):
        return self._make_position(self._root)
 
    def parent(self, p):
        return self._make_position(self._validate(p).parent)
 
    def left(self, p):
        return self._make_position(self._validate(p).left)
 
    def right(self, p):
        return self._make_position(self._validate(p).right)
 
    def is_leaf(self, p):
        n = self._validate(p)
        return n.left is None and n.right is None
 
    def add_root(self, element):
        if self._root is not None:
            raise ValueError("Root already exists")
        self._root = self._Node(element)
        return self.root()
 
    def add_left(self, p, element):
        n = self._validate(p)
        if n.left is not None:
            raise ValueError("Left child already exists")
        n.left = self._Node(element, parent=n)
        return self._make_position(n.left)
 
    def add_right(self, p, element):
        n = self._validate(p)
        if n.right is not None:
            raise ValueError("Right child already exists")
        n.right = self._Node(element, parent=n)
        return self._make_position(n.right)

    def attach_subtrees(self, p, left_tree, right_tree):
        """Transfers subtrees to other trees and without duplicating them"""
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("Target position must be a leaf")
        if type(self) is not type(left_tree) or type(self) is not type(right_tree):
            raise TypeError("Subtree must be the same class")
        if left_tree is self or right_tree is self or left_tree is right_tree:
            raise ValueError("Cannot attach a tree to itself")
        if left_tree._root is not None:
            left_tree._root.parent = node
            node.left = left_tree._root
            left_tree._root = None
        if right_tree._root is not None:
            right_tree._root.parent = node
            node.right = right_tree._root
            right_tree._root = None

    def preorder(self):
        def visit(p):
            if p is not None:
                yield p.element()
                yield from visit(self.left(p))
                yield from visit(self.right(p))
        yield from visit(self.root())
 
    def inorder(self):
        def visit(p):
            if p is not None:
                yield from visit(self.left(p))
                yield p.element()
                yield from visit(self.right(p))
        yield from visit(self.root())
 
    def postorder(self):
        def visit(p):
            if p is not None:
                yield from visit(self.left(p))
                yield from visit(self.right(p))
                yield p.element()
        yield from visit(self.root())
 
    def level_order(self):
        q = deque([self.root()]) if self.root() is not None else deque()
        while q:
            p = q.popleft()
            yield p.element()
            for child in (self.left(p), self.right(p)):
                if child is not None:
                    q.append(child)


class BinaryExpressionTree(LinkedBinaryTree):
    Operators = {"+","-","*","/"}

     @staticmethod
    def _is_number(token):
        if token.lower() in {"nan", "inf", "+inf", "-inf", "infinity", "+infinity", "-infinity"}:
            return False
        try:
            float(token)
            return True
        except ValueError:
            return False
    
    @classmethod
    def postfix(cls,expression):
        if not isinstance(expression, str) or not expression.strip():
            raise ValueError(Postfix cannot be enpty)
        tokens = expression.split()
        stack = Stack()
        for token in tokens:
            if cls._is_number(token):
                math_tree = cls()
                math_tree.add_root(token)
                stack.push(math_tree)
            elif token in cls.Operators:
                if len(stack) < 2:
                    raise ValueError(f"Bad Postfix, insufficient operands for '{token}'")
                left_subtree = stack.pop()
                right_subtree = stack.pop()
                oper_tree = cls()
                oper_root = oper_tree.add_root(token)
                op_tree.attach_subtrees(oper_root, left_subtree, right_subtree)
                stack.push(oper_tree)
            else:
                raise ValueError(f"Bad token in postfix: '{token}'")
        if len(stack) != 1:
            raise ValueError("Bad Postfix: too many operands left")
        return stack.pop()

    def evaluate(self):
        if self.is_empty():
            raise ValueError("Can't evaluate an empty tree")

        def judge(p)
            if self.is_leaf(p):
                return float(p.element())
            left_val = _judge(self.left(p))
            right_val = _judge(self.right(p))
            op = p.element()

            if op == "+":
                return left_val + right_val
            if op == "-":
                return left_val - right_val
            if op == "*":
                return left_val * right_val
            if op == "/":
                return left_val / right_val

        return _judge(self.root())

    def infix(self):
        if self.is_empty():
            raise ValueError("Cannot format an empty tree")

        def _format(p):
            if self.is_leaf(p):
                return str(p.element())
            left_str = _format(self.left(p))
            right_str = )format(self.right(p))
            return f"({left_str} {p.element()} {right_str})"

        return _format(self.root())

    def __str__(self):
        return self.infix() if not self.is_empty() else ""
