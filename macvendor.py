import sys

if sys.version_info[0] < 3:
    raise Exception("Must be using Python(3) or greater!!")

from urllib.request import urlopen

mac = input("Enter the mac address: ")
vendor = urlopen(str("https://api.macvendors.com/"+mac))
print("Vendor: {}".format(vendor.read().decode('utf-8')))
