import subprocess


def device_selection():
    """
    The function checks for connected devices
    :return: transport_id
    """
    list_devices = subprocess.run(["adb", "devices", "-l"], stdout=subprocess.PIPE)
    list_devices = str(list_devices.stdout).split('\\n')
    device_count = 0
    devices_dict = dict()
    for index in range(len(list_devices)):
        if str(list_devices[index]).find("transport_id:") != -1 and str(list_devices[index]).find("product:"):
            device_count = device_count + 1
            temp = str(list_devices[index]).split(":")

            devices_dict[device_count] = {
                'transport_id': temp[len(temp) - 1],
                'product': temp[len(temp) - 4].split(' ')[0]
            }

            tr_id = "-t" + str(devices_dict[device_count]['transport_id'])
            print(device_count, list_devices[index])

    if device_count == 0:
        print("No connected devices")
        quit()
    elif device_count > 1:
        current_device = int(input("Choose device: "))
        tr_id = "-t" + str(devices_dict[current_device]['transport_id'])
        return tr_id
    else:
        return tr_id
