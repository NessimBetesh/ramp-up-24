import redis
import json

def message_handler(message):
    print(f"Received: {json.loads(message['data'])}")

r = redis.Redis(host='redis', port=6379, db=0)
p = r.pubsub()
p.subscribe(**{'channel': message_handler})

print("Subscriber is running...")
p.run_in_thread(sleep_time=1)