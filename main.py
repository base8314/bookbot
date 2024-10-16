def main():
    #Main function
    #inputs = .txt file
    #Returns # of words in the file
   


    with open("/home/base8314/workspace/github.com/base8314/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        
    word_text = file_contents.split()
    print(len(word_text))



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
    print(sorted_char_count)    

character_count(simple_string)

