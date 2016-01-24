import mysql.connector
import logging
from mysql.connector import Error
from Config import read_config
from Log import Log

# Datbase Connection/Cursor Configuration
### TODO: Move these out to an ini file, and have them being server-specific settings.
defaultConnectionParams = read_config(section='mysql')

defaultCursorParams = {
	"dictionary": True
}


class Database:
	"""
	Convenience class for dealing with a common database connection.	You can just import the db variable into your
	code and you'll have an open connection and cursor ready to use.

	Example:
		
		from Database import db
		db.cursor.execute( "SELECT * FROM table_name;" )
	"""
	connection = None
	cursor = None

	def FetchByID(self,table_name,id,id_field='id'):
		"""
		Generic function to fetch a single row from database using simple WHERE id_field = id query
		Args:
		    table_name:
		    id:
		    id_field:

		Returns:
		Dict of data contained inside field
		"""


		result = None

		query = "SELECT * FROM "+table_name+" WHERE "+id_field+" = %(id)s"
		self.cursor.execute(query,{'id':id})
		result = self.cursor.fetchone()

		return result


	def __init__(self, connectionParams, cursorParams):
	 
		try:
			Log.info(('DATABASE:', 'Trying to connect to database'))
			self.connection = mysql.connector.connect(**connectionParams)
			self.cursor = self.connection.cursor(**cursorParams)
			Log.info(('DATABASE:', 'Connected to database'))
		except Error as e:
			Log.critical(('DATABASE:', e))
			Log.info(('DATABASE: Connection Params:', connectionParams))
			Log.info(('DATABASE: Cursor Params:', cursorParams))
			Log.info(('DATABASE:', 'Connection failed'))

	def __exit__(self):
		self.cursor.close()
		self.connection.close()


# Create a default instance of a database connection which we can then just import without having to mess about with
# connection parameters in every module.	If you want another just create your own instance of Database.
db = Database(defaultConnectionParams, defaultCursorParams)



def FetchTree( root_id, table_name, id_field = "id", parent_id_field = "parent_id", children_property = "children" ):
	"""
	Fetches a tree structure from a database table, where the table has the following structure:
		id					unique identifier of the record
		parent_id		key that points to the id of a parent record in this table, or null if the record has no parent.
	
	The field names (id, parent_id) used can be overridden with the corresponding named arguments (id_field and parent_id_field respectively).
	
	###
	### WARNING: NOT SAFE - Data passed to the table_name, id_field, and parent_id_field MUST be clean.  DO NOT derrive these values directly
	###                     from user input.
	
	Args:
		root_id							The unique identifier of the root record to get the children of.  NOTE: This function does not return the record specified by this id.
		table_name					string: The name of the database table to query.	### WARNING: THIS VALUE MUST BE CLEAN.
		id_field						string, optional: The name of the field to use for the record id.  By default this is "id".	### WARNING: THIS VALUE MUST BE CLEAN.
		parent_id_field			string, optional: The name of the field to use for the record parent id.  By default this is "parent_id".	### WARNING: THIS VALUE MUST BE CLEAN.
		children_property		string, optional: The name of the property within a records dict that their children are stored.  By default this is "children".

	Returns:
		The result is a list of dicts representing the first layer, and then each dict has a "children" property set that will contain a list of dicts of any children of 
		that record, otherwise None if there aren't any.  The name of the property used here can be overridden using the named argument children_property.

	Example:
		
		CREATE TABLE category ( id INT PRIMARY KEY, parent_id INT, name VARCHAR(50) );
		INSERT INTO category VALUES ( 1, NULL, "Books" ), ( 2, 1, "Fiction" ), ( 3, 1, "Crime" );
		
		from Database import FetchTree
		print( FetchTree( None, "category" ) )
		
		[
			{ "id": 1, "parent_id": None, "name": "Books", "children":
			[
				{ "id": 2, "parent_id": 1, "name": "Fiction", "children": None },
				{ "id": 3, "parent_id": 1, "name": "Crime", "children": None }
			]
		]
	"""

	# Built the SQL query to select the next level of this branch in the tree, taking care to handle the case where the root
	# could be null.
	query = "SELECT * FROM " + table_name + " WHERE " + parent_id_field
	if root_id is not None:
		query += " = %(root_id)s"
	else:
		query += " IS NULL"
	
	db.cursor.execute( query, { "root_id": root_id } )
	children = db.cursor.fetchall()
	
	if children is not None:
		for child in children:
			child[ children_property ] = FetchTree( child[ id_field ], table_name )
	
	return children

