def is_valid_ip_address(ip_address):
    octets = ip_address.split(".")
    if len(octets) != 4:
        return False

    for octet in octets:
        # Check for leading zeroes
        if len(octet) > 1 and octet.startswith("0"):
            return False

        value = int(octet)
        if value < 0 or value > 255:
            return False

    return True

def determine_ip_class(first_octet):
    if 0 <= first_octet <= 127:
        print("Class: A")
    elif 128 <= first_octet <= 191:
        print("Class: B")
    elif 192 <= first_octet <= 223:
        print("Class: C")
    elif 224 <= first_octet <= 239:
        print("Class: D (Multicast)")
    elif 240 <= first_octet <= 255:
        print("Class: E (Reserved)")

def determine_ip_type(ip_address):
    octets = ip_address.split(".")
    first_octet = int(octets[0])
    last_octet = int(octets[3])

    if first_octet == 0 or first_octet == 127 or last_octet == 0 or last_octet == 255:
        print("Type: Reserved")
    elif 224 <= first_octet <= 239:
        print("Type: Multicast")
    elif last_octet == 255:
        print("Type: Broadcast")
    else:
        print("Type: Unicast")

def main():
    ip_address = input("Enter an IP address: ")

    if is_valid_ip_address(ip_address):
        octets = ip_address.split(".")
        first_octet = int(octets[0])
        determine_ip_class(first_octet)
        determine_ip_type(ip_address)
    else:
        print("Invalid IP address format.")

if __name__ == "__main__":
    main()