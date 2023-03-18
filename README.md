## Command line search

Are you frustrated with switching tabs every time an error pops up? Yes, I am. It's time-consuming! So, I created this tool that, by just typing a single character and the search parameters, it will pop up a new tab ready for you to see what you want on your chosen sites.

### Installation 

Firstly, you need to clone this repository with this command:

```Shellscript
git clone https://github.com/raspberrydeveloper/command-line-search
```

Secondly install the required python modules:

```Shellscript
pip3 install colorama
```

Thirdly, generate the URL list by running this command in the project folder:

```Shellscript
python3 sites_add.py
```

A prompt will pop up asking you to enter you favorite sites for troubleshouting and the it will spit out some *googl*-y stuff, so take this string and add it to your search.py in line 6 in the sites variable.

Now make the script executable with this command:

```Shellscript
chmod +x search.py
```

Last but not least, either move the file somewhere or just leave it in this folder, then open your ***.bashrc*** file and add the following line (make sure to replace the path with your own. I am assuming that the file is in the ***project*** folder in the user's directory):

```Shellscript
alias s=~/command-line-search/search.py
```

### Usage

To use this command just type s in you terminal and if you did everything right a browser windows will pop up searching what you want. Here is an example:

```Shellscript
s raspberry pi camera
```