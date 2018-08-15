class node:
	def __init__(self,value=None):
		self.value=value
		self.left_child=None
		self.right_child=None
		self.parent=None


class binary_search_tree:
	def __init__(self):
		self.root=None

	def insert(self,value):
		if self.root==None:
			self.root=node(value)
		else:
			self._insert(value,self.root)

	def _insert(self,value,cur_node):
		if value<curr_node.value:
			