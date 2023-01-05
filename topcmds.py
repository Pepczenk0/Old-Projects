help_message = """
=================================================================
\nThis python script grabs the last 2000 commands used in
your .bash_history and makes a basic graph showing how many times
you have used those commands, and which commands they are.


This is not meant to be in any utility just a mini project
that displays the top 5 most used commands 

=================================================================

OPTIONS...

topcmds N // to show last N amount of commands range: 50-2000
e.g (topcmds 583)

topcmds -h or -H // to show this text

----------------------
github.com/Pepczenk0/
discord: Pepczenko#1665
"""

from sys import argv
from os.path import expanduser
from math import ceil


class Main:
    def __init__(self):
        self.file=open(str(expanduser("~/.bash_history")), 'r')
        
        # list of raw commands with args and times used
        self.lines = self.file.readlines()
        
        self.new_cmds = []
        self.cmds=dict({})
        # commands without extra args (wmd)
        self.cmds_wmd = []
        
        # blocks in order (visual hashtags list for the graph)
        self.bio = []
        
        # list (in order) of how many times a command has been used
        self.cmds_used_times = []
        
        
    def clean_and_sort(self, last_used_commands=2000):
        """Cleaning and sorting of the list self.lines
        this will deconstruct it into different lists"""
        if last_used_commands < 50 or last_used_commands > 2000:
            print("Input must be in between 50-2000...")
            exit()
        
        for cmd in self.lines[len(self.lines)-int(last_used_commands):-1]:
            new_cmd = cmd.partition(' ')[0]
            if new_cmd == "sudo":
                new_cmd = cmd.partition(' ')[1]
            else:
                self.new_cmds.append(new_cmd)
        
        # Increment if duplicate found in commands
        for cmd in self.new_cmds:
            if cmd not in self.cmds:
                self.cmds[cmd] = 1
            else:
                self.cmds[cmd] += 1

        # Sort most used commands
        self.cmds = dict(sorted(self.cmds.items(), key=lambda x: x[1], reverse=True))

        # top 5 most used commands
        self.top_cmds = list(self.cmds.items())[:5]

        # Parsing data from "top_cmds"
        for tuple in self.top_cmds:
            cmd = tuple[0].strip()
            self.cmds_wmd.append(cmd)
            
            self.blocks = ceil(tuple[1] / 30)
            self.bio.append(self.blocks)

            temp = tuple[1]
            self.cmds_used_times.append(temp)
    
    
    def show_graph(self):
        """Output Visual graph"""

        # Coloured texts: Red - R | Green - g | Yellow - y | Blue - b | Purple | p

        r = "\033[1;31m# " + "\033[0m"
        g = "\033[1;32m #" + "\033[0m"
        y = "\033[1;33m #" + "\033[0m"
        b = "\033[1;34m #" + "\033[0m"
        p = "\033[1;35m #" + "\033[0m"


        graph = f"""\n| 1st |: {r * self.bio[0]}| '{self.cmds_wmd[0]}' [{self.cmds_used_times[0]}]
| 2nd |:{g * self.bio[1]} | '{self.cmds_wmd[1]}' [{self.cmds_used_times[1]}]
| 3rd |:{y * self.bio[2]} | '{self.cmds_wmd[2]}' [{self.cmds_used_times[2]}]
| 4th |:{b * self.bio[3]} | '{self.cmds_wmd[3]}' [{self.cmds_used_times[3]}]
| 5th |:{p * self.bio[4]} | '{self.cmds_wmd[4]}' [{self.cmds_used_times[4]}]"""


        print(graph)


if __name__ == '__main__':
    # Check for help flag -h -H
    try:
        if argv[1] == '-h' or argv[1] == '-H':
            print(help_message)
            exit()
    except IndexError:
        pass
    
    # Check for specified value, if it doesnt exist then default to 2000
    try:
        main = Main()
        main.clean_and_sort(int(argv[1]))
        main.show_graph()
    except (IndexError, ValueError):
        main = Main()
        main.clean_and_sort()
        main.show_graph()
        
