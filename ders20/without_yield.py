import psutil
import os


def fetch_lines(file_name):
    with open(file_name, "r") as f:
        cntr = 0
        lines = []
        for line in f:
            lines.append(line)
            cntr+=1
            # Show memory usage periodically (e.g., every 1000 lines)
            if len(lines) % 1000 == 0:
                print(
                    f"Memory usage after reading {len(lines)} lines: {get_memory_usage()} MB"
                )
            if cntr == 500000:
                break
    return lines


def get_memory_usage():
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    return memory_info.rss / 1024 / 1024  # Convert from bytes to MB


print(f"Initial memory usage: {get_memory_usage()} MB")
file = fetch_lines("tl_usd_exchange_rate.csv")
print(f"Final memory usage: {get_memory_usage()} MB")
