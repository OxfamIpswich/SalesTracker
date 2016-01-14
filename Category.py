class Category:
	"""
	Sales Category entity, which are linked together in a hierarchy.
	"""
	
	id = None
	parent_id = None
	name = None
	code = None
	
	def __init__( self, name, id = None, parent_id = None, code = None ):
		"""
		Args:
			name				string(255)	The common name of the category.  Required.
			id					int					The unique identifier of the Category.
			parent_id		int					The unique identifier of the parent Category.  Root-level categories have a NULL parent.
			code				string(3)		Three-letter code used for the category, only used to label items to be tracked through a sales point.
		"""
		if name is not None:
			self.name = name
		
		if id is not None:
			self.id = id
			
		if parent_id is not None:
			self.parent_id = parent_id
		
		if code is not None:
			self.code = code