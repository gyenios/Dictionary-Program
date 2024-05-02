import concurrent.futures
from gtts import gTTS
from playsound import playsound
import os

# Function to read a file into a hash table
def read_file_into_hash_table(file_name):
    hash_table = {}
    indices = {}
    line_number = 1

    def process_line(line):
        nonlocal line_number
        parts = line.strip().split(' : ', 1)
        if len(parts) == 2:
            word, meaning = parts
            hash_table[word] = meaning
            # Store the line number for this word
            indices[word] = line_number
        else:
            print(f"Invalid line format at line {line_number}")
            print(len(parts), 'parts')
        # Increment the line number for the next line
        line_number += 1

    with open(file_name, 'r', encoding='utf-8-sig') as file:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(process_line, line) for line in file]
            concurrent.futures.wait(futures)
    return [hash_table, indices]

# Class representing a dictionary
class Dictionary:
    def __init__(self):
        self.words,self.indices = read_file_into_hash_table("words.txt")

    def add_word(self, word, definition):
        word = word.title()
        if word in self.words:
            return 'Word already in dictionary. Not added'
        else:
            # Add word and definition to dictionary
            self.words[word] = definition

    def update_word(self, word, new_definition):
        word = word.title()
        if word in self.words:
            # Update definition in the dictionary
            self.words[word] = new_definition
            return "Word updated successfully"
        else:
            return "Word not found in the dictionary."

    def delete_word(self, word):
        word = word.title()
        if word in self.words:
            # Delete from dictionary
            del self.words[word]
            return f"{word} deleted successfully"
        else:
            return f"Word '{word}' not found in the dictionary."

    def find_definition(self, word):
        # Transform the word to title case for consistency
        word = word.title()
        if word in self.words:
            return self.words[word]
        else:
            return "Word not found in the dictionary."

    def suggest_similar_words(self, partial_word):
        similar_words = [word for word in self.words.keys() if partial_word in word]
        return similar_words

    def to_Speech(self, word, definition):
        if definition == "Word not found in the dictionary.":
            output = definition
        else:
            output = f'{word},is defined as, {definition}'
        tts = gTTS(output, lang='en')
        tts.save('output.mp3') # Save the speech to an audio file
        playsound('output.mp3') # Play the audio using playsound

        # Delete the audio file after playing
        os.remove('output.mp3')
        
# Class representing a menu
class Menu:
    @staticmethod
    def display_menu():
        print('''
            Choose an option:
            [1] Search for a word
            [2] Add new word
            [3] Update a word
            [4] Delete a word
            [5] Suggest similar words
            [6] Exit
            ''')

    @staticmethod
    def get_word_definition(option, dictionary):    
        word = input("Enter word: ")
        if option == 2 or option == 3:
            meaning = input("Meaning of word: ")
            if option == 2:
                dictionary.add_word(word.title(), meaning)
            elif option == 3:
                dictionary.update_word(word, meaning)
        elif option == 1:
            definition = dictionary.find_definition(word)
            print(definition)
            # dictionary.to_Speech(definition)
        elif option == 4:
            dictionary.delete_word(word)
        elif option == 5:
            similar = dictionary.suggest_similar_words(word)
            for i in similar:
                print(i)

# Function to handle the user's choice to exit or continue
def Choice():
    print('''
Would you want to exit?
[1] Yes
[2] No
''')
    while True:
        option = int(input(">> "))
        try:
            if option == 1 or option == 2:
                if option == 1:
                    break
                else:
                    main()
            else:
                print("Enter 1 or 2")
        except ValueError:
            print("Invalid response. Enter an integer 1 or 2")

# Function to write dictionary contents to a file
def write_dictionary_to_file(dictionary, file_name, buffer_size=10000):
    with open(file_name, 'w', encoding='utf-8') as file:
        buffer = []  # Buffer to accumulate key-value pairs
        for word, meaning in dictionary.items():
            buffer.append(f"{word} : {meaning}\n")
            if len(buffer) >= buffer_size:
                # Write the buffer contents to the file
                file.writelines(buffer)
                buffer = []  # Clear the buffer
        # Write any remaining contents in the buffer to the file
        if buffer:
            file.writelines(buffer)

# Main function to run the program
def main():
    dictionary = Dictionary()
    try:
        while True:
            Menu.display_menu()
            option = int(input('>> '))
            if option == 6:
                print("Exiting...")
                break  # Exit the loop and naturally exit the program
            while True:
                if option >= 1 and option <= 6:
                    Menu.get_word_definition(option, dictionary)
                    break
                else:
                    print('Invalid response. Enter an integer 1-5')
                    option = int(input('>> '))
    finally:
        # Write the dictionary contents to the file before exiting
        write_dictionary_to_file(dictionary.words, "words.txt")
        return

# Entry point of the program
if __name__ == "__main__":
    main()
    Choice()
