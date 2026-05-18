import pandas as pd

def rank_candidates(df):
    df_sorted = df.sort_values(by="predicted_activity",ascending=False).reset_index(drop=True)
    df_sorted["rank"] =df_sorted.index + 1
    return df_sorted

# Example usage
data = {
    "smiles": [
        "CCO",
        "CCCN",
        "CC(=O)O",
        "CCN(CC)CC",
        "CCOC(=O)C"
    ],
    "predicted_activity": [0.23, 0.78, 0.12, 0.56, 0.44]
}
df = pd.DataFrame(data)
ranked_df = rank_candidates(df)
print(ranked_df)