import threading
import time

def checking_status():
    while True:
        print(f"Checking status ⌛")
        time.sleep(2)
t = threading.Thread(target=checking_status, daemon=True)
t.start()

print("Main Program Done")