from Database import db
from mysql.connector import Error

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
		query = "SELECT * FROM shop WHERE id = %s;"
		db.cursor.execute( query, ( id, ) )
		result = db.cursor.fetchone()
		
	except Error as e:
		print( e )	### TODO: Use a proper logging mechanism.
	
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
		query = "SELECT * FROM shop;"
		db.cursor.execute( query )
		result = db.cursor.fetchall()
	except Error as e:
		print( e )	### TODO: Use a proper logging mechanism.
	
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
		query = "SELECT * FROM shop WHERE code = %s;"
		db.cursor.execute( query, ( code, ) )
		result = db.cursor.fetchone()
		
	except Error as e:
		print( e )	### TODO: Use a proper logging mechanism.
	
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
		query = "SELECT * FROM shop WHERE region_id = %s;"
		db.cursor.execute( query, ( region_id, ) )
		result = db.cursor.fetchall()
	except Error as e:
		print( e )	### TODO: Use a proper logging mechanism.
	
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