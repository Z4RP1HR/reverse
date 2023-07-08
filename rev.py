import socket

def ip_to_domain(ip_address):
    try:
        domain_name = socket.gethostbyaddr(ip_address)[0]
        return domain_name
    except socket.herror:
        return "Domain name not found"
    except socket.gaierror:
        return "Invalid IP address"

# Test the function
ip_address = input("Enter an IP address: ")
domain = ip_to_domain(ip_address)
print("Domain name: " + domain)
