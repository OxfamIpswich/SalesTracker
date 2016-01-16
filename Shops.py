from Database import db
from mysql.connector import Error
from Log import Log
import Regions

def FetchById( id ):
	"""
	Fetches an individual shop record from the database using the specified identifier.
	
	Args:
		id: int, the unique identifier of the shop.
	
	Returns:
		A dict containing all the shop fields: id, region_id, code, name
	"""
	result = None
	
	try:
		Log.info(('SHOPS-Fetch-Id:', 'Trying to grab data from table using Id'))
		query = "SELECT * FROM shop WHERE id = %s;"
		db.cursor.execute( query, ( id, ) )
		result = db.cursor.fetchone()
		Log.info(('SHOPS-Fetch-Id:', 'Successfully grabbed data'))
		
	except Error as e:
		Log.error(('SHOPS-Fetch-Id:', e))
		Log.info(('SHOPS-Fetch-Id:', query))
		Log.info(('SHOPS-Fetch-Id:', 'Failed to grab data'))
	return result

def FetchAll():
	"""
	Fetch all the shop records in the system.
	
	Args:
		None
	
	Returns:
		A list of dicts containing all the shop records in the system.
	"""
	result = None
	
	try:
		Log.info(('SHOPS-Fetch-All:', 'Trying to grab all data from table'))
		query = "SELECT * FROM shop;"
		db.cursor.execute( query )
		result = db.cursor.fetchall()
		Log.info(('SHOPS-Fetch-All:', 'Successfully grabbed data'))
	except Error as e:
		Log.error(('SHOPS-Fetch-All:', e))
		Log.info(('SHOPS-Fetch-All:Query:', query))
		Log.info(('SHOPS-Fetch-All:', 'Failed to grab data'))

	return result

def FetchByCode( code ):
	"""
	Fetches an individual shop record from the database using the specified shop code.
	
	Args:
		code: string, the shop's code.
	
	Returns:
		A dict containing all the shop fields: id, region_id, code, name
	"""
	result = None
	
	try:
		Log.info(('SHOPS-Fetch-Code:', 'Trying to grab data from table using Code'))
		query = "SELECT * FROM shop WHERE code = %s;"
		db.cursor.execute( query, ( code, ) )
		result = db.cursor.fetchone()
		Log.info(('SHOPS-Fetch-Code:', 'Successfully grabbed data'))
		
	except Error as e:
		Log.error(('SHOPS-Fetch-Code:', e))
		Log.info(('SHOPS-Fetch-Code:Query:',query))
		Log.info(('SHOPS-Fetch-Code:', 'Failed to grab data'))
	
	return result


def FetchByRegionId( region_id ):
	"""
	Fetch all the shop records that have the specified region_id (i.e. those that belong to the specified area).
	
	Args:
		region_id: int, the unique identifier of the region this shop belongs to.
	
	Returns:
		A list of dicts containing all the shop records that belong to the specified region (area).
	"""
	result = None
	
	try:
		Log.info(('SHOPS-Fetch-RegionId:', 'Trying to grab data from table using RegionId'))
		query = "SELECT * FROM shop WHERE region_id = %s;"
		db.cursor.execute( query, ( region_id, ) )
		result = db.cursor.fetchall()
		Log.info(('SHOPS-Fetch-RegionId', 'Successfully grabbed data'))
	except Error as e:
		Log.error(('SHOPS-Fetch-RegionId', e))
		Log.info(('SHOPS-Fetch-RegionId:Query:', query))
		Log.info(('SHOPS-Fetch-RegionId', 'Failed to grab data'))
	
	return result


def FetchByRegionCode( code ):
	"""
	Fetch all the shop records that belong to the region specified by the region code.  This is a common use-case internally
	within Oxfam.
	
	Args:
		code: string, the region code 
	
	Returns:
		A list of dicts containing all the shop records that belong to the specified region (area).
	"""
	result = None
	
	# While we could just do this in one SQL statement, we're going to use the Regions module so that the code is more robust.
	# This can be changed if required when we look at optimization.
	region = Regions.FetchByCode( code )
	
	if region is not None:
		try:
			query = "SELECT * FROM shop WHERE region_id = %s;"
			db.cursor.execute( query, ( region[ "id" ], ) )
			result = db.cursor.fetchall()
		except Error as e:
			print( e )	### TODO: Use a proper logging mechanism.
	
	return result