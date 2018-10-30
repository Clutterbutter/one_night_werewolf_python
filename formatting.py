#If you want to run go to RUN ME!!!!!!!!!!!!!!!!!!!
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def prompt_user_continue():
    input("Press Enter to continue...")
    cls()