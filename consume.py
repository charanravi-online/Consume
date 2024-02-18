"""
# ⚠️ WARNING 

When consume.py is run, a complex calculation is performed which utilises around 2TB of system RAM.
Some of the basic operations are temporarily down since the demand for RAM would be so high. 
Any normal user in their right mind would not have over 2TB of RAM installed, so use this with caution.
Although not harmful, it may cause some damage to the system and I take no reponsibility for it.
This is for research and education purpose only. Use it at your own risk.

"""
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


"""
# ⚠️ WARNING 

When consume.py is run, a complex calculation is performed which utilises around 2TB of system RAM.
Some of the basic operations are temporarily down since the demand for RAM would be so high. 
Any normal user in their right mind would not have over 2TB of RAM installed, so use this with caution.
Although not harmful, it may cause some damage to the system and I take no reponsibility for it.
This is for research and education purpose only. Use it at your own risk.

"""