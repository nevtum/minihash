Building an executable
---------------

In the console make sure Python 3 and PyInstaller set up. To install pyinstaller type the following in the command prompt:

    $pip install pyinstaller
	
Build the executable:
	
	$pyinstaller --onefile minihash.py

The built file will be located in the dist folder.