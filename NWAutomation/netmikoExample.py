"""
Log into the router and fetch some information:

    task1(): Show the version, show the IP in brief, show the clock, and show the configured usernames on the router.
    task2(): Create another username on the test router with the password test and check whether we can log in successfully with the newly created username.
    task3(): Log in with the newly created username test, and delete all the other usernames from the running-config. Once this is done, return all the current usernames configured on the router to confirm whether only the test username is configured on the router.

"""

from netmiko import ConnectHandler

device = ConnectHandler(device_type='cisco_ios',
                        ip='192.168.255.249', username='cisco', password='cisco')


def displayInfo():
    output = device.send_command("show version")
    print(output)
    output = device.send_command("show ip int brief")
    print(output)
    output = device.send_command("show clock")
    print(output)
    output = device.send_command("show running-config | inc username")
    output = output.splitlines()
    for line in output:
        if 'username' in line:
            line_item = line.split(' ')
            print('username configured: ', line_item[1])


def addUser():
    global device
    configcmds = ["username test privilege 15 secret test"]
    device.send_config_set(configcmds)
    output = device.send_command('show running | inc username')
    output = output.splitlines()
    for line in output:
        if 'username' in line:
            line_item = line.split(' ')
            print('username configured: ', line_item[1])
    device.disconnect()

    try:
        device = ConnectHandler(device_type='cisco_ios',
                                ip='192.168.255.249', username='test', password='test')
        print('Authenticated successfully with username test')
        device.disconnect()
    except:
        print('Unable to authenticate with username test')


def modifyUser():
    device = ConnectHandler(device_type='cisco_ios',
                            ip='192.168.255.249', username='test', password='test')
    output = device.send_command('show running | inc username')

    output = output.splitlines()
    for line in output:
        if 'username' in line:
            if 'test' not in line:
                line_item = line.split(' ')
                cmd = 'no username ' + line_item[1]
                send_cmd = device.send_config_set(cmd)

    output = output.splitlines()
    for line in output:
        if 'username' in line:
            line_item = line.split(' ')
            print('username configured: ', line_item[1])
    device.disconnect()
