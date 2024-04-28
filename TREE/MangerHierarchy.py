# Data structures exercise: General Tree
# Below is the management hierarchy of a company.
# Here is how your main function should will look like,
#
# if __name__ == '__main__':
#     root_node = build_management_tree()
#     root_node.print_tree("name") # prints only name hierarchy
#     root_node.print_tree("post") # prints only post hierarchy
#     root_node.print_tree("both") # prints both (name and post) hierarchy
class TreeNode:
    def __init__(self, name, post):
        self.name = name
        self.post = post
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_length(self):
        length = 0
        p = self.parent
        while p:
            length += 1
            p = p.parent
        return length

    def print_tree(self, Option):
        if Option == "name":
            value = self.name
        elif Option == "post":
            value = self.post
        else:
            value = self.name + "(" + self.post + ")"

        spaces = ' ' * self.get_length() * 3
        prefix = spaces + "!__" if self.parent else " "
        print(prefix + value)
        for child in self.children:
            child.print_tree(Option)


def build_prod_tree():
    root = TreeNode("Nilpul", "CTO")
    Chinmay = TreeNode("Chinmay", "CTO")
    Vishwa = TreeNode("Vishwa", "Infrastructure Head")
    Vishwa.add_child(TreeNode("Dhaval", "Cloud Manager"))
    Vishwa.add_child(TreeNode("Abijit", "AppManager"))
    Chinmay.add_child(Vishwa)
    Aamir = TreeNode("Aamir", "Application Head")
    Chinmay.add_child(Aamir)

    Gels = TreeNode("Gels", "Hr Head")
    Peter = TreeNode("Peter", "Recruitment Manager")
    Waqas = TreeNode("Waqas", "Policy Manager")
    Gels.add_child(Peter)
    Gels.add_child(Waqas)
    root.add_child(Gels)
    root.add_child(Chinmay)
    root.print_tree("post")


if __name__ == '__main__':
    build_prod_tree()
