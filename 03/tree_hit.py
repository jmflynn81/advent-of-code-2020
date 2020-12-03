SLOPES = [
    {
        "accross": 1,
        "down": 1
    },
    {
        "accross": 3,
        "down": 1
    },
    {
        "accross": 5,
        "down": 1
    },
    {
        "accross": 7,
        "down": 1
    },
    {
        "accross": 1,
        "down": 2
    }
]

def get_map():
    with open('trees') as f:
        trees = f.read().splitlines()
    return trees


def get_tree(current_horizontal, current_vertical, tree_map):

    hit = tree_map[current_vertical][current_horizontal]
    if hit == '#':
        return 1
    else:
        return 0


def get_horizontal(current_horizontal, max_horizontal, accross):
    temp = current_horizontal + accross
    if temp > max_horizontal:
        leftover = (temp % max_horizontal) - 1
        return leftover
    else:
        return(temp)


def get_slope_trees(accross, down, tree_map):
    current_horizontal = 0
    current_vertical = 0
    tree_hit_count = 0
    max_horizontal = len(tree_map[0]) - 1
    max_vertical = len(tree_map)

    while current_vertical < max_vertical:
        if not current_vertical > max_vertical:
            tree_hit_count += get_tree(current_horizontal, current_vertical, tree_map)
        current_horizontal = get_horizontal(current_horizontal, max_horizontal, accross)
        current_vertical += down

    return tree_hit_count


tree_map = get_map()
tree_tally = 1
for slope in SLOPES:
    trees = get_slope_trees(slope['accross'], slope['down'], tree_map)
    print(trees)
    tree_tally = tree_tally * trees

print()
print(tree_tally)



