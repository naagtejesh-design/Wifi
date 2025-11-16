import json
import os

def save_wifi_info(ssid, password):
    data = {"ssid": ssid, "password": password}
    folder = os.path.join(os.getcwd(), 'wifi_data')
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, 'saved_wifi.json')
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            all_data = json.load(f)
    else:
        all_data = []
    all_data.append(data)
    with open(file_path, 'w') as f:
        json.dump(all_data, f)