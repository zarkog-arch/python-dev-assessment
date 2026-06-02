def filter_and_sort_evens(numbers):
    evens = [num for num in numbers if num % 2 == 0]
             return sorted(evens)



def count_character_frequency(text):
       frequency = {}
       for char in text.lower():
              frequency[char] = frequency.get(char, 0) + 1
              return frequency


if __name__ == _main_
    sample_numbers = [3, 1, 4, 7, 1, 5, 9, 2, 6, 8]
    sorted_evens = filter_and_sort_evens(semple_numbers)
    print(f"Original list: {sample_numbers}")
    print(f"Filterd and sorted evens: {sorted_evens}")
    print("-* 40")


    sample_text = "This my task for Basic Data Structures & Algorithms"
    char_freq = count_character_frequency(sample_text)
    print(f"Original text: '{sample_text}'")
    print(f"Character frequency: {char_freq}")


