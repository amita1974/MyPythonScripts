'''
Important!!! Any change in this file - please do in
D:\\Users\\AA\\Unbacked2cloud\\Code\\GitHub\\MyPythonApps\\renameFileNamesAddCreationDate
and then copy the latest version to the HP Scans destination folder (D:\\Users\\AA\\Pictures\\Scan_docs\\HP_SCANS)
The latest version in D:\\Users\\AA\\code\\MyPythonApps\\renameFileNamesAddCreationDate is maintained by git and pushed to my github repo
https://github.com/amita1974/MyPythonScripts
'''

import os, datetime

workingDir = './'
destDirName = './fNamesWithDateTime/'
filesToRenameExtensions = (['.jpg', '.pdf']);
'''
# Enable this code to support rename of files that will only have the time and date, without other properties, in order
  to allow destinguish between destination files with the same name due to being created at the exact same time.
newfilesDictionary = {} 
'''
renamedFilesCount = 0

# Get a list of files in the workingDir
filelist = os.listdir(workingDir)

if (os.path.exists(destDirName) == False):
	os.makedirs(destDirName)

for file in filelist:
	# split the file into filename and extension
	filename, extension = os.path.splitext(file)
	# if the extension is a valid extension
	if (extension in filesToRenameExtensions):
		# Get the create time of the file
		create_time = os.path.getctime( file )
		# convert it to a readable timestamp format
		format_time = datetime.datetime.fromtimestamp( create_time )
		# convert time into string
		format_time_string = format_time.strftime("%Y-%m-%d_%H%M%S__") # e.g. 2023-09-21_182038__.jpg
		# Construct the new name of the file
		newfile = format_time_string + filename + extension

		'''
		# If there is other files created at the same timestamp that has the exact same file name create another running index postfix in the file name
		if (newfile in newfilesDictionary.keys()):
			index = newfilesDictionary[newfile] + 1;
			newfilesDictionary[newfile] = index;
			newfile = format_time_string + filename + '-' + str(index) + extension; # e.g. 2015-01-01 09.00.00-1.jpg
		else:
			newfilesDictionary[newfile] = 0;
		'''
		newfile = destDirName + newfile;
		# rename the file and put it in the new dir
		try:
			os.rename( file, newfile );
		except FileNotFoundError:
			print ("Error: FileNotFoundError exception !!!")
		# renamedFilesCount the number of files that were renamed
		renamedFilesCount = renamedFilesCount + 1
		# printing log
		print( file.rjust(35) + '    =>    ' + newfile.ljust(35) )


print( 'All done. ' + str(renamedFilesCount) + ' files were renamed. Renamed files location: ' + destDirName)
input("Press Enter to continue...")

