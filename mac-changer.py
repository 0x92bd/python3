#!/usr/bin/python3

import subprocess
import optparse
import re


# get user arguments
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more information.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC address, use --help for more information.")
    return options


# main function for changing mac address for given interface
def change_mac(interface, new_mac):
    print("[+] Changing MAC address for {0} to {1}".format(interface, new_mac))
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


# get current MAC address from ifconfig output
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


# call get_arguments function and store the value to variable that user enters
options = get_arguments()

# print current MAC address of given interface
current_mac = get_current_mac(options.interface)
print("Current MAC of {0} = {1}".format(options.interface, current_mac))

# call change_mac function to change the MAC address
change_mac(options.interface, options.new_mac)

# check if the current MAC is changed to the users requested MAC
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address of {0} was successfully changed to {1}".format(options.interface, current_mac))
else:
    print("[-] MAC address of {0} was not changed.".format(options.interface))

