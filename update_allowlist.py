"""
Security Automation Script: IP Allowlist Updater
Author: Thitsadaphone (Yayee) Phiakeo
Description: Reads an IP allowlist file, removes unauthorized IP addresses
             listed in a remove_list, and updates the allowlist file automatically.
"""

def update_allowlist(import_file, remove_list):
    # Open and read the current allowlist file
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    # Convert the string of IP addresses into a list
    ip_list = ip_addresses.split()

    # Iterate through the remove_list and remove matching IPs
    for element in remove_list:
        if element in ip_list:
            ip_list.remove(element)
            print(f"[INFO] Removed unauthorized IP: {element}")

    # Convert the updated list back into a newline-separated string
    updated_ips = "\n".join(ip_list)

    # Write the updated IP list back to the original file
    with open(import_file, "w") as file:
        file.write(updated_ips)
    
    print("[SUCCESS] IP allowlist has been successfully updated.")

# Example execution
if __name__ == "__main__":
    allow_file = "allow_list.txt"
    unauthorized_ips = ["192.168.97.225", "192.168.158.170", "192.168.201.40"]
    update_allowlist(allow_file, unauthorized_ips)
