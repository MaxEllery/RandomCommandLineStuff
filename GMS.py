import webbrowser
import sys
import pyperclip

# any argument but file name present is > 1
# want copy pasta of address so all argument, ignoring sys.argv[0]

if len(sys.argv) > 1:
	if sys.argv[1] == '-h':
		print()
		print('-------------------------------------------------------')
		print('Can be used from console or as an executable .py file.')
		print('Execute the file: "python FILENAME.py WHERE TO SEARCH".')
		exit()
	
	else:
		address_string = str(' '.join(sys.argv[1:]))
	
elif len(sys.argv) <= 1:
	print('Google Maps Searcher! (GMS)')
	address_string = input('Where to search?: ')
	# address_string = pyperclip.paste()

print('Searching Google Maps for ' + address_string + '...')
webbrowser.open('https://www.google.com/maps/place/' + address_string)

