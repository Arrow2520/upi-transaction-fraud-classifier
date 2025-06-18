class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()


aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


# Binary Tree
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


tree_tuple = ((1, 3, None), 2, (None, 3, 4), 5, (6, 7, 8))


def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


tree1 = parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))


def tree_to_tuple(tree):
    if tree is None:
        return None
    if tree.left is None and tree.right is None:
        return tree.key

    left_tuple = tree_to_tuple(tree.left)
    right_tuple = tree_to_tuple(tree.right)

    return left_tuple, tree.key, right_tuple


def display_keys(node, space='\t', level=0):
    if node is None:
        print(space*level + '@')
        return
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    display_keys(node.right, space, level + 1)
    print(space*level + str(node.key))
    display_keys(node.left, space, level+1)


def traverse_in_order(node):
    if node is None:
        return []
    return traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right)


def traverse_pre_order(node):
    if node is None:
        return []
    return [node.key] + traverse_pre_order(node.left) + traverse_pre_order(node.right)


def traverse_post_order(node):
    if node is None:
        return []
    return traverse_post_order(node.left) + traverse_post_order(node.right) + [node.key]


def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)

# Binary Search Trees from here on


tree2 = parse_tuple((('aakash', 'biraj', 'hemanth'), 'jadesh', ('siddhant', 'sonaksh', 'vishal')))


def remove_none(nums):
    return [x for x in nums if x is not None]


def is_bst(node):
    if node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and (max_l is None or node.key > max_l) and (min_r is None or node.key < min_r))
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    return is_bst_node, min_key, max_key

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node


tree = insert(None, jadhesh.username, jadhesh)
insert(tree, biraj.username, biraj)
insert(tree, sonaksh.username, sonaksh)
insert(tree, aakash.username, aakash)
insert(tree, hemanth.username, hemanth)
insert(tree, siddhant.username, siddhant)
insert(tree, vishal.username, siddhant)


def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)


def update(node, key,value):
    target = find(node, key)
    if target is not None:
        target.value = value


update(tree, 'hemanth', User('hemanth', 'Hemanth J', 'hemanthj@example.com'))
node = find(tree, 'hemanth')
# print(node.value)


def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)


print(list_all(tree))


def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_l, height_r)
    return balanced, height
