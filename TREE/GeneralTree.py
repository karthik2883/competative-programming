class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "!__" if self.parent else" "
        print(prefix + self.data)
        for child in self.children:
            child.print_tree()


def build_product_tree():
    root = TreeNode("Electronic")
    laptop = TreeNode("laptop")
    laptop.add_child(TreeNode("MackBook"))
    laptop.add_child(TreeNode("Microsoft-Surface"))
    laptop.add_child(TreeNode("ThinkPad"))

    cellphone = TreeNode("cellphone")
    cellphone.add_child(TreeNode("Iphone"))
    cellphone.add_child(TreeNode("Google-Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("tv")
    tv.add_child(TreeNode("SamSung"))
    tv.add_child(TreeNode("MI"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    root.print_tree()


if __name__ == '__main__':
    build_product_tree()
