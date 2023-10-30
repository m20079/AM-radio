import pandas as pd

for i in range(51, 57):
    df = pd.read_csv(f"new/scope_{i}.csv", header=1, usecols=["Volt"])
    print(df.max()["Volt"])
