import pandas as pd
import plotly.express as px

# Load data
df = pd.read_excel("data/south_br_pop_geog_reg_sun_2022.xlsx")

# Clean column names
df.columns = df.columns.str.strip()

# Sort and select top 10 regions by population
top_10 = df.sort_values("POP_2022", ascending=False).head(10)

fig = px.sunburst(
    top_10,
    path=["STATE", "REGION"],
    values="POP_2022",
    title=(
        "Top 10 Most Populous Intermediate Geographic Regions\n"
        "Southern Region of Brazil"
    )
)

fig.write_html("reports/south_br_pop_geog_reg_sun_2022.html")

