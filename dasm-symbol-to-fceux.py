#!/bin/python

import sys
import re

#Convert a DASM Listing or SYMBOL file to FCEUX NL format

def convert_symbol_to_nl( symbol_filename, nl_filename ):
	symbol_file = open( symbol_filename, "rt" )
	nl_file = open( nl_filename, "wt" )
	for symbol_line in symbol_file:
		if "---" in symbol_line: #skip symbol comment lines
			continue
		tokens = re.split( ' +', symbol_line )
		if len( tokens ) >= 2: #if this looks like a valid line
			nl_line = "$"+tokens[1]+"#"+tokens[0]+"#\n"
			nl_file.write( nl_line )

if len( sys.argv ) != 3:
	print ("Usage: " + sys.argv[0] + " symbol_file.sym nl_file.nl")

convert_symbol_to_nl( sys.argv[1], sys.argv[2] )
