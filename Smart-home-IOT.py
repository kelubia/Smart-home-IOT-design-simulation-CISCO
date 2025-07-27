
---

## Step 2: Python Code — `fire_smoke_co_detector.py`

```python
"""
fire_smoke_co_detector.py

Simulates sensor readings for fire, smoke, and CO levels and triggers alerts.
Because a smart home without sass is just a boring home.

Author: Kitten (your friendly neighborhood code wizard)
"""

import random
import time

# Thresholds for danger levels (arbitrary units)
SMOKE_THRESHOLD = 70
FIRE_THRESHOLD = 80
CO_THRESHOLD = 50

def get_sensor_readings():
    """
    Randomly generate sensor readings to simulate real data.
    Returns a dictionary with levels of smoke, fire, and CO.
    """
    return {
        "smoke": random.randint(0, 100),
        "fire": random.randint(0, 100),
        "co": random.randint(0, 100)
    }

def analyze_readings(readings):
    """
    Analyze sensor data against thresholds and decide alert level.
    Returns alert messages with witty remarks.
    """
    alerts = []

    if readings["fire"] >= FIRE_THRESHOLD:
        alerts.append("[🔥 FIRE ALERT] Flames detected! Time to fry marshmallows elsewhere! 🔥")
    if readings["smoke"] >= SMOKE_THRESHOLD:
        alerts.append("[😷 SMOKE ALERT] Smoke levels high! Evacuate the snacks, I mean the house! 🚒")
    if readings["co"] >= CO_THRESHOLD:
        alerts.append("[☠️ CO ALERT] Carbon monoxide detected! Open all windows and hold your breath! 😱")

    if not alerts:
        alerts.append("[✅ SAFE] All clear. You can chill and binge your favorite shows. 🍿")

    return alerts

def main():
    print("Smart-Home Fire/Smoke/CO Detection System v1.0")
    print("Press Ctrl+C to exit.\n")

    try:
        while True:
            sensor_data = get_sensor_readings()
            print(f"Sensor Readings: Fire={sensor_data['fire']} Smoke={sensor_data['smoke']} CO={sensor_data['co']}")

            alerts = analyze_readings(sensor_data)
            for alert in alerts:
                print(alert)

            print("\nSleeping for 5 seconds before next check...\n")
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nExiting. Stay safe and sassy!")

if __name__ == "__main__":
    main()
