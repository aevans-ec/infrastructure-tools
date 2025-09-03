import datetime
import random

def check_status():
    now = datetime.datetime.now()
    status = random.choice(["OK", "WARN", "FAIL"])
    print(f"[{now}] System status: {status}")

if __name__ == "__main__":
    check_status()
