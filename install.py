#!usr/bin/env python3

import os, time

name = input("Enter your home username (/home/?): ").strip()

for char in "Installing Hacker Python for you...":
  print(char, end=" ", flush=True)
  time.sleep(0.05)

try:
    os.system(f"cp -r HackerPython /home/{name}/.config/sublime-text/Packages")
    print("\n\nDone. Activate and enjoy your theme :)")
    
except Exception as ex:
  print("\n\nError: {ex}")
