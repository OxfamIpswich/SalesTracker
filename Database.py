import mysql.connector
from mysql.connector import Error
from Config import read_db_config

# Datbase Connection/Cursor Configuration
### TODO: Move these out to an ini file, and have them being server-specific settings.
defaultConnectionParams = read_db_config()

defaultCursorParams = {
    "dictionary": True
}


class Database:
    """
	Convenience class for dealing with a common database connection.  You can just import the db variable into your
	code and you'll have an open connection and cursor ready to use.
	
	Example:
		
		from Database import db
		db.cursor.execute( "SELECT * FROM table_name;" )
	"""

    connection = None
    cursor = None

    def __init__(self, connectionParams, cursorParams):
        try:
            self.connection = mysql.connector.connect(**connectionParams)
            self.cursor = self.connection.cursor(**cursorParams)
            

        except Error as e:
            print(e)  ### TODO: Use a proper logging mechanism.

    def __exit__(self):
        self.cursor.close()
        self.connection.close()


# Create a default instance of a database connection which we can then just import without having to mess about with
# connection parameters in every module.  If you want another just create your own instance of Database.
db = Database(defaultConnectionParams, defaultCursorParams)
