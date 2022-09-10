# Made by TH1RDKEYBLADE
# Note that there are typos in transcript and those aren't accounted for
# Imports - BuiltIn
from os import path

# Main Function
def main():
    print("Bee Movie Transcript Word Counter!")
    print("----------------------------------")
    input("Press Enter to continue!\n")

    # Opens Script file
    with open(path.join(path.dirname(__file__), 'bee_movie_transcript.txt')) as f:
        all_text = f.read()

        # Main Game loop
        while True:
            
            # Custom word
            my_word = input("Enter the word you want to count: ").lower()
            word_count = 0
            
            # Goes through every word in the script and counts it
            for word in all_text.split(" "):
                # char to lowercase then back to list
                word = word.lower()
                word = list(word)

                # Removes Special characters from the word
                for char in word:
                    if char in ['', ' ', '~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']:
                        word.remove(char)

                # changes word back to string to compare
                word = "".join(word)
                if my_word == word:
                    word_count += 1
            
            # Prints outcome
            print(f"\"{my_word}\" was said {word_count} times!\n")

if __name__ == "__main__":
    main()