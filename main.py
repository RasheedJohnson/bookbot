

def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_text(path_to_file)
    word_list = get_word_count(file_contents)
    word_count = len(word_list)
    print(word_count)

def get_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return words

if __name__ == "__main__":
    main()