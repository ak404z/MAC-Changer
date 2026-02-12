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
