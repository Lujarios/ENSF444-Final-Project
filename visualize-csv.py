import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Replace 'your_file.csv' with the path to your CSV file
df = pd.read_csv('data/ml_data.csv')

# Define a set of stop words to ignore (all in lowercase for comparison)
stopwords = {"a", "the", "this", "of", "to", "or", "and"}

# Dictionary to hold word counts for each color and an overall counter
color_word_counts = {}
overall_counter = Counter()

# Process each row in the CSV
for _, row in df.iterrows():
    color = row['color']
    features = row['features']
    tokens = features.split()  # Split on whitespace
    
    # Initialize a Counter for the color if it doesn't exist yet
    if color not in color_word_counts:
        color_word_counts[color] = Counter()
    
    # Process each token in the "word:count" format
    for token in tokens:
        try:
            word, count_str = token.split(':')
            # Skip stop words (case insensitive)
            if word.lower() in stopwords:
                continue
            count = int(count_str)
            color_word_counts[color][word] += count
            overall_counter[word] += count
        except ValueError:
            # If token is not in the expected format, skip it
            continue

# Plot the top 25 words for each color
for color, counter in color_word_counts.items():
    top_words = counter.most_common(25)
    if top_words:
        words, counts = zip(*top_words)
    else:
        words, counts = [], []
    
    plt.figure(figsize=(25, 6))
    plt.bar(words, counts)
    plt.title(f"Top 25 Words for Color: {color}")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Plot the overall top 25 words across all cards
overall_top_words = overall_counter.most_common(25)
if overall_top_words:
    overall_words, overall_counts = zip(*overall_top_words)
else:
    overall_words, overall_counts = [], []

plt.figure(figsize=(25, 6))
plt.bar(overall_words, overall_counts)
plt.title("Top 25 Words in All Cards")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
