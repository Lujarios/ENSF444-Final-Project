import requests

def fetch_mono_color_cards(colour=""):
    '''
    Fetches all cards of a specified color from the scryfall API
    Will only fetch mono-color cards. A.k.a., cards with multiple colors
    will not be fetched.

    Keyword Arguments:
    colour -- the specified color
    '''
    letter_code = {
        "blue":"U",
        "black":"B",
        "red":"R",
        "green":"G",
        "white":"W"
    }

    query = f"c:{colour} -c:multicolor"

    print(f"Query: {query}")

    params = {
        "q":query,
        "order":"name", 
        "unique":"cards"}
    
    url = "https://api.scryfall.com/cards/search"
    texts = []  # List to store the oracle text of blue cards

    while url:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print("Error fetching data:", response.status_code)
            break

        data = response.json()
        for card in data.get("data", []):
            # Cards contain a certain type. This will just be appended to the beginning of the oracle text
            type_line = card.get("type_line")
            oracle_text = card.get("oracle_text") if card.get("oracle_text") != None else ""

            # Some cards may not have oracle_text (e.g., tokens or cards with no text)
            card_text = type_line + "\n" + oracle_text
            if card_text:
                texts.append(card_text)
        
        # If there are more pages, use the provided next_page URL.
        if data.get("has_more"):
            url = data.get("next_page")
            params = {}  # next_page URL already includes the query parameters.
        else:
            url = None

    return texts

def main():
    # colors to be fetched
    colors = ["blue", "black", "red", "green", "white"]
    # iterate through each color, fetching and storing them
    for color in colors:
        print(f"Fetching text for {color} cards...")
        color_card_texts = []
        color_card_texts = fetch_mono_color_cards(color)
        output_filename = f"{color}_cards_texts.txt"
        
        output_filepath = "data/"
        output_filename = output_filepath + output_filename  
        with open(output_filename, "w", encoding="utf-8") as file:
            for text in color_card_texts:
                file.write(text + "\n\n")
        
        print(f"Downloaded text for {len(color_card_texts)} {color} cards.")
        print(f"Check the file '{output_filename}' for the results.")

if __name__ == "__main__":
    main()
