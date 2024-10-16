with open("/home/base8314/workspace/github.com/base8314/bookbot/books/frankenstein.txt") as f:
    file_contents = f.read()

def word_count(file_string):
    #Main function
    #inputs = .txt file
    #Returns # of words in the file    
    word_text = file_string.split()
    return(len(word_text))



def character_count(character_string):
    #Character count function
    #input = string
    #Returns Key sorted dictionaray of {character : Count}
    char_count={}
    for char in character_string.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char]= char_count[char] + 1

    sorted_char_count = dict(sorted(char_count.items()))
    return(sorted_char_count)    


def report_print(sorted_dict_count):
    #Prints to console
    #inputs = sorted dictionary of character counts
    #returns = None
    print("--- Begin report of books/frankenstein.txt ---")
    print("%d words found in the document" %(word_count(file_contents)))
    print("\n")
    
    for key, value in (sorted_dict_count).items():
        if key == "\n":
            pass
        else:
            print("The '%s' character was found %d times" %(key,value))
    print("---End Report---")


report_print(character_count(file_contents))
