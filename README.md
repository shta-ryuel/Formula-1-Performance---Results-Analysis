# Formula 1 Performance & Results Analysis

## Project Overview
This project provides an in-depth analysis of Formula 1 data, exploring driver performance, constructor standings, race locations, and more. Using Python libraries like Pandas, Matplotlib, and Seaborn, the analysis visualizes key insights from historical Formula 1 data.

## Features
- **Driver Performance**:
  - Analyze top drivers based on total points.
  - Visualize the fastest laps achieved by drivers.
- **Constructor Insights**:
  - Track constructor performance over time.
  - Summarize seasonal points by constructors.
- **Race Results**:
  - Distribution of race positions.
- **Geographical Insights**:
  - Plot race locations by country.
  - Visualize circuit distributions based on latitude and longitude.
- **Demographics**:
  - Pie chart showing the top nationalities of drivers.

## Data Sources
This project uses CSV files containing historical Formula 1 data, including:
- **`circuits.csv`**: Information about circuits (location, latitude, longitude, country).
- **`drivers.csv`**: Details about drivers (names, nationalities).
- **`constructor_standings.csv`**: Constructor standings over seasons.
- **`driver_standings.csv`**: Driver standings over seasons.
- **`results.csv`**: Race results data.
- **`races.csv`**: Information about races (season, race ID, etc.).

## Visualizations
The following visualizations are included:

1. **Top Drivers by Total Points**:
   - Bar chart highlighting the top drivers based on accumulated points.

2. **Constructor Performance Over Time**:
   - Scatter plot showing the performance of top constructors across races.

3. **Race Position Distribution**:
   - Histogram displaying the frequency of race positions.

4. **Fastest Laps by Drivers**:
   - Line plot of drivers with the most fastest laps.

5. **Driver Nationalities**:
   - Pie chart of top nationalities represented in Formula 1.

6. **Constructor Points Over Seasons**:
   - Line plot showing seasonal points scored by constructors.

7. **Race Locations by Country**:
   - Bar chart of races hosted by each country.

## Requirements
- Python 3.8+
- Libraries: `pandas`, `matplotlib`, `seaborn`

Install the required libraries with:
```bash
pip install pandas matplotlib seaborn
```

## Usage
1. Clone the repository.
   ```bash
   git clone https://github.com/shta-ryuel/Formula-1-Performance---Results-Analysis
   cd Formula-1-Performance---Results-Analysis
   ```

2. Place the CSV files in the `data/` directory.

3. Run the main script:
   ```bash
   python main.py
   ```

4. Explore the generated visualizations.

## Project Structure
```
.
├── data_preparation.py      # Data loading and cleaning functions
├── visualizations.py        # Visualization functions
├── main.py                  # Entry point to run the analysis
├── data/                    # Directory for CSV files
├── README.md                # Project documentation
```

## Acknowledgments
This analysis is inspired by the thrill and complexity of Formula 1 racing. The data used is publicly available and meant for educational purposes.
Link to original datasets: https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020

