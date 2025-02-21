import psutil
import os


def fetch_lines(file_name):
    with open(file_name, "r") as f:
        for line in f:
            yield line


def get_memory_usage():
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    return memory_info.rss / 1024 / 1024  # Convert from bytes to MB


file = fetch_lines("tl_usd_exchange_rate.csv")
print(f"Initial memory usage: {get_memory_usage()} MB")

for i in range(500000):  # line numbers
    print(next(file))

    # Show memory usage periodically (e.g., every 1000 lines)
    if i % 1000 == 0:
        print(f"Memory usage after {i} lines: {get_memory_usage()} MB")

# Show final memory usage
print(f"Final memory usage: {get_memory_usage()} MB")
