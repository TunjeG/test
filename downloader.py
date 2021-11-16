#! python3
import requests,pyperclip

# Takes content from the clipboard as the address
address = pyperclip.paste()
res = requests.get(address)
res.raise_for_status()

# the downloaded file is stored
playFile = open('new_download.txt', 'wb')

# this method returns chunk of the content on each iteration of the loop
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
