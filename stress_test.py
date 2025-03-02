import multiprocessing
import random

def is_prime(n):
    """Check if a number is prime (CPU-intensive task)."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes():
    """Continuously generate prime numbers to stress the CPU."""
    num = random.randint(10**5, 10**6)
    while True:
        num += 1
        if is_prime(num):
            pass  # Keep computing primes

def stress_cpu(cpu_load):
    """Stress CPU by spawning multiple processes."""
    processes = []
    for _ in range(cpu_load):
        p = multiprocessing.Process(target=generate_primes)
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()

if __name__ == "__main__":
    cpu_cores = multiprocessing.cpu_count()
    print(f"🖥️ Detected {cpu_cores} CPU cores. Launching stress test...")
    
    stress_cpu(cpu_cores)  # Utilize all CPU cores
