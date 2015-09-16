class Node:
	def __init__(self, data):
		self.l_child = None
		self.r_child = None
		self.val = data

def insert_node(root, node):
	if root == None:
		root = node
	else:
		if node.val < root.val:
			if root.l_child == None:
				root.l_child = node
			else:
				insert_node(root.l_child, node)
		else:
			if root.r_child == None:
				root.r_child = node
			else:
				insert_node(root.r_child, node)

def dps_in_order(root):
	if not root:
		return
	dps_in_order(root.l_child)
	print(root.val)
	dps_in_order(root.r_child)

def dps_pre_order(root):
	if not root:
		return
	print(root.val)
	dps_pre_order(root.l_child)
	dps_pre_order(root.r_child)

def dps_post_order(root):
	if not root:
		return
	dps_post_order(root.l_child)
	dps_post_order(root.r_child)
	print(root.val)

from sys import argv

args = [None] * 10
args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7]= argv

r = Node(args[1])
insert_node(r, Node(args[2]))
insert_node(r, Node(args[3]))
insert_node(r, Node(args[4]))
insert_node(r, Node(args[5]))
insert_node(r, Node(args[6]))
insert_node(r, Node(args[7]))

print("Pre-order:")
dps_pre_order(r)

print("In-order:")
dps_in_order(r)

print("Post-order:")
dps_post_order(r)