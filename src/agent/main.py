#!/usr/bin/env python3
from agent.metrics_collector import collect_cpu, collect_memory
import time

def run():
    while True:

        cpu = collect_cpu()
        memory = collect_memory()

        print(f"CPU: {cpu}%")
        print(f"Memory: {memory}%")

        time.sleep(5)

if __name__ == "__main__":
    run()