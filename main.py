import sys

def main():
    path_to_file = "books/frankenstein.txt"
    # path_to_file = "books/text.txt"
    file_contents = get_text(path_to_file)
    word_list = get_word_count(file_contents)
    word_count = len(word_list)
    
    count = char_count(file_contents)

    report = f"--- Begin report of {path_to_file} ---\n{word_count} words found in document\n"
    for i in count:
        num = count[i]
        message = f"The '{i}' char occurs {count[i]} times"
        print(message)
    print("--- End report ---")

def get_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return words

def char_count(file_text):
    # counts char appearance in words for each char in received
    chars_match = "abcdefghijklmnopqrstuvwxyz"
    symbols = ["'", '"', "\\n", ",", ".", " "]
    count = {}
    new_percentage = 0
    for i in chars_match:
        char_occurrence = 0
        for j in file_text:
            if j.lower() == i:
                char_occurrence += 1
            count[i] = char_occurrence
        percentage = round((len(count) / (len(chars_match)+len(symbols))) * 100)
        if percentage > new_percentage:
          new_percentage = percentage
          progress_bar = percentage * "#"
          
          print(f"[{progress_bar}] | {percentage}%", end="\r")
    print(f"{progress_bar} | 100%")
    return count


if __name__ == "__main__":
    main()
    