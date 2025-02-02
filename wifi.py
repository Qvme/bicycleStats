import json
import network
from time import sleep


def add_network(ssid, pwd):
    """To add new network details in json file"""
    already_exists = None
    buf = {"ssid": ssid, "password": pwd}
    
    with open("ssid.json", "r") as file:
        data = json.load(file)
        
    for network in data["WiFi_Networks"]:
        if network["ssid"] == ssid:
            already_exists = True
            
    if not already_exists:
        data["WiFi_Networks"].append(buf)
        with open("ssid.json", "w") as file:
            json.dump(data, file)


def remove_network(ssid):
    """To remove existing network details from json file"""
    del_index = None
    
    with open("ssid.json", "r") as file:
        data = json.load(file)
        
    for index, network in enumerate(data["WiFi_Networks"]):
        if network["ssid"] == ssid:
            del_index = index
            
    if del_index is not None:
        del data["WiFi_Networks"][del_index]
    with open("ssid.json", "w") as file:
        json.dump(data, file)


def brute_connect():
    """atttempts to connect networks from ssid.json file"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    with open("ssid.json", "r") as file:
        data = json.load(file)

        for network_info in data["WiFi_Networks"]:
            ssid = network_info["ssid"]
            password = network_info["password"]
            attempts = 0

            while attempts < 5:  # allow up to 5 attempts
                wlan.connect(ssid, password)
                print(f"attempting to connect to {ssid}")

                # Wait for connection
                while not wlan.isconnected() and attempts < 5:
                    print(f"trying to connect {attempts+1}th time...")
                    sleep(1)
                    attempts += 1

                if wlan.isconnected():
                    print(f"Connected to Wi-Fi: {ssid}, IP address: {wlan.ifconfig()[0]}")
                    return  # Exit the function after a successful connection

            print(f"Failed to connect to {ssid} after {attempts} attempts.")

    print("All networks attempted, no successful connection.")
    return -1
# Examples
# add_network("1984", "LcGG8eQu")
# remove_network("1984")
# brute_connect()
