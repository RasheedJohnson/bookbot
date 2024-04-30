import sys

def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_text(path_to_file)
    word_list = get_word_count(file_contents)
    word_count = len(word_list)
    
    
    if sys.argv[1] == None:
        user_input == "arg"
    else:
        user_input = sys.argv[1]
        
    characters = char_count(user_input, file_contents)
    collection = f"Word count: {word_count}\ntext character count: {characters}"
    print(collection)

def get_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return words

def char_count(received, words):
    # counts char appearance in words for each char in received
    count = {}
    for i in received:
      i_count = 0
      for j in words:
        if j.lower() == i:
          i_count += 1
      count[i] = i_count
    
    return count


if __name__ == "__main__":
    main()
    