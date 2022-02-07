import os
import dropbox
from dropbox.files import WriteMode

class TransferData():
	def __init__(self, accessToken):
		self.access_token = accessToken

	def uploadFile(self, fileFrom, fileTo):
		dbx = dropbox.Dropbox(self.access_token)

		for root, dirs, files in os.walk(fileFrom):
			for fileName in files:
				localPath = os.path.join(root, fileName)
				relPath = os.path.relpath(localPath, fileFrom)
				dropboxpath = os.path.join(fileTo, relPath)
				with open(localPath, "rb") as f:
					dbx.files_upload(f.read(), dropboxpath, mode=WriteMode("overwrite"))

def main():
	acess_token = "2YiHnSB7fe4AAAAAAAAAAeRpOvAlNQ7GYyM_hsYUuzGe-igKPCIC3XqXKRDwokKU"
	dtTransfer = TransferData(acess_token)
	fileFrom = input("Enter the path of file that you want to upload: ")
	fileTo = input("Enter the full path to upload to dropbox: ")
	dtTransfer.uploadFile(fileFrom, fileTo)
	print("File has been moved")

main()