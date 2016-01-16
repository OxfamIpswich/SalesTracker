from Database import db
from mysql.connector import Error
from Log import Log

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
		Log.info(('REGIONS-Fetch-Id:', 'Trying to grab data from table using Id'))
		query = "SELECT * FROM region WHERE id = %s;"
		db.cursor.execute( query, ( id, ) )
		result = db.cursor.fetchone()
		Log.info(('REGIONS-Fetch-Id:', 'Successfully grabbed data'))
	except Error as e:
		Log.error(('REGIONS-Fetch-Id:', e))
		Log.info(('REGIONS-Fetch-Id:Query:', query))
		Log.info(('REGIONS-Fetch-Id:', 'Failed to grab data'))
	
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
		Log.info(('REGIONS-Fetch-Code', 'Trying to grab data from table using Code'))
		query = "SELECT * FROM region WHERE code = %s;"
		db.cursor.execute( query, ( code, ) )
		result = db.cursor.fetchone()
		Log.info((('REGIONS-Fetch-Code', 'Successfully grabbed data')))

	except Error as e:
		Log.info(('REGIONS-Fetch-Code', e))
		Log.info(('REGIONS-Fetch-Code:Query:', query))
		Log.info(('REGIONS-Fetch-Code:', 'Failed to grab data'))
	
	return result