import time
import json
import const
import socket
from machine import Pin
from wifi import brute_connect
from dark_html import serve_html

brute_connect()
# constants
rad = const.rad # in meters
PinNum = const.PinNum
DELAY=const.DELAY
sensor_pin = Pin(PinNum, Pin.IN)

CONFIG_FILE = const.CONFIG
def load_config():
    """loads the configuration from JSON file"""
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def save_config(data):
    """save the configuration to the JSON file."""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(data, f)
        
stats =load_config() 
last_save_time = time.time()  # track the last save time
current_total_distance = 0 # distance of current bicycle session
current_total_time = 0 # duration of current bicycle session
last_time = time.ticks_us()  # init last_time to the current time in microseconds



# Create a simple web server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr[:2])
s.listen(1)

def get_ride_statistics():
    return stats

try: 
    while True:
        past_sensor_reading = sensor_pin.value()
        
        if past_sensor_reading == 1 and sensor_pin.value() == 0:
            
            
            current_total_distance += 2 * const.pi * rad # total distance update
            stats["total_distance"]+= 2 * const.pi * rad
            
            
            current_time_us = time.ticks_us() #time elapsed in microsecs
            time_elapsed_us = time.ticks_diff(current_time_us, last_time)  # diff in microsecs
            
            
            time_elapsed = time_elapsed_us / 1_000_000  # microseconds ==> seconds
            current_total_time += time_elapsed #total time update
            stats["total_riding_time"] += time_elapsed
        
            speed = (2 * const.pi * rad) / (time_elapsed-DELAY)   # speed in ms^-1
            
            
            last_time = current_time_us # update last_time to current_time
            
            # print(optional)
            print(f"Total Distance: {current_total_distance:.2f} m, Speed: {speed:.2f} m/s")
            
            # delay to prevent rapid counting
            time.sleep(DELAY)
            
            
        # auto-save every 10secs
        current_time = time.time()
        if current_time - last_save_time >= 5:
            print("Saving files")
            print(stats)
            save_config(stats)
            last_save_time = current_time
            
            cl, addr = s.accept()
            print('Client connected from', addr)
            request = cl.recv(1024)
            request = str(request)

            if '/stats' in request:
                # Return JSON data for ride statistics
                stats = get_ride_statistics()
                print(stats)
                response = 'HTTP/1.0 200 OK\r\nContent-Type: application/json\r\n\r\n'
                response += str(stats).replace("'", '"')  # Convert single quotes to double quotes for JSON
                cl.send(response.encode())
            else:
                # Serve the HTML page
                response = 'HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n'
                response += serve_html()
                cl.send(response.encode())

            cl.close()
            
            

except KeyboardInterrupt:
    # save details in case of EXCEPTION
    save_config(stats)
    
except Exception as e:
    # save details in case of EXCEPTION
    save_config(stats)

finally:
    stats["total_rides"]+=1
    save_config(stats)


