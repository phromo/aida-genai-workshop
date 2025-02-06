#!/usr/bin/env python
from pathlib import Path
import pandas as pd

df = pd.read_csv('./synthetic.csv.gz')
#df = pd.read_csv("hf://datasets/starmpcc/Asclepius-Synthetic-Clinical-Notes/synthetic.csv")
Path('./asclepius_notes.json').write_text(df.head(2000).to_json(orient='records'))

print("done")
