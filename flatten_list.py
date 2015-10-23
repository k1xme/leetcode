class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, val):
		self.val = val
		self.next = None
		self.opt = None
		

def flatten_list(l):
	dummy = ListNode(0)

	dummy.next = l

	previous_node = dummy

	while previous_node.next:
		if previous_node.next.opt:
			# Do falltening here.
			tmp = previous_node.next
			previous_node.next = previous_node.node.opt
			while previous_node.next: previous_node = previous_node.next
			previous_node.next = tmp
			continue

		previous_node = previous_node.next

	return dummy.next
		