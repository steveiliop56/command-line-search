import webbrowser
from colorama import Fore
import sys

base_url = "https://www.google.com/search?q="
sites = "sites%3A%5Bstackoverflow.com%2C+raspberrypi.com%2C+makeuseof.com%2C+linuxhint.com%2C+raspberrypi.org%2C+medium.com%2C+geeksforgeeks.org%2C+google.com%2C+github.com%2C+digitalocean.com%2C+reddit.com%2C+youtube.com%2C+jeffgeerling.com"
params = ""
final_url = ""

for i in range(int(len(sys.argv))):
    if i == 0:
        pass
    else:
        params = params + str(sys.argv[i]) + "+"

final_url = base_url + params + sites

print(Fore.GREEN + "Scanning the internet..." + Fore.WHITE)

webbrowser.open(final_url)