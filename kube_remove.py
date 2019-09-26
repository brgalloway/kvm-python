!/usr/bin/python3.6

import sys,os
import subprocess as sp

objects_created = [
  "serviceaccount",
  "clusterrole",
  "clusterrolebindings",
  "role",
  "rolebindings",
  "deployments",
  "services",
  "ingress"
]
discovered = []

def search_words():
    search_word = input("Enter search string: ")
    return search_word

def fetch_objects(search_word):
    namespace = input("enter namespace: ")
    argument_string = f"kubectl get -n {namespace}"
    for i in objects_created:
        output = sp.getoutput(f"{argument_string} {i}| grep -i {search_word}| cut -d' ' -f1")
        if search_word in output:
            print(f"found {i} named {output}")

if __name__ == '__main__':
    search_word = search_words()
    fetch_objects(search_word)
