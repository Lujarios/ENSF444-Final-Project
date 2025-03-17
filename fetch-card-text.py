import requests

def fetch_blue_cards():
    # Base URL for Scryfall card search
    url = "https://api.scryfall.com/cards/search"
    # Query to select blue cards (Scryfall query syntax: c:blue)
    params = {
        "q": "c:blue",
        "order": "name",      # optional: orders the results by card name
        "unique": "cards"    # optional: include every printed version
    }
    
    blue_texts = []  # List to store the oracle text of blue cards

    while url:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print("Error fetching data:", response.status_code)
            break

        data = response.json()
        for card in data.get("data", []):
            # Some cards may not have oracle_text (e.g., tokens or cards with no text)
            card_text = card.get("oracle_text")
            if card_text:
                blue_texts.append(card_text)
        
        # If there are more pages, use the provided next_page URL.
        if data.get("has_more"):
            url = data.get("next_page")
            params = {}  # next_page URL already includes the query parameters.
        else:
            url = None

    return blue_texts

def fetch_black_cards():
    # Base URL for Scryfall card search
    url = "https://api.scryfall.com/cards/search"
    # Query to select black cards (Scryfall query syntax: c:black)
    params = {
        "q": "c:black",
        "order": "name",      # optional: orders the results by card name
        "unique": "cards"    # optional: include every printed version
    }
    
    black_texts = []  # List to store the oracle text of black cards

    while url:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print("Error fetching data:", response.status_code)
            break

        data = response.json()
        for card in data.get("data", []):
            # Some cards may not have oracle_text (e.g., tokens or cards with no text)
            card_text = card.get("oracle_text")
            if card_text:
                black_texts.append(card_text)
        
        # If there are more pages, use the provided next_page URL.
        if data.get("has_more"):
            url = data.get("next_page")
            params = {}  # next_page URL already includes the query parameters.
        else:
            url = None

    return black_texts

def fetch_red_cards():
    # Base URL for Scryfall card search
    url = "https://api.scryfall.com/cards/search"
    # Query to select red cards (Scryfall query syntax: c:red)
    params = {
        "q": "c:red",
        "order": "name",      # optional: orders the results by card name
        "unique": "cards"    # optional: include every printed version
    }
    
    red_texts = []  # List to store the oracle text of red cards

    while url:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print("Error fetching data:", response.status_code)
            break

        data = response.json()
        for card in data.get("data", []):
            # Some cards may not have oracle_text (e.g., tokens or cards with no text)
            card_text = card.get("oracle_text")
            if card_text:
                red_texts.append(card_text)
        
        # If there are more pages, use the provided next_page URL.
        if data.get("has_more"):
            url = data.get("next_page")
            params = {}  # next_page URL already includes the query parameters.
        else:
            url = None

    return red_texts

def fetch_green_cards():
    # Base URL for Scryfall card search
    url = "https://api.scryfall.com/cards/search"
    # Query to select green cards (Scryfall query syntax: c:green)
    params = {
        "q": "c:green",
        "order": "name",      # optional: orders the results by card name
        "unique": "cards"    # optional: include every printed version
    }
    
    green_texts = []  # List to store the oracle text of green cards

    while url:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print("Error fetching data:", response.status_code)
            break

        data = response.json()
        for card in data.get("data", []):
            # Some cards may not have oracle_text (e.g., tokens or cards with no text)
            card_text = card.get("oracle_text")
            if card_text:
                green_texts.append(card_text)
        
        # If there are more pages, use the provided next_page URL.
        if data.get("has_more"):
            url = data.get("next_page")
            params = {}  # next_page URL already includes the query parameters.
        else:
            url = None

    return green_texts

def fetch_white_cards():
    # Base URL for Scryfall card search
    url = "https://api.scryfall.com/cards/search"
    # Query to select white cards (Scryfall query syntax: c:white)
    params = {
        "q": "c:white",
        "order": "name",      # optional: orders the results by card name
        "unique": "cards"    # optional: include every printed version
    }
    
    white_texts = []  # List to store the oracle text of white cards

    while url:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print("Error fetching data:", response.status_code)
            break

        data = response.json()
        for card in data.get("data", []):
            # Some cards may not have oracle_text (e.g., tokens or cards with no text)
            card_text = card.get("oracle_text")
            if card_text:
                white_texts.append(card_text)
        
        # If there are more pages, use the provided next_page URL.
        if data.get("has_more"):
            url = data.get("next_page")
            params = {}  # next_page URL already includes the query parameters.
        else:
            url = None

    return white_texts

def main():

    colors = ["blue","black", "red", "green", "white"]

    for color in colors:
        print(f"Fetching text for {color} cards...")
        color_card_texts = []
        if color == "black":
            color_card_texts = fetch_black_cards()
            output_filename = "black_cards_texts.txt"
        elif color == "red":
            color_card_texts = fetch_red_cards()
            output_filename = "red_cards_texts.txt"
        elif color == "green":
            color_card_texts = fetch_green_cards()
            output_filename = "green_cards_texts.txt"
        elif color == "white":
            color_card_texts = fetch_white_cards()
            output_filename = "white_cards_texts.txt"
        elif color == "blue":
            color_card_texts = fetch_blue_cards()
            output_filename = "blue_cards_texts.txt"
            
        output_filepath = "data/"
        output_filename = output_filepath + output_filename  
        with open(output_filename, "w", encoding="utf-8") as file:
            for text in color_card_texts:
                file.write(text + "\n\n")
        
        print(f"Downloaded text for {len(color_card_texts)} {color} cards.")
        print(f"Check the file '{output_filename}' for the results.")

if __name__ == "__main__":
    main()
