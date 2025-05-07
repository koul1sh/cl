def map_reduce(file_path, target_word):
    word_count = 0
    with open(file_path, 'r') as file:
        mapped_data = [(word.lower(), 1) for line in file for word in line.strip().split()]
    print(mapped_data)
        
    for word, count in mapped_data:
        if word == target_word.lower():
            word_count += count

    return word_count

file_path = 'input.txt'
target_word = "Dheeraj"

frequency = map_reduce(file_path, target_word)
print(f"The word '{target_word}' appears {frequency} times.")

"""-------------------------Parallel processing-------------------------"""
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

def mapper(line):
    mapped = []
    for ch in line:
        if ch.isalpha():
            a = (ch.lower(), 1)
            mapped.append(a)
    return mapped

def reducer(mapped):
    reduced = defaultdict(int)
    for (key, val) in mapped:
        reduced[key] += 1
    return reduced

def read_and_map(filename):
    with open(filename) as f:
        lines = f.readlines()
    mapped = []
    for line in lines:
        mapped += mapper(line)
    return mapped

def map_reduce():
    files = ["mapreduce_text1.txt", "mapreduce_text2.txt"]  # Use two different input files
    mapped = []

    with ThreadPoolExecutor() as executor:
        results = executor.map(read_and_map, files)

    for result in results:
        mapped += result

    return reducer(mapped)

# Output result
if __name__ == "__main__":
    result = map_reduce()
    for k, v in sorted(result.items()):
        print(f"{k}: {v}")
