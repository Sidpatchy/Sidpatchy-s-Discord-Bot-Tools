# This file is intended to create functions that are used in other parts of this tool suite. It will also contain a minimal CLI for adding the bot token to a file for the user (and perhaps more in the future)
# Additionally, this is apart of Sidpatchy's Discord Bot Tools, the library can be found on GitHub.

import os
import datetime as DT

#Functions

# writeFile() writes a string to the specified file
# Usage: 
#   file: string, filename
#   string: string to be written to file.
#   time: Boolean, whether or not the time should be logged.
def writeFile(file, string, time):
    f = open(file, 'a')
    f.write(string)
    if time == True:
        f.write(str(DT.datetime.now()))
    f.write('\n')
    f.close()

# readFile() reads a file
# Usage: 
#   file: string, filename
def readFile(file):
    f = open(file, 'r')
    contents = f.read()
    return contents
    f.close()

# reads the bot token from token.txt
def retrieveToken():
    return readFile('token.txt')