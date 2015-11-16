from __future__ import with_statement
from contextlib import closing
from zipfile import ZipFile, ZIP_DEFLATED
import os
import datetime
import time
import glob
import shutil
from os import listdir
import zipfile
import fileinput
import os.path
import re



print("This program takes files in order of download and renames")
print("The first file to be downloaded from the scanner should be")
print("the plugin.html then the executive.html and finally the .csv")
#Initialize variables
raw_input("Press Enter to continue...")

	##Testing
	##create test files

		
while True:
	user_profile = os.environ['USERPROFILE']
	if not os.path.exists(user_profile+"/documents/AutoMoveInternal/"):
		print ("###  Creating File for Target ...."+user_profile+"/documents/AutoMoveInternal/ File" )
		os.makedirs(user_profile+"/documents/AutoMoveInternal/")
	target = os.path.dirname(user_profile+"/documents/AutoMoveInternal/") 
	os.chdir(target)

	##Testing
	##create test files
	# if os.path.isfile("exec.html") == False:
		# open("exec.html",'w')
	# if os.path.isfile("plugin.html") == False:
		# open("plugin.html",'w')
	# if os.path.isfile("itisacsv.csv") == False:
		# open("itisacsv.csv",'w')
	fnames = glob.glob("*.html")
	csvname = glob.glob("*.csv")
	print csvname
	root_src_dir = target
	root_dst_dir = raw_input('Paste destination Directory here:')


	# Gets current date
	ScanDate=(time.strftime("%Y-%m-%d"))
	#Regex file location and remove everything but company name
	name=re.search('2015\\\\(.+)',root_dst_dir)
	if name:
		CompanyName=name.group(1)

	os.chdir(target)
	#print "Scan Date is " + ScanDate
	os.chdir(target)
	# get a list of all files

	
	# sort according to time of last modification/creation 
	# reverse: newer files first
	fnames.sort(key=lambda x: os.stat(x).st_ctime, reverse=True)
	# rename files,
	#print csvname[0]
	yes = set(['yes','y', 'ye', ''])
	no = set(['no','n'])
	IsInternal=raw_input('Is this scan Internal? Y/N: ')
	IsInternal=IsInternal.lower()

	def MoveFile(ZipName,root_dst_dir):
		shutil.move(ZipName+'.zip',root_dst_dir)
	def zipFile(ZipName,root_dst_dir):
		newZip = zipfile.ZipFile(ZipName+'.zip', 'w')
		fnames = glob.glob("*.html")
		csvname = glob.glob("*.csv")
		newZip.write(fnames[1], compress_type=zipfile.ZIP_DEFLATED)
		newZip.write(fnames[0], compress_type=zipfile.ZIP_DEFLATED)
		newZip.write(csvname[0], compress_type=zipfile.ZIP_DEFLATED)
		shutil.move(csvname[0],root_dst_dir)
		shutil.move(fnames[1],root_dst_dir)
		shutil.move(fnames[0],root_dst_dir)
		newZip.close()

	
	#code to run for internal scan
	if IsInternal in yes:
		os.rename(csvname[0],("DNI - "+CompanyName+"- SecurScan Quarterly VA -"+ScanDate+"[int].csv"))
		os.rename(fnames[0],("DNI -"+CompanyName+"_VA_"+ScanDate+"_exec[int].html"))
		os.rename(fnames[1],("DNI -"+CompanyName+"_VA_"+ScanDate+"_full[int].html"))
		ZipName = 'DNI - '+CompanyName+' - SecurScan Quarterly VA - '+ScanDate+' [int]'
		zipFile(ZipName,root_dst_dir)
		MoveFile(ZipName,root_dst_dir)
		break
	if IsInternal in no:
		os.rename(csvname[0],("DNI - "+CompanyName+"- SecurScan Quarterly VA -"+ScanDate+"[ext].csv"))
		os.rename(fnames[0],("DNI -"+CompanyName+"_VA_"+ScanDate+"_exec[ext].html"))
		os.rename(fnames[1],("DNI -"+CompanyName+"_VA_"+ScanDate+"_full[ext].html"))
		ZipName = 'DNI - '+CompanyName+' - SecurScan Quarterly VA - '+ScanDate+' [ext]'
		zipFile(ZipName,root_dst_dir)
		MoveFile(ZipName,root_dst_dir)
		break
	else:
		sys.stdout.write("Please respond with 'yes' or 'no'")
		

	break
else:
	print "an unspecified error has occurred "




