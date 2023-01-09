#Writing to a text file
import os

def txt_file_generator(content):
    """
    Generates a text file and writes the specified content to it.
    
    Parameters:
        content (str): The content to be written to the text file.
    Returns:
        None
    """
    with open("temporary.txt", "w") as txt:
        txt.write(content)

def generated_txt_file_remover():
    """
    Deletes the "temporary.txt" file if it exists.
    
    Parameters:
        None
    Returns:
        None
    """
    file_path = "./temporary.txt"
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("Error! Text file (temporary.txt) not found.")

def main(content):
    """
    Main function of the script. Creates the "temporary.txt" file, prompts the user to read it, and then deletes the file.
    
    Parameters:
        content (str): The content to be written to the text file.
    Returns:
        None
    """
    print("\nCreating 'temporary.txt' file....")
    txt_file_generator(content)
    print("\nText file created Successfully!")
    input("\nOpen the txt file and when done press 'Enter' (PRESSING ENTER WILL DELETE THE FILE AUTOMATICALLY): ")
    generated_txt_file_remover()

if __name__ == "__main__":
    txt_file_content = "The quick brown fox jumps over the lazy dog.\nThis is a sentence that contains every letter of the alphabet.\nThis file was generated by txt_file(writing).py and will be deleted automatically once the script terminates."
    main(txt_file_content)