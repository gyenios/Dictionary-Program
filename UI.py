import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
from main import *

dictionary = Dictionary()

class DictionaryUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dictionary Application")
        self.root.resizable(False, False)  # Fix window size
        self.root.configure(bg="white")  # Set background color to white
        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = int(screen_width / 2.5)  # Double the width
        window_height = int(screen_height / 3)  # Double the height
        
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Create Options dropdown menu as a title
        options_title = tk.Label(root, text="Options", font=("Open Sans", 11),fg='black', bg='white')  # Adjust font size here
        options_title.grid(row=0, column=3, padx=0, pady=0)

        # Create dropdown symbol on the right
        self.dropdown_symbol = tk.Label(root, text=u"\u25BE", font=("Arial", 20),fg ='green', bg='white')  # Adjust font size here
        self.dropdown_symbol.grid(row=0, column=4, padx=0, pady=0)
        self.dropdown_symbol.bind("<Button-1>", self.toggle_dropdown) 
        
        # Create Search Box
        self.search_entry = tk.Entry(root, width=15, font=("Arial", 12), fg='black', bd=1, highlightbackground='black',highlightthickness=1)  # Adjust width and font size here
        self.search_entry.grid(row=0, column=0, padx=0, pady=0)
        self.search_button = tk.Button(root, text="Search", command=self.search_word, font=("Arial", 11),fg='white', bg='green')  # Adjust font size here
        self.search_button.grid(row=0, column=1, padx=0, pady=0)

        # Definition Text Display title
        definition_title = tk.Label(root, text="DEFINITION", font=("Open Sans", 12, 'bold'), fg='green', bg='white')  # Adjust font size here and set text color to blue
        definition_title.grid(row=1, column=0, padx=0, pady=5)
        

        # Create Definition Text Display Region
        self.definition_text = tk.Text(root, height=5, width=40, font=("Arial", 12), fg='darkred', bg='white', bd=1, highlightbackground='black',highlightthickness=1)  # Adjust height, width, and font size here
        self.definition_text.grid(row=2, column=0, columnspan=4, padx=20, pady=10)
        self.definition_text.config(state=tk.DISABLED)  # Make it read-only

        # Create to Speech button
        self.speech_button = tk.Button(root, text="to Speech", command=self.to_speech, font=("Arial", 11),fg='white', bg='green')  # Adjust font size here
        self.speech_button.grid(row=8, column=0, padx=0, pady=0)
        
        # Dropdown menu initially hidden
        self.dropdown_menu_visible = False
        
        # Bind the on_close method to the window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def toggle_dropdown(self, event):
        if self.dropdown_menu_visible:
            self.dropdown_menu.grid_forget()
            self.dropdown_menu_visible = False
        else:
            self.show_dropdown_menu()

    def show_dropdown_menu(self):
        self.dropdown_menu = tk.Menu(self.root, tearoff=0)
        self.dropdown_menu.add_command(label="Add word", command=lambda: self.handle_option_selection("Add word"))
        self.dropdown_menu.add_command(label="Delete word", command=lambda: self.handle_option_selection("Delete word"))
        self.dropdown_menu.add_command(label="Update word", command=lambda: self.handle_option_selection("Update word"))

        self.dropdown_menu.tk_popup(self.dropdown_symbol.winfo_rootx(), self.dropdown_symbol.winfo_rooty() + self.dropdown_symbol.winfo_height())
        self.dropdown_menu_visible = True

    def handle_option_selection(self, option):
        if option == "Add word":
            self.show_add_word_popup()
        elif option == "Delete word":
            self.show_delete_word_popup()
        elif option == "Update word":
            self.show_update_word_popup()

    def show_add_word_popup(self):
        add_word_popup = tk.Toplevel(self.root)
        add_word_popup.title("Add Word")
        
        word_label = tk.Label(add_word_popup, text="Word:")
        word_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        self.word_entry = tk.Entry(add_word_popup)
        self.word_entry.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        self.word_entry.bind("<KeyRelease>", self.check_entries_filled)  # Check entry on each key release

        definition_label = tk.Label(add_word_popup, text="Definition:")
        definition_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        self.definition_entry = tk.Entry(add_word_popup)
        self.definition_entry.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')
        self.definition_entry.bind("<KeyRelease>", self.check_entries_filled)  # Check entry on each key release

        self.add_button = tk.Button(add_word_popup, text="Add", state=tk.DISABLED, command=lambda: self.add_word(add_word_popup))
        self.add_button.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

    def check_entries_filled(self, event=None):
        if self.word_entry.get() and self.definition_entry.get():
            self.add_button.config(state=tk.NORMAL)
        else:
            self.add_button.config(state=tk.DISABLED)

    def add_word(self, popup):
        word = self.word_entry.get()
        definition = self.definition_entry.get()
        result = dictionary.add_word(word,definition)
        messagebox.showinfo("Add Word", result)
        popup.destroy()


    def show_delete_word_popup(self):
        delete_word_popup = tk.Toplevel(self.root)
        delete_word_popup.title("Delete Word")
        
        word_label = tk.Label(delete_word_popup, text="Word:")
        word_label.grid(row=0, column=0, padx=10, pady=10)
        self.word_entry_delete = tk.Entry(delete_word_popup)
        self.word_entry_delete.grid(row=0, column=1, padx=10, pady=10)
        self.word_entry_delete.bind("<KeyRelease>", self.check_entry_filled)  # Check entry on each key release

        self.delete_button = tk.Button(delete_word_popup, text="Delete", state=tk.DISABLED, command=lambda: self.delete_word(delete_word_popup))
        self.delete_button.grid(row=1, column=1, padx=10, pady=10)

    def check_entry_filled(self, event=None):
        if self.word_entry_delete.get():  # Check if entry box is filled
            self.delete_button.config(state=tk.NORMAL)  # Enable the button
        else:
            self.delete_button.config(state=tk.DISABLED)  # Disable the button

    def delete_word(self,popup):
        word = self.word_entry_delete.get()
        result = dictionary.delete_word(word)
        messagebox.showinfo("Delete Word", result)
        popup.destroy()

    def show_update_word_popup(self):
        update_word_popup = tk.Toplevel(self.root)
        update_word_popup.title("Update Word")
        
        word_label = tk.Label(update_word_popup, text="Word:")
        word_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        self.word_entry_update = tk.Entry(update_word_popup)
        self.word_entry_update.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        self.word_entry_update.bind("<KeyRelease>", self.check_entries_filled_update)  # Check entry on each key release

        new_definition_label = tk.Label(update_word_popup, text="New Definition:")
        new_definition_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        self.new_definition_entry = tk.Entry(update_word_popup)
        self.new_definition_entry.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')
        self.new_definition_entry.bind("<KeyRelease>", self.check_entries_filled_update)  # Check entry on each key release
        
        self.update_button = tk.Button(update_word_popup, text="Update", state=tk.DISABLED, command=lambda: self.update_word(update_word_popup))
        self.update_button.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

    def check_entries_filled_update(self, event=None):
        if self.word_entry_update.get() and self.new_definition_entry.get():  # Check if both entry boxes are filled
            self.update_button.config(state=tk.NORMAL)  # Enable the button
        else:
            self.update_button.config(state=tk.DISABLED)  # Disable the button
    
    def update_word(self, popup):
        word = self.word_entry_update.get()
        definition = self.new_definition_entry.get()
        result = dictionary.update_word(word,definition)
        messagebox.showinfo("Update Word", result)
        popup.destroy()

    def search_word(self):
        self.word = self.search_entry.get().strip()
        if self.word:
            self.definition = dictionary.find_definition(self.word)
            self.definition_text.config(state=tk.NORMAL)
            self.definition_text.delete("1.0", tk.END)
            self.definition_text.insert(tk.END, self.definition)
            self.definition_text.config(state=tk.DISABLED)

    def to_speech(self):
        word = self.word
        definition = self.definition
        dictionary.to_Speech(word,definition)

    def on_close(self):
        print("Window is closing")
        write_dictionary_to_file(dictionary.words, "words.txt")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DictionaryUI(root)
    root.mainloop()
