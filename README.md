# Brazilian Regional Economic and Demographic Analysis

## Overview
This project performs an economic and demographic data analysis focused on Brazil, combining state-level GDP data and population data from intermediate geographic regions in the Southern Region of the country.

The project was designed for portfolio purposes, emphasizing clean code organization, real-world datasets, and appropriate data visualization techniques.

---

## Objectives
- Analyze the GDP evolution of Brazilian states between 2002, 2010, and 2023
- Identify:
  - Top 10 states with the largest GDP growth (percentage)
  - Top 10 states with the highest absolute GDP values
  - Top 10 states with the smallest GDP growth (percentage)
- Analyze the population distribution of the Southern Region’s intermediate geographic regions
- Present results using static and interactive visualizations

---

## Data Sources
- GDP data: Wikipedia / IBGE (Brazilian Institute of Geography and Statistics)
- Population data: IBGE – Intermediate Geographic Regions (2017 division)

All datasets were manually curated and normalized to ensure consistency across years and regions.

The file `sample.xlsx` contains fictitious data and is included solely for demonstration and testing purposes. It is not part of the real-world datasets used in the analysis.

---

## Technologies Used
- Python 3.10+
- pandas
- matplotlib
- plotly
- openpyxl

---

## Visualizations

### GDP Analysis
- Bar chart: Top 10 largest GDP growth (percentage, 2002–2023)
- Line chart: GDP trends of the 10 largest state economies
- Bar chart: Top 10 smallest GDP growth (percentage)

### Population Analysis (Southern Brazil)
- Pie chart: Population distribution of the top 10 intermediate geographic regions
- Sunburst chart (interactive): Population hierarchy by state and intermediate region

---

## Project Structure

excel-data-analyzer/
│
├── data/
│ ├── gdp_br_states_evolution.xlsx
│ ├── south_br_pop_geog_reg_2022.xlsx
│ ├── south_br_pop_geog_reg_sun_2022.xlsx
│ └── sample.xlsx
│
├── reports/
│ ├── .gitkeep
│ └── excel_analysis_report.txt
│
├── analyzer.py
├── evolution_states_gdp.py
├── loader.py
├── main.py
├── report.py
├── south_br_pop.py
├── south_br_pop_sunburst.py
├── README.md

---

## How to Run

### Install dependencies

pip install pandas matplotlib plotly openpyxl

### Run main analysis

python main.py

### Run GDP evolution analysis

python evolution_states_gdp.py

### Run population analysis (pie chart)

python south_br_pop.py

### Run population analysis (sunburst)

python south_br_pop_sunburst.py

---

## Key Insights
- High absolute GDP values do not necessarily imply high relative growth
- Smaller state economies may present higher percentage growth over time
- Population in Southern Brazil is highly concentrated in major urban regions
- Choosing the appropriate visualization type improves analytical clarity

---

## Notes
- Interactive visualizations may take a few seconds to render due to their dynamic nature
- Sunburst charts are generated using Plotly and rendered locally
- Column names are sanitized to avoid inconsistencies across different data sources

---

## Future Improvements
- GDP per capita analysis
- Regional aggregation by Brazilian macro-regions
- Automated data ingestion
- Dashboard integration

---

## License
This project is intended for educational and portfolio purposes.