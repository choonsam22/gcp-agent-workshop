import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")
df.groupby("region")["amount"].sum().plot(kind="bar")
plt.title("Sales by Region")
plt.ylabel("Amount (KRW)")
plt.tight_layout()
plt.savefig("sales.png")
print("saved: sales.png")
