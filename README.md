# The Correlation Between Housing Value and the Unemployment Rates in the United States

## Abstract
Upon first reflection, it seems that there would some correlation between unemployment and housing value. If unemployment rises, less people may be able to afford the home they live in, leading to the person in question selling their home. With more houses on the market, housing value may drop. However, even if the one who is unemployed does not sell their house, they may not be able to afford up-keep on the house. This too would cause a drop in housing value.

The Bureau of Labor Statistics (BLS) and Federal Housing Finance Agency (FHFA) publish datasets that allow this theory to be tested. Nationally, it is found that there is a weak negative correlation between the unemployment rate and housing value of -0.28. When correlations are grouped by metro area, there are some signifcant outliers where the correlation is much stronger or much weaker. A time-series analysis is performed on a four select metro areas, which include the two minimal and maximal outliers, and two middling metro areas closer to the national average. Local correlation and housing value are plotted to visualize their relationship over time. The graphs suggest that factors other than unemployment often drive housing prices.

## Main Questions & Findings

### Questions
1. **National Trend:** Is there a significant correlation between the unemployment rate and housing value index on a national scale?
2. **Local Variations:** Does the correlation become stronger or exhibit different behaviors when isolated to specific metropolitan areas?

### Findings & Observations
* **National Correlation:** Intuition suggests that as unemployment rises, housing value drops, but the analysis suggests a relatively weak correlation between the national unemployment rate and housing value index.
* **Metro-Specific Trends:** The project investigates specific metro areas (e.g., Fresno, CA; Des Moines, IA; Tulsa, OK; Louisville, KY). These were selected to observe because the correlation was exceptionally strong (Fresno, CA), middling (Tulsa, OK), and low (Louisville, KY; Des Moines, IA). The time series analysis suggests that factors other than unemployment tend to drive housing value. 
* **Data Coverage:** The analysis covers a timeframe of thirty-five years (1990–2025) and joins data between sixty-seven geographic regions. However, of the 393 geographical codes (CBSAs) only 67 were found to be in common between the two datasets. A larger commonality between datasets may yield differing results. 

---

## Data Sources
Credit is given to the following federal agencies for the raw data used in this analysis:

1. **Housing Price Index (HPI)**
    * **Source:** [Federal Housing Finance Agency (FHFA)](https://www.fhfa.gov/data/hpi)
    * **Dataset:** `hpi_po_metro.csv`
    * **Description:** Seasonally adjusted and non-seasonally adjusted housing price index values for metropolitan areas.

2. **Local Area Unemployment Statistics (LAUS)**
    * **Source:** [U.S. Bureau of Labor Statistics (BLS)](https://www.bls.gov/lau/)
    * **Dataset:** `ssamatab1.csv`
    * **Description:** Monthly estimates of employment, unemployment, and labor force data by metropolitan area.

---

## Setup & Installation

Follow these instructions to set up the project environment on your local machine.

### 1. Clone or Download the Repository
Download the files to a local directory.

### 2. Create a Python Virtual Environment
Create a virtual environment to download all library dependencies.

Run `python -m venv venv`:
This calls the built-in `venv` module to create a Python virtual environment.
* **`venv` (the second one)**: This is the name of the folder created. Standard convention is `venv` or `.venv`.

### 3. How to Activate the Environment
Creating the environment is only half the battle; you must **activate** it to use it.

**For Windows (Command Prompt):**
```
.\venv\Scripts\activate
```

**For Windows (Git Bash / PowerShell):**
```
source venv/Scripts/activate
```

**For macOS / Linux:**
```
source venv/bin/activate
```

 **Note:** Once activated, your terminal prompt should change to show `(venv)` at the beginning.

**Deactivation** To exit the virtual environment enter `deactivate` into your terminal.

### 4. Install 'requirements.txt'

Run ```pip install -r requirements.txt``` This will install all the required dependencies.

### 5. Using Jupyter Notebooks
The maion project file is named **presentation.ipynb.** Use this file to view the findings.

This project uses Jupyter notebooks instead of a traditional Python file. The advantages of using this file type are the ability to run code blocks independently of one another in python cells. Markdown cells are also able to be inserted into the document, making for presentable code. 

In order to use the notebook:
1. Install a Jupyter Notebook Extension for your IDE if required.
2. Select the Kernel of Python installed from requirements.txt.
3. Run the file using the 'run' button found in your preferred IDE. This will generate all the code and visualizations within the notebook itself, and not in your terminal.

# Author
David English

# Acknowledgements
Gemini, ChatGPT, and Claude were consulted during the making of this project.

# License
MIT License
