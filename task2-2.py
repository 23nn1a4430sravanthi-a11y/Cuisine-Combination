'''Task: Cuisine Combination
Identify the most common combinations of
cuisines in the dataset.
Determine if certain cuisine combinations
tend to have higher ratings'''
import pandas as pd

# ===== Step 1: Load Dataset =====
df = pd.read_csv("restaurants.csv")

# ===== Step 2: Clean Cuisine Combinations =====
# Keep full cuisine combination as given (do not split)
df['Cuisines'] = df['Cuisines'].str.strip()

# Count each cuisine combination
combo_counts = df['Cuisines'].value_counts()

# Top 10 most common combinations
top_combinations = combo_counts.head(10)

print("===== Top 10 Most Common Cuisine Combinations =====")
print(top_combinations)

# ===== Step 3: Average Rating for Each Combination =====
combo_avg_rating = df.groupby('Cuisines')['Aggregate rating'].mean()

# Combine count and rating
combo_analysis = pd.DataFrame({
    'Count': combo_counts,
    'Average Rating': combo_avg_rating
})

# Sort by count
combo_analysis = combo_analysis.sort_values(by='Count', ascending=False)

print("\n===== Cuisine Combination Analysis (Top 10) =====")
print(combo_analysis.head(10))

# ===== Step 4: Find Combinations with Higher Ratings =====
# Filter combinations with at least 10 restaurants to avoid rare cases
popular_combos = combo_analysis[combo_analysis['Count'] >= 10]

# Sort by highest rating
highest_rated_combos = popular_combos.sort_values(by='Average Rating', ascending=False)

print("\n===== Cuisine Combinations with Highest Ratings =====")
print(highest_rated_combos.head(5))

# ===== Step 5: Save Results =====
combo_analysis.head(10).to_csv("top_cuisine_combinations.csv")
highest_rated_combos.head(5).to_csv("highest_rated_combinations.csv")

print("\nResults saved as:")
print("top_cuisine_combinations.csv")
print("highest_rated_combinations.csv")
