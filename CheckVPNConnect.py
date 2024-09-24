import subprocess

def is_vpn_running():
    try:
        # Run netstat command to check routing table
        output = subprocess.check_output("scutil --nc list", shell=True).decode()
        # Look for specific VPN routes or identifiers
        if "(Connected)" in output:
            return True
    except Exception as e:
        print(f"Error: {e}")
    return False

if __name__ == "__main__":
    if is_vpn_running():
        print("VPN is running.")
    else:
        print("VPN is not running.")
