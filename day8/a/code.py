

lines: list = open('input.txt').read().splitlines()

tree_map: list = []

class Tree:
    ALL: list = []

    def __init__(self, size):
        self.size = int(size)
        self.visible = False
        self.ALL.append(self)


    def __repr__(self) -> str:
        return str(self.size)


    def __lt__(self, other):
        return self.size < other.size


for line in lines:
    tree_map.append([Tree(char) for char in line])


def mark_tree(tree_string: list) -> None:
    biggest_tree: Tree = tree_string[0]
    tree_string = tree_string[1:-1]

    while tree_string:
        current_tree = tree_string.pop(0)
        if current_tree > biggest_tree:
            current_tree.visible = True
            biggest_tree = current_tree


rotate = lambda l: [list(e) for e in zip(*l[::-1])]

for i in range(0,4):
    for tree_string in tree_map[1:-1]:
        mark_tree(tree_string)

    tree_map = rotate(tree_map)

visible_trees = list(set([tree for tree in Tree.ALL if tree.visible]))

default_count: int = len(tree_map[0]) * 2 + (len(tree_map) -2) * 2

print(len(visible_trees) + default_count)