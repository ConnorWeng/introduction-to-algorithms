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

def key_with_level(node, level, nodes_all_level):
    if node:
        if len(nodes_all_level) > level:
            nodes_all_level[level].append(node)
        else:
            nodes_all_level.append([node])
        if node.left:
            key_with_level(node.left, level+1, nodes_all_level)
        if node.right:
            key_with_level(node.right, level+1, nodes_all_level)

def print_tree(tree):
    nodes_all_level = []
    key_with_level(tree, 0, nodes_all_level);
    for nodes in nodes_all_level:
        line = '('
        last_parent = None
        for node in nodes:
            if node.parent != last_parent and line != '(':
                line += ') ('
            line += '%d ' % node.key
            last_parent = node.parent
        line += ')'
        print line

def main():
    tree = tree_insert(None, Node(None, 13, None, None))
    tree_insert(tree, Node(None, 15, None, None))
    tree_insert(tree, Node(None, 11, None, None))
    tree_insert(tree, Node(None, 10, None, None))
    tree_insert(tree, Node(None, 19, None, None))
    tree_insert(tree, Node(None, 12, None, None))
    print_tree(tree)

main()
