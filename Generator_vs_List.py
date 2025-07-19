import time
import sys

n = 10**6  # 1 million

# List Comprehension
def list_even_numbers(n):
    return [i for i in range(n) if i % 2 == 0]

# Generator Expression
def generator_even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

# Using list
start_list = time.time()
list_result = list_even_numbers(n)
list_time = time.time() - start_list
list_memory = sys.getsizeof(list_result)
print(f"List: Time = {list_time:.4f}s, Memory = {list_memory} bytes")

# Using generator
start_gen = time.time()
gen_result = generator_even_numbers(n)
gen_time = time.time() - start_gen
gen_memory = sys.getsizeof(gen_result)
print(f"Generator: Time = {gen_time:.4f}s, Memory = {gen_memory} bytes")
