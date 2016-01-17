from Database import db
from mysql.connector import Error
from Log import Log

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
		Log.info(('CATEGORIES-Fetch-Id:', 'Trying to grab data from table using Id'))
		query = "SELECT * FROM category WHERE id = %s;"
		db.cursor.execute( query, ( id, ) )
		result = db.cursor.fetchone()
		Log.info(('CATEGORIES-Fetch-Id:', 'Successfully grabbed data'))

	except Error as e:
		Log.error(('CATEGORIES-Fetch-Id:', e))
		Log.info(('CATEGORIES-Fetch-Id:Query:', query))
		Log.info(('CATEGORIES-Fetch-Id:','Failed to grab data'))

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
		Log.info(('CATEGORIES-Fetch-ParentId:', 'Trying to grab data from table using ParentId'))
		query = "SELECT * FROM category WHERE parent_id = %s;"
		db.cursor.execute( query, ( parent_id, ) )
		result = db.cursor.fetchall()
		Log.info(('CATEGORIES-Fetch-ParentId:', 'Successfully grabbed data'))
	except Error as e:
		Log.error(('CATEGORIES-Fetch-ParentId:', e))
		Log.info(('CATEGORIES-Fetch-ParentId:Query:', query ))
		Log.info(('CATEGORIES_Fetch-ParentId:', 'Failed to grab data'))

	return result

def FetchAll():


	result = None

	try:
		Log.info(('CATEGORIES-Fetch-All:', 'Trying to grab all data from table'))
		query = "SELECT * FROM category;"
		db.cursor.execute( query )
		result = db.cursor.fetchall()
		Log.info(('CATEGORIES-Fetch-All', 'Successfully grabbed data'))
	except Error as e:
		Log.error(('CATEGORIES-Fetch-All', e))
		Log.info(('CATEGORIES-Fetch-All:Query:', query))
		Log.info(('CATEGORIES-Fetch-All:', 'Failed to grab data'))

		return result


