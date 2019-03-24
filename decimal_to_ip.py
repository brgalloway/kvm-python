#!/usr/bin/python

from ipaddress import ip_address
from sys import argv


def decimalConverter(addressFile):
    convertedList = []
    convertoutput = open('./convertedoutput.txt', 'w')
    with open(addressFile) as f:
        addressList = f.readlines()
    addressList = [x.strip() for x in addressList]
    addressList = [int(i) for i in addressList]

    for i in addressList:
        convertedList.append(ip_address(i))

    for x in convertedList:
        convertoutput.write("%s\n" % x)

decimalConverter(argv[1])
