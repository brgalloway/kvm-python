#!/usr/bin/python3.6

import sys
import subprocess as sp

def list_running():
    sp.call("docker image ls", shell=True)

def list_all():
    sp.call("docker image ls -a", shell=True)

def bulk_delete():
    sp.call("for i in $(sudo docker image ls -a| awk print '{$2}'); do sudo docker image rmi -f ${i}; done", shell=True)

def menu_selection(prompt, dispatch_dict): 
    while True:
        response = input(prompt)
        response = response.lower()
        response = response.strip()
        try:
            if dispatch_dict[response]() == "quit":
                sys.exit()
        except KeyError:
            print("\n\ninvalid response\n")

def quit_app():
    return "quit"

# main menu items    
main_menu = "Choose one of the following options. \n\n" \
            "1 - show running images \n" \
            "2 - show all images \n" \
            "3 - delete all images \n" \
            "4 - Quit \n" \
            ">> "

# value returned from choice keys
main_dispatch = {
    "1": list_running,
    "2": list_all,
    "3": bulk_delete,
    "4": quit_app
}

if __name__ == '__main__':
    menu_selection(main_menu, main_dispatch)
