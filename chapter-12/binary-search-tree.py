class Node:
    def __init__(self, parent, key, left, right):
        self.parent = parent
        self.left = left
        self.key = key
        self.right = right

def tree_insert(tree, new_node):
    if not tree:
        return new_node
    cur_node = tree
    while True:
        if cur_node.key > new_node.key:
            if cur_node.left == None:
                cur_node.left = new_node
                new_node.parent = cur_node
                break
            cur_node = cur_node.left
        else:
            if cur_node.right == None:
                cur_node.right = new_node
                new_node.parent = cur_node
                break
            cur_node = cur_node.right
    return tree

def key_with_level(node, level, nodes):
    if node:
        if len(nodes) > level:
            nodes[level].append(node.key)
        else:
            nodes.append([node.key])
        if node.left:
            key_with_level(node.left, level+1, nodes)
        if node.right:
            key_with_level(node.right, level+1, nodes)

def print_tree(tree):
    nodes = []
    key_with_level(tree, 0, nodes);
    for node in nodes:
        print node

def main():
    tree = tree_insert(None, Node(None, 13, None, None))
    tree_insert(tree, Node(None, 15, None, None))
    tree_insert(tree, Node(None, 11, None, None))
    tree_insert(tree, Node(None, 10, None, None))
    tree_insert(tree, Node(None, 19, None, None))
    tree_insert(tree, Node(None, 12, None, None))
    print_tree(tree)

main()
