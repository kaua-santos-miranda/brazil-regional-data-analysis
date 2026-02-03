import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("data/gdp_br_states_evolution.xlsx")

# Set state as index
df.set_index("State", inplace=True)

# Calculate percentage growth from 2002 to 2023
df["Growth_%"] = ((df["GDP_2023"] - df["GDP_2002"]) / df["GDP_2002"]) * 100

# TOP 10 GROWTH_% #

top_10_growth = df.sort_values("Growth_%", ascending=False).head(10)

plt.figure()
top_10_growth["Growth_%"].plot(kind="bar")
plt.title("Top 10 largest percentage GDP growth rates (2002–2023)")
plt.xlabel("State")
plt.ylabel("Percentage growth (%)")
plt.tight_layout()
plt.show()

# TOP 10 GDP #

top_10_gdp = df.sort_values("GDP_2023", ascending=False).head(10)

plt.figure()
for state in top_10_gdp.index:
    plt.plot(
        ["2002", "2010", "2023"],
        [
            top_10_gdp.loc[state, "GDP_2002"],
            top_10_gdp.loc[state, "GDP_2010"],
            top_10_gdp.loc[state, "GDP_2023"],
        ],
        label=state
    )

plt.title("GDP trend of the 10 largest states (2002–2023)")
plt.xlabel("Year")
plt.ylabel("GDP")
plt.legend()
plt.tight_layout()
plt.show()

bottom_10_growth = df.sort_values("Growth_%", ascending=True).head(10)

plt.figure()
bottom_10_growth["Growth_%"].plot(kind="bar")
plt.title("Top 10 lowest percentage GDP growth rates (2002–2023)")
plt.xlabel("State")
plt.ylabel("Percentage growth (%)")
plt.tight_layout()
plt.show()
