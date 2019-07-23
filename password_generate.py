import getpass
import passlib
from passlib.hash import sha256_crypt

passtry1 = getpass.getpass("Enter the password to hash: ")
passtry2 = getpass.getpass("Retype password: ")

if passtry1 == passtry2:
    hash_pass = sha256_crypt.encrypt( passtry1 )
    print hash_pass
    verify = raw_input("Verify Password? y/n: ")
    if verify  == "y":
        pass_ = getpass.getpass("Please enter the secret password: ")
        if sha256_crypt.verify( pass_, hash_pass ):
            print("Everything worked!")
        else:
            print("Try again :(")
    else:
        exit

else:
    exit 
