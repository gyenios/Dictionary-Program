# Dictionary Application

## Description
This Python program provides a dictionary interface that allows users to manage a list of words and their definitions. It consists of two main components: a command-line interface (CLI) for managing the dictionary data and a graphical user interface (GUI) for interacting with the dictionary visually.
This program uses a dataset of 50 words and their meanings written in a txt file, however the read and write functions are efficient for large datasets, having the same formatting as the sample text file.

## Features
- **Command-Line Interface (CLI):**
  - Add new words with definitions.
  - Update existing word definitions.
  - Delete words from the dictionary.
  - Search for word definitions.
  - Suggest similar words based on partial input.
  - Convert word definitions to speech.

- **Graphical User Interface (GUI):**
  - Provides a user-friendly interface for interacting with the dictionary.
  - Allows users to perform CRUD (Create, Read, Update, Delete) operations on dictionary entries.
  - Displays word definitions in a text area.
  - Supports adding, updating, and deleting words through popup dialogs.
  - Offers a dropdown menu for additional options like adding, deleting, and updating words.

## Dependencies
- Python 3.x
- `concurrent.futures`
- `gtts` (Google Text-to-Speech)
- `playsound`
- `tkinter` (for GUI)

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/gyenios/dictionary_application.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd dictionary_application
   ```
3. **Install the required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
- **CLI:**
  - Run the program by executing `main.py` in the command-line interface.
  - Follow the on-screen prompts to interact with the dictionary.
- **GUI:**
  - Run the program by executing `ui.py`.
  - Use the graphical interface to perform dictionary operations.

## Concepts and Functions
- **Dictionary Class:**
  - Represents a dictionary with methods to manage words and their definitions.
    - `add_word()`: Adds a new word and its definition.
    - `update_word()`: Updates the definition of an existing word.
    - `delete_word()`: Deletes a word from the dictionary.
    - `find_definition()`: Searches for the definition of a word.
    - `suggest_similar_words()`: Suggests similar words based on a partial input.
    - `to_Speech()`: Converts text to speech using Google Text-to-Speech.
- **Menu Class:**
  - Provides a simple text-based menu for interacting with the dictionary.
- **UI Class:**
  - Implements the GUI using the `tkinter` library.
  - Allows users to perform dictionary operations through a graphical interface.
- **Function to Write Dictionary to File:**
  - Writes the contents of the dictionary to a text file.
-**Data Structures & Algorithms:**
  - The program stores the words and their meanings and key value pairs in a hashtable by reading from the file. This is sped up by the use of the concurrent futures module.
  - It also writes the content of the hashtable to the text file before exiting. It uses the memory buffer to speed up this process. 
## Author
[Gyening Kwadjo Augustine, DSA Project](https://github.com/gyenios)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

--- 
