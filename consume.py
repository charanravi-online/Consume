import numpy as np
import psutil

available_ram = 0
def get_available_ram():
    virtual_memory = psutil.virtual_memory()
    available_ram = virtual_memory.available / (1024 ** 3)  # Convert to gigabytes
    return available_ram


def consume_memory():

    data = np.random.rand(2**48)  # consume approximately 2 TB of RAM

def main():
    available_ram = get_available_ram()
    print(f"Available RAM: {available_ram:.2f} GB")
    try:
        while True:
            consume_memory()
    except MemoryError:
        print("Memory limit reached.")
    

if __name__ == "__main__":
    main()
