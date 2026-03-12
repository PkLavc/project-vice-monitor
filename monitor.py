import requests
import datetime

URL = "https://pklavc.github.io/"

def check():
    try:
        start = datetime.datetime.now()
        r = requests.get(URL, timeout=10)
        latency = (datetime.datetime.now() - start).total_seconds() * 1000
        status = "ONLINE" if r.status_code == 200 else f"OFFLINE ({r.status_code})"
        log = f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {URL} | {status} | {latency:.2f}ms\n"
    except Exception as e:
        log = f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {URL} | ERROR: {str(e)}\n"
    
    with open("uptime_log.txt", "a") as f:
        f.write(log)

if __name__ == "__main__":
    check()
