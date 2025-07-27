"""
alert_simulator.py

A fun CLI program to simulate smart home alerts with a sense of humor.

Author: Meeeeee
"""

import time

alerts = [
    "[🔥 FIRE ALERT] Flames detected! Quick, grab the marshmallows! 🔥",
    "[😷 SMOKE ALERT] Smoke levels rising! Evacuate the snacks! 🚒",
    "[☠️ CO ALERT] CO detected! Time to air out the existential dread! 😱",
    "[✅ SAFE] All clear. Time for Netflix and chill. 🍿"
]

def simulate_alerts():
    print("Starting smart home alert simulator...\n")
    for alert in alerts:
        print(alert)
        time.sleep(3)
    print("\nEnd of simulation. Remember: Safety first, sass second!")

if __name__ == "__main__":
    simulate_alerts()
