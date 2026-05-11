import pandas as pd
import random
from datetime import datetime

def generate_logs():

    senders = [
        "admin@gmail.com",
        "unknown@gmail.com",
        "spam@gmail.com",
        "employee@company.com",
        "hacker@xyz.com"
    ]

    receivers = [
        "user1@gmail.com",
        "user2@gmail.com",
        "user3@gmail.com",
        "user4@gmail.com"
    ]

    logs = []

    for i in range(10):

        log = {
            "sender": random.choice(senders),
            "receiver": random.choice(receivers),
            "failed_login": random.randint(0, 10),
            "attachments": random.randint(0, 5),
            "ip": f"192.168.1.{random.randint(1,255)}",
            "time": datetime.now()
        }

        logs.append(log)

    return pd.DataFrame(logs)
