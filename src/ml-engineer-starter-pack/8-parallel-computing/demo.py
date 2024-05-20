import multiprocessing
import numpy as np
import time

ARRAY_SIZE = int(1e7)

# Define the number of processes to create
# NUM_CORES = multiprocessing.cpu_count()
NUM_CORES = 1


# Function to perform some computation
def compute_square(number):
    return number * number


if __name__ == "__main__":
    t0 = time.time()

    # Create a pool of processes
    pool = multiprocessing.Pool(processes=NUM_CORES)

    # Define a list of numbers
    numbers = np.random.randn(ARRAY_SIZE)

    # Map the compute_square function to the list of numbers
    results = pool.map(compute_square, numbers)

    # Close the pool to release resources
    pool.close()

    print(f"Complete in {time.time() - t0} seconds (using {NUM_CORES} cores)")
