# 作者：乾
# 时间：2025年02月19日
# Mail:chb8572@gamil.com


class Node:

    def __init__(self, elem=-1, left_child=None, right_child=None):
        self.elem = elem
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree:

    def __init__(self):
        self.root = None
        self.help_queue = []  # 辅助队列

    def level_build_tree(self, new_node: Node):  # 建立新树
        if self.root is None:
            self.root = new_node
            self.help_queue.append(self.root)
        else:
            self.help_queue.append(new_node)
            if self.help_queue[0].left_child:
                self.help_queue[0].right_child = new_node
                self.help_queue.pop(0)
            else:
                self.help_queue[0].left_child = new_node
        pass

    def pre_order(self, current_node: Node):  # 前序遍历
        if current_node:
            print(current_node.elem, end=" ")
            self.pre_order(current_node.left_child)
            self.pre_order(current_node.right_child)

    def mid_order(self, current_node: Node):  # 中序遍历 左根右
        if current_node:
            self.mid_order(current_node.left_child)
            print(current_node.elem, end=" ")
            self.mid_order(current_node.right_child)

    def post_order(self, current_node: Node):  # 后序遍历
        if current_node:
            self.post_order(current_node.left_child)
            self.post_order(current_node.right_child)
            print(current_node.elem, end=" ")

    def level_order(self, current_node: Node):  # 层次遍历
        help_queue = [current_node]
        while help_queue:
            node = help_queue.pop(0)
            print(node.elem, end=" ")
            if node.left_child:
                help_queue.append(node.left_child)
            if node.right_child:
                help_queue.append(node.right_child)


if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(1, 11):
        node = Node(i)
        tree.level_build_tree(node)
    print('前序遍历:', end=" ")
    tree.pre_order(tree.root)
    print('')
    print('中序遍历:', end=" ")
    tree.mid_order(tree.root)
    print('')
    print('后序遍历:', end=" ")
    tree.post_order(tree.root)
    print('')
    print('层次遍历:', end=" ")
    tree.level_order(tree.root)
    pass
