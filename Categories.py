from Database import db
from mysql.connector import Error

def FetchById( id ):
	"""
	Fetches an individual category record from the database using the specified identifier.
	
	Args:
		id: int, the unique identifier of the category.
	
	Returns:
		A dict containing all the category fields: id, parent_id, name, code
	"""
	result = None
	
	try:
		query = "SELECT * FROM category WHERE id = %s;"
		db.cursor.execute( query, ( id, ) )
		result = db.cursor.fetchone()
		
	except Error as e:
		print( e )	### TODO: Use a proper logging mechanism.
	
	return result


def FetchByParentId( parent_id ):
	"""
	Fetch all the category records that have the specified parent_id.
	
	Args:
		parent_id: int, the unique identifier of the parent category.
	
	Returns:
		A list of dicts containing all the category records with the matching parent_id.
	"""
	result = None
	
	try:
		query = "SELECT * FROM category WHERE parent_id = %s;"
		db.cursor.execute( query, ( parent_id, ) )
		result = db.cursor.fetchall()
	except Error as e:
		print( e )	### TODO: Use a proper logging mechanism.
	
	return result