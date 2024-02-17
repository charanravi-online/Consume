import numpy as np

def consume_memory():
    data = np.random.rand(2**28)  # Creates an array with approximately 1 gigabyte of random data

def main():
    try:
        while True:
            consume_memory()
    except MemoryError:
        print("Memory limit reached.")

if __name__ == "__main__":
    main()
