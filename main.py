from binary_expression_tree import BinaryExpressionTree

def driver():
    testers = [
        "5 3 8 * +",        #(5+(3*8)) = 29.0
        ]
    
    print(" ---  Valid Postfix Expression --- ")
    for expression in testers:
        tree = BinaryExpressionTree.postfix(expression)
        print(f"Postfix   : {expression}")
        print(f"Infix     : {tree.infix()}")
        print(f"Result    : {tree.evaluate()}")
        print(f"Preorder  : {list(tree.preorder())}")
        print(f"Postorder : {list(tree.postorder())}")
        print("-" * 40)


if __name__ == "__main__":
    driver()