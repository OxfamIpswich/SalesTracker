from Database import db
from mysql.connector import Error

def FetchById( id ):
	"""
	Fetches an individual region record from the database using the specified identifier.
	
	Args:
		id: int, the unique identifier of the region.
	
	Returns:
		A dict containing all the region fields: id, parent_id, code, name
	"""
	result = None
	
	try:
		query = "SELECT * FROM region WHERE id = %s;"
		db.cursor.execute( query, ( id, ) )
		result = db.cursor.fetchone()
		
	except Error as e:
		print( e )	### TODO: Use a proper logging mechanism.
	
	return result


def FetchByCode( code ):
	"""
	Fetches an individual region record from the database using the specified region code.
	
	Args:
		code: string, the region's code.
	
	Returns:
		A dict containing all the region fields: id, parent_id, code, name
	"""
	result = None
	
	try:
		query = "SELECT * FROM region WHERE code = %s;"
		db.cursor.execute( query, ( code, ) )
		result = db.cursor.fetchone()
		
	except Error as e:
		print( e )	### TODO: Use a proper logging mechanism.
	
	return result