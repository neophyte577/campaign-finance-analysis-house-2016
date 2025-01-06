import numpy as np
import pandas as pd

def clean_names(df):

    if 'name' not in df.columns:
        print('WRONG')
        return

    appellations = r'\b(?:mr|mrs|ms|miss|dr|prof|honorable|hon|jr|sr|esq|ph\.?d|md|rev|capt|lt|gen|cmdr|maj|col|sgt)\b\.? ?'

    df['name'] = (
        df['name']
        .str.replace(appellations, '', regex=True, case=False) # Remove titles, case insensitive
        .str.replace(r'\b\w+\.\s*', '', regex=True)            # Remove all string-separated substrings followed by a period
        .str.replace(r'\b[A-Z]\.?\s+', '', regex=True)         # Remove single initials followed by a space
        .str.replace(r'([^,]+), (.+)', r'\2 \1', regex=True)   # "Last, First" --> "First Last"
        .str.replace(r'[^a-zA-Z ]', '', regex=True)            # Retain only letters and spaces
        .str.replace(r'\s+', ' ', regex=True)                  # Replace multiple spaces with a single space
        .str.lower()                                           
        .str.strip()                                         
    ) 

    def first_and_last(name):
        parts = name.split()  
        return ' '.join([parts[0], parts[-1]])

    df['name'] = df['name'].apply(first_and_last)

    return df

def main():

    df = pd.DataFrame({'name': ['Jingleheimer, Mr. A Honorable Hon. Juan B. Jon Esq. Ack.']})

    print(clean_names(df))

if __name__ == '__main__':
    main()

