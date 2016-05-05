import psycopg2
import logging
from psycopg2 import OperationalError
from Config import read_config
from Log import Log
defaultConnectionParams = read_config(section='psql')

defaultCursorParams = {

}


class Databasepsql:

    connection = None
    cursor = None

    def __init__(self, connectionParams, cursorParams):
         try:
                Log.info(('DATABASE:', 'Trying to connect to database'))
                self.connection = psycopg2.connect(**connectionParams)
                self.cursor = self.connection.cursor(**cursorParams)
                Log.info(('DATABASE:', 'Connected to database'))
         except OperationalError as e:
             Log.critical(('DATABASE:',e))
             Log.info(('DATABASE: Connection Params:', connectionParams))
             Log.info(('DATABASE: Cursor Params:', cursorParams))
             Log.info(('DATABASE:', 'Connection failed'))


    def __xor__(self):
        self.cursor.close()
        self.connection.close()

testdb = Databasepsql(defaultConnectionParams,defaultCursorParams)








