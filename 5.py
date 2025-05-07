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
