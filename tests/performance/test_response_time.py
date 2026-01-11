import time
import requests

def test_response_time():
    start = time.time()
    requests.get("http://localhost:5000/health")
    elapsed = time.time() - start
    assert elapsed < 0.5
