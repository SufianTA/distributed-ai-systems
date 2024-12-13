# distributed-ai-systems/distributed_example.py

import ray

# Initialize Ray for distributed computing
ray.init()

# Example remote function
@ray.remote
def compute_square(x):
    return x * x

# Run distributed tasks
results = ray.get([compute_square.remote(i) for i in range(10)])
print(results)
