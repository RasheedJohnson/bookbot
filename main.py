import sys

def main():
    # path_to_file = "books/frankenstein.txt"
    path_to_file = "books/text.txt"
    file_contents = get_text(path_to_file)
    word_list = get_word_count(file_contents)
    word_count = len(word_list)
    
    char_count(file_contents)


def get_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return words

def char_count(file_text):
    # counts char appearance in words for each char in received
    chars_match = "abcdefghijklmnopqrstuvwxyz0123456789"
    symbols = ["'", '"', "\\n", ",", ".", " "]
    count = {}
    new_percentage = 0
    for i in file_text:
        i = i.lower()
        i_count = 0
        for j in file_text:
          if j.lower() == i:
            i_count += 1
        count[i] = i_count
        percentage = round((len(count) / (len(chars_match)+len(symbols))) * 100)
        if percentage > new_percentage:
          new_percentage = percentage
          progress_bar = percentage * "#"
          
          print(f"[{progress_bar}] | {percentage}%", end="\r")
    print(f"{progress_bar} | 100%")
    print(count)
    # return count


if __name__ == "__main__":
    main()
    