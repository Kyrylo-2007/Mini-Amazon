import json
import os

def load_data(filename, default):
    try:
        if not os.path.exists(filename):
            return default
        with open(filename, "r") as f:
            return json.load(f)
    except Exception as e:
        print("Error loading file:", e)
        return default
    
def save_data(filename, data):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("Error saving file:", e)