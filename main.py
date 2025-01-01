from data_preparation import load_data, clean_data
from visualizations import (
    plot_top_drivers_by_points, 
    plot_constructor_performance, 
    plot_race_positions,
    plot_fastest_laps,
    plot_driver_nationalities,
    plot_seasonal_constructor_points,
    plot_race_locations_by_country
)

def main():
    # Load and clean data
    data = load_data()
    clean_data(data)

    # Extract data for visualization
    driver_standings = data['driver_standings']
    constructor_standings = data['constructor_standings']
    results = data['results']
    drivers = data['drivers']
    constructors = data['constructors']
    races = data['races']
    circuits = data['circuits'] 
    

    # Create visualizations
    plot_top_drivers_by_points(driver_standings)  # Plot the top drivers by total points
    plot_constructor_performance(constructor_standings, constructors)  # Plot constructor performance over time
    plot_race_positions(results)  # Plot race position distribution
    plot_fastest_laps(results, drivers)  # Plot fastest laps by drivers
    plot_driver_nationalities(drivers)  # Plot driver nationalities
    plot_seasonal_constructor_points(results, races, constructors)  # Plot constructor points over seasons
    plot_race_locations_by_country(circuits)  # Plot race locations based on country

if __name__ == "__main__":
    main()

