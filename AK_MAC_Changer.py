#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ===============================================================
#  AK Software License v1.0
#  Copyright (c) 2025 AK (ak404z)
#
#  This software is provided for educational and research purposes
#  only. You are NOT allowed to use this code for:
#      - Illegal activities
#      - Harming individuals or organizations
#      - Unauthorized access or data breaches
#
#  By using this software, you agree that:
#      - The author is not responsible for any misuse.
#      - The tool is provided "AS IS" without any warranty.
#      - You assume full responsibility for any consequences.
#
#  You may modify and redistribute this code ONLY with proper
#  credit to the original author (AK / ak404z).
#
#  Unauthorized commercial use is strictly prohibited.
# ===============================================================
import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="network_interface", help="This place is for Network Interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="This place is for MAC Address")
    options, arguments = parser.parse_args()

    if not options.network_interface:
       parser.error("[-] Specify an Network Interface please, type -h for help")

    if not options.new_mac:
        parser.error("[-] Specify MAC Address, type -h for help")

    return options

def mac_changer(network_interface, new_mac):
    subprocess.call("ifconfig " + network_interface + " down", shell=True)
    subprocess.call("ifconfig " + network_interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + network_interface + " up", shell=True)
    print("[+] Changing MAC Address for " + network_interface + " to " + new_mac)

def get_mac(network_interface):
    ifconfig_result = subprocess.check_output("ifconfig " + network_interface, shell=True).decode("UTF-8")
    mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    return mac_address[0]

options = get_arguments()
mac_changer(options.network_interface, options.new_mac)
mac_address = get_mac(options.network_interface)

if mac_address == options.new_mac:
    print("[+] MAC address has changed successfully to " + options.new_mac)
else:
    print("Something went wrong...")
