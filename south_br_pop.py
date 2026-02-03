import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("data/south_br_pop_geog_reg_2022.xlsx")

# Clean column names
df.columns = df.columns.str.strip()

# Sort and select top 10
top_10 = df.sort_values("POP_2022", ascending=False).head(10)

plt.figure()
plt.pie(
    top_10["POP_2022"],
    labels=top_10["REGION"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title(
    "Top 10 Most Populous Intermediate\nGeographic Regions in Southern Brazil"
)
plt.tight_layout()
plt.show()

explode = [0.1 if p == top_10["POP_2022"].max() else 0 for p in top_10["POP_2022"]]

plt.figure()
plt.pie(
    top_10["POP_2022"],
    labels=top_10["REGION"],
    autopct="%1.1f%%",
    startangle=90,
    explode=explode
)
plt.title(
    "Top 10 Most Populous Intermediate\nGeographic Regions in Southern Brazil"
)
plt.tight_layout()
plt.show()

