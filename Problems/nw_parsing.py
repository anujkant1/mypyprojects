"""
Parsing and counting items from a long list:
Given a list of network device names, device_list = ["IO", "IC", "MAD08S06", "TG", "FJR02S08", "LAX17S38", "IH", "FRA03(pop)"...], 
1. write a function to retrun all the devices with pattern "[3-letter][2-digit][1-letter][2-digit]", e.g. "FJR02S08". Please write the regex first and write the function to return the matched device.
2. then, given the 1-letter in the pattern is a device type character for the device, we have multiple types of device, find how many devices of each distinctive type
"""
import re

device_list = ["IO", "IC", "MAD08S06", "TG", "FJR02S08", "LAX17S38", "MAA01R03", "IH", "SIN04R02", "FJR02F08"]

DEVICE_REGEX = re.compile(r'^([A-Z]{3})(\d{2})([A-Z])(\d{2})$')



def find_devices(device_names):
    """Return device names matching the required pattern."""
    return [device for device in device_names if DEVICE_REGEX.fullmatch(device)]


def count_device_types_mapped(device_names):
    """Count how many devices belong to each device type."""
    device_dict = {
        'router': 0,
        'switch': 0,
        'unclassified': []
        }

    for device in find_devices(device_list):
        match_obj = DEVICE_REGEX.fullmatch(device)
        if match_obj.group(3).lower() == 'r':
            device_dict['router'] += 1
        elif match_obj.group(3).lower() == 's':
            device_dict['switch'] += 1
        else:
            device_dict['unclassified'].append(device)

    return device_dict


print(find_devices(device_list))
print(count_device_types_mapped(device_list))