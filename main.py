from binary_expression_tree import BinaryExpressionTree

def driver():
    testers = [
        "5 3 8 * +",        #(5+(3*8)) = 29.0
        "8 2 / 3 -",        #((8/2)-3) = 1.0
        "3 2 /",            #(3/2)= 1.5 
        "0 0 /",            #should give error
        "520 300 + 60 * 12345 37 - /",    #(((520 + 300) * 60) / (12345 - 37) = 3.9974
        ]
    
    print(" ---  Valid Postfix Expression --- ")
    for expression in testers:
        try:
            tree = BinaryExpressionTree.postfix(expression)
            result = tree.evaluate()
            print(f"Postfix   : {expression}")
            print(f"Infix     : {tree.infix()}")
            print(f"Result    : {tree.evaluate()}")
            print(f"Preorder  : {list(tree.preorder())}")
            print(f"Postorder : {list(tree.postorder())}")
            print("-" * 40)
        except (ValueError, ZeroDivisionError) as exc:
            print(f"Error: '{expression}' did not work" )
            print("-" * 40)



if __name__ == "__main__":
    driver()