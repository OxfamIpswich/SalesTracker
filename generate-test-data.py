#!/usr/bin/python
#
# Generate Random Test Data
#
import datetime
import Shops
from Database import FetchTree

def GenerateReading( shopId, date ):
	pass
	#print( "Shop ID: %s, DATE: %s" % ( shopId, date ) )

### TODO: Should this go somewhere else, and if so where?  Database.py?
def GetLeaves( tree ):
	
	result = []
	
	# So we recurse through each dict in the tree of categories and see if it has any children.  If it does not, it is a "leaf" so we add it to our results.
	for record in tree:
		if not record[ "children" ]:
			result.append( record )
		else:
			result.extend( GetLeaves( record[ "children" ] ) )
	
	return result

def Run():
	
	# Here we define the parameters for creating the test data.  I'll put it here for now, as it's not something that's going to
	# be part of the main app in the end, but part of the test suite.
	fiscalStart = { "month": 4, "day": 1 }
	startYear = 2014
	endYear = 2015
	
	# Define some useful time intervals.
	oneDay = datetime.timedelta( days = 1 )
	oneWeek = datetime.timedelta( weeks = 1 )
	
	# Calculate our start and end dates.
	startDate = datetime.datetime( startYear, fiscalStart[ "month" ], fiscalStart[ "day" ] )
	endDate = datetime.datetime( endYear, fiscalStart[ "month" ], fiscalStart[ "day" ] ) - oneDay
	
	### TODO: Properly sort out the financial weeks around the start and end of the year, and the start/end of the financial year, and wrap that up in a module.
	
	# Get all of the categories then identify all the "leaves" (have no children), as it's the leaves we're going to be generating data for, the data for their
	# parent categories will be calculated.
	categories = FetchTree( None, "category" )
	baseCategories = GetLeaves( categories )
	
	### DEBUG: Output the list of categories we're going to be generating data for, just for a quick sanity check.
	for cat in baseCategories:
		print( cat[ "code" ] + " " + cat[ "name" ] )
	
	# Get all the shops in the system so we can create data for them.
	shops = Shops.FetchAll()
	
	# Let's create test data for each shop in-turn.
	if shops is not None:
		for shop in shops:
			
			# Now lets loop through every day in-turn, and create a reading for it.
			currentDate = startDate
			keepGoing = True
			
			while currentDate <= endDate:
				GenerateReading( shop[ "id" ], currentDate )
				currentDate += oneDay

	else:
		print( "### ERROR: There are no shops in the database to create test data for." )

# We wrap everything in a function then call it at the bottom if this script is being executed stand-alone, so that the script
# can be imported and run from another script.	
if __name__ == "__main__":
	Run()