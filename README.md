# 🔥 Smart-Home Fire, Smoke & CO Detection IoT System 🚨

> *Because your smart home deserves to smell danger before you do.*

![Smart Home Diagram](https://img.shields.io/badge/Smart%20Home-Diagram-blue)

---

## 🌟 Project Overview
Welcome to the ultimate Smart Home Safety Squad! This repo simulates a **fire/smoke/flame/CO detection** system using Cisco Packet Tracer and Python. Our goal? To detect danger early, alert the user with some sass, and maybe save your house — or at least your favorite snack stash.

---
## What’s Inside?

- **Cisco Packet Tracer simulation files** (`.pkt`) — Build your own smart home IoT network featuring sensors, gateways, and MQTT brokers.  
- **Python scripts** — Simulate sensor data, run detection algorithms, and sound hilarious alarms that’ll make you chuckle while you evacuate.  
- **Architecture diagrams** — Because who doesn’t love pretty pictures of networks?  
- **Project report** — Deep dive into methodology, security considerations, and future directions.

---

## How It Works: The Smart Smell Test 👃

1. Sensors (fire, smoke, CO) constantly sniff the air.  
2. Data is sent to a central IoT Gateway (simulated in Cisco).  
3. Python scripts analyze sensor data for dangerous thresholds.  
4. If danger is detected, alerts trigger with a cheeky message AND a real emergency notification.

---

## Technologies

| Component             | Tool/Tech               |
|-----------------------|------------------------|
| Network Simulation    | Cisco Packet Tracer      |
| Programming           | Python 3.x               |
| Messaging Protocol    | MQTT (conceptual)        |
| Alert System          | CLI alerts & logs        |

---

## Getting Started

### Cisco Packet Tracer Setup

- Open `cisco/smart_home_fire_iot_simulation.pkt` (coming soon!)  
- Devices include smart smoke detectors, CO sensors, smart lights, and the central gateway router.  
- Configure sensors using `configs/sensor_config.txt`.  
- Gateway config available at `configs/gateway_config.txt`.

> **Pro tip:** Sensors talk MQTT, so configure your broker accordingly!

### Python Simulation

```python
cd python
python3 fire_smoke_co_detector.py
---

---

## Step 2: Python Code — `fire_smoke_co_detector.py`



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

```





























