import pandas as pd
import re


def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", " URL ", text)
    text = re.sub(r"\d+", " NUMBER ", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# Load raw dataset
df = pd.read_csv(
    "data/raw/SMSSpamCollection",
    sep="\t",
    names=["label", "text"],
    encoding="utf-8"
)

# Convert labels
df["label"] = df["label"].map({
    "ham": 0,
    "spam": 1
})

# Clean messages
df["clean_text"] = df["text"].apply(clean_text)

# Keep required columns
processed_df = df[["clean_text", "label"]].dropna()

# Save processed dataset
processed_df.to_csv(
    "data/processed/processed_sms.csv",
    index=False
)

print("Dataset preprocessing completed!")
print(f"Total messages: {len(processed_df)}")
print(processed_df["label"].value_counts())