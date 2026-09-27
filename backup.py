from netmiko import ConnectHandler

devices = [{"device_type":"cisco_xe", "host":"devnetsandboxiosxec8k.cisco.com", "username":"ADD_YOUR_USERNAME", "password":"ADD_YOUR_PASSWORD"}]

for device in devices:
    try:
        connection = ConnectHandler(device_type=device.get("device_type"), host=device.get("host"), username=device.get("username"), password=device.get("password"))
        prompt = connection.find_prompt()[:-1]
        running_configuration = connection.send_command("show running-config")
        try:
            with open(f"{prompt}_backup.txt", 'w') as file:
                file.write(str(running_configuration))
            print(f"---------------------- RUNNING CONFIGURATION ({prompt}) ----------------------\n" + str(running_configuration))
        except Exception as e: print(e)
    except Exception as e: print(e)