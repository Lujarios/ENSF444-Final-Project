import os
import glob
from collections import Counter
import csv
import re

def card_processing_symbols(text):
    '''
    Card from scryfall use a specific non-english syntax when defining important values
    For example, a card costing 2 white mana would be {W}{W}
    This function takes card text and returns the same text with its mana symbol replaced with a specific name
    i.e.,
    {W}{W}{2} -> mana_white mana_white 2 mana_generic
    
    Keyword arguments:
    text -- the text to be processed and returned
    '''
    text = re.sub(r"\{W\}", "mana_white ", text)
    text = re.sub(r"\{U\}", "mana_blue ", text)
    text = re.sub(r"\{B\}", "mana_black ", text)
    text = re.sub(r"\{R\}", "mana_red ", text)
    text = re.sub(r"\{G\}", "mana_green ", text)
    text = re.sub(r"\{(\d+)\}", r"\1 mana_generic", text)
    text = re.sub(r"\{T\}", "symbol_tap ", text)
    text = re.sub(r"\{Q\}", "symbol_untap ", text)
    text = re.sub(r"\{E\}", "symbol_energy ", text)
    return text

def card_remove_explanation_text(text):
    '''
    Cards tend to have an explanation of certain mechanics present within brackets of the cards. As far as which cards have the mechanic versus the explanation
    of the mechanic is inconsistent. Therefore, it makes sense to remove all explanations of mechanics that are simply there for additional information.
    All 'mechanic explanations' are surrounded by brackets.
    This function takes card text and returns the same text with all text between parentheses removed
    i.e.,
    Convoke - (Tap creatures to do something) -> Covoke -

    Keyword arguments:
    text -- text to be processed and returned
    '''
    text = re.sub(r"\((.*?)\)", "", text)
    return text



def main():
    # Set the directory where your text files are located.
    input_dir = ".\\data\\"  # update this path accordingly
    # Output CSV file where the processed data will be saved.
    output_file = "ml_data.csv"

    # Find all files that match the pattern "*_cards_texts.txt"
    all_files = glob.glob(os.path.join(input_dir, "*_cards_texts.txt"))
    # Data will be [{color: , text:}, ]
    data = []
    # This loop will import the text data from each file an append it to our list
    for file_path in all_files:
        filename = os.path.basename(file_path)
        # Extract the color from the filename (e.g., "black_cards_texts.txt" -> "black")
        color = filename.split("_")[0]
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            # Split on double newline; adjust the split if your file uses a different separator.
            cards = content.split("\n\n")
            for card in cards:
                card = card.replace('\n', ' ')
                card = card_processing_symbols(card)
                card = card_remove_explanation_text(card)
                data.append({"color":color, "text":card})

    # Write the processed data to a CSV file.
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames=["color", "text"]
        writer = csv.DictWriter(csvfile, fieldnames=["color", "text"])    
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    print(f"ML data saved to {output_file}")

if __name__ == "__main__":
    main()
