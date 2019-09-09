import time
from datetime import datetime as dt

"""
Website Blocker on work ours.

For windows:
- Rename with *.pyw and execute as administrator
- Use task scheduler of windows and create a startup task

For linux:
- use crontab*
- Add @reboot python3 /path/to/script/*.py
"""
linux_hosts = "/etc/hosts"
windows_hosts = r"C:\Windows\System32\drivers\etc\hosts"

website_list = ["www.facebook.com", "www.reddit.com"]
redirect = "127.0.0.1"


host_location = windows_hosts
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 1) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours...")
        with open(host_location, 'r+') as h_files:
            contents = h_files.read()
            for website in website_list:
                if website not in contents:
                    h_files.writelines(f"{redirect}\t{website}\n")

    else:
        with open(host_location, 'r+') as h_files:
            contents = h_files.readlines()
            h_files.seek(0)
            for line in contents:
                if not any(website in line for website in website_list):
                    h_files.write(line)
            h_files.truncate()
        print("Fun hours...")
    time.sleep(5)
