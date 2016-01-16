import mysql.connector
import logging
from mysql.connector import Error
from Config import read_config
from Log import Log
from Log import Logdb
# Datbase Connection/Cursor Configuration
### TODO: Move these out to an ini file, and have them being server-specific settings.
defaultConnectionParams = read_config(section='mysql')

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
            Logdb.info('Attempting to connect to database')
            self.connection = mysql.connector.connect(**connectionParams)
            self.cursor = self.connection.cursor(**cursorParams)
            Logdb.info('Connected to database')

        except Error as e:
            Logdb.critical(e)
            Logdb.info('Connection failed')










    def __exit__(self):
        self.cursor.close()
        self.connection.close()


# Create a default instance of a database connection which we can then just import without having to mess about with
# connection parameters in every module.  If you want another just create your own instance of Database.
db = Database(defaultConnectionParams, defaultCursorParams)
