#!/usr/bin/python
#
# Generate Random Test Data
#
import Shops

def Run():
	print( "\nGENERATING RANDOM TEST DATA" )
	print( "---------------------------" )
	
	# First, let's get all the shops in the system so we can create data for them.
	shops = Shops.FetchAll()
	
	# Let's create test data for each shop in-turn.
	if shops is not None:
	
		for shop in shops:
			print( "\tCreating test data for: %s" % shop[ "name" ] )
	
	else:
		print( "### ERROR: There are no shops in the database to create test data for." )

# We wrap everything in a function then call it at the bottom if this script is being executed stand-alone, so that the script
# can be imported and run from another script.	
if __name__ == "__main__":
	Run()