from colorama import Fore, Style

prefix_start = "sites%3A%5B"
prefix_add = "%2C+"
final_sites = ""

sites = input("Enter the sites that you want to add to your list seperated by a space: ").split()

final_sites = prefix_start + sites[0]

for i in range(1, int(len(sites))):
    final_sites = final_sites + prefix_add + sites[i]

print(f"Here is your final url {Fore.GREEN + final_sites}." + Style.RESET_ALL() + "Now add it in sites in the search.py file.")
