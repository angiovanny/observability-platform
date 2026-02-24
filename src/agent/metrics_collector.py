import psutil

def collect_cpu():
    return psutil.cpu_percent(interval=1)

def collect_memory():
    memory = psutil.virtual_memory()
    return memory.percent