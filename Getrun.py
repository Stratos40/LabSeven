from netmiko import ConnectHandler
import getpass
import os
import datetime
from netmiko.ssh_exception import AuthenticationException, SSHException, NetMikoTimeoutException

    
usern = input("Please enter a username: ")
cred = getpass.getpass(prompt='Please enter a password: ')
address = input("Please enter the IP address of the router: ")
cisco = {'device_type': 'cisco_ios', 'host': address, 'username': usern, 'password': cred}
ext = ".txt."
now = datetime.datetime.now()
time = now.strftime("%Y-%m-%d")
filename = 'RunningConfig' + time + ext
try:
    netM = ConnectHandler(**cisco)
    output = netM.send_command("Show run")
    Grun = open(filename,"w")
    Grun.write(output)
except (AuthenticationException):
    print("An authentication error has occured connecting to " + cisco['host']) 
except(NetMikoTimeoutException):
    print("Connection Timeout.")
except(SSHException):
    print("An error occured when attempting to SSH into the device.")

"""
def Getrun():
    from netmiko import ConnectHandler
    import getpass
    import os
    import datetime
    usern = input("Please enter a username: ")
    cred = getpass.getpass(prompt='Please enter a password: ')
    address = input("Please enter the IP address of the router: ")
    cisco = {'device_type': 'cisco_ios', 'host': address, 'username': usern, 'password': cred}
    netM = ConnectHandler(**cisco)
    ext = ".txt."
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d")
    filename = 'RunningConfig' + time + ext
    output = netM.send_command("Show run")
    Grun = open(filename,"w")
    Grun.write(output)
Getrun()
"""
