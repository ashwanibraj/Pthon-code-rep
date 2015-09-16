import sys

class Node:
	def __init__(self, data, nxt = None):
		self.data = data
		self.next = nxt

class linked_list:
	def __init__(self, head):
		self.head = head
		self.tail = head
	def add_node(self, node):
		self.tail.next = node
		self.tail = self.tail.next				
	def print_list(self):
		n = self.head
		print n.data
		while n.next is not None:
			n = n.next
			print n.data
	def rem_node(self, val):
		h = self.head		
		flag = True
		while flag:
			if self.head.data == val:
				self.head = self.head.next
			else:
				flag = False
		while h.next is not None:
			nxt = h
			h = h.next
			if h.data == val:
				nxt.next = h.next

temp = []
x = raw_input('Enter the data for your linked list:')

temp = x.split()


if len(temp) < 1:
	sys.exit('Invalid Input')
else:
	ll = linked_list(Node(temp[0]))	
	for i in range(1,len(temp)):		
		ll.add_node(Node(temp[i]))
	print 'Linked List is:' 
	ll.print_list()


def rem_dupli_node(ll):
	sl = ll.head	
	
	while sl.next is not None:
		t = sl
		fs = sl.next
		while fs.next is not None:
			if fs.data == sl.data:
				t.next = fs.next
			else:
				t = fs
			fs = fs.next
		if fs.data == sl.data:
			t.next = None
		if sl.next is not None:
			sl = sl.next


def element_frm_end(ll):
	slo = ll.head
	fst = ll.head

	cnt1 = 1
	cnt2 = 1

	while fst.next is not None:
		cnt1 = cnt1+1
		slo = slo.next
		fst = fst.next
		if fst.next is not None:
			fst = fst.next
			cnt2 = cnt2+2
		else:
			cnt2 = cnt2 + 1
	print cnt1, cnt2, fst.data, slo.data

	element_frm_end = raw_input('Enter k to find kth to last element:')
	x=int(element_frm_end)
	if cnt2-x <= 0:
		print 'Size of array is ', cnt2, '. Enter a smaller value. Exiting.'
		return 
	if cnt2-x > cnt2/2:
		for i in range(cnt1, cnt2-x):
			slo = slo.next
		print slo.data
	else:
		fst = ll.head
		for i in range(1, cnt2-x):
			fst = fst.next
		print fst.data


print '-'*10

r = raw_input('Enter the value to be removed:')
ll.rem_node(r)
ll.print_list()

rem_dupli_node(ll)
print '-'*10
print 'Linked list after removing duplicates:'
ll.print_list()


element_frm_end(ll)

def delete_node_wo_head(node):

	while node.next is not None:
		node.data = node.next.data
		prev = node
		node = node.next
	prev.next = None

	return

#delete_node_wo_head() -- Make sure to call this only by passing a node as parameter. 
#Wont work if u take data from user, as same data can be in multiple nodes.


