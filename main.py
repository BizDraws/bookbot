def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted = sort(chars_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    for item in sorted:
        print(f"The '{item['character']}' was found {item['num']} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def sort_on(d):
    return d["num"]
    
    
def sort(dict):

    report = []

    for chars in dict:
        if chars.isalpha():
            cha_dict = {"character": chars, "num": dict[chars]}
            report.append(cha_dict) 
    
    report.sort(reverse = True, key = sort_on)

    return report



    
#WORD COUNT
    #words = file_contents.split()
    #print (len(words))

    #LOWER CASE AND CHARACTER COUNT
    #characters = {}
    #lower_case = file_contents.lower()

    #for char in lower_case:
    #    if char not in characters:
    #        characters[char] = 1
    #    else:
    #        characters[char] += 1
            

main()  