import pandas as pd

# Load the datasets
def load_data():
    circuits = pd.read_csv('circuits.csv')
    constructor_results = pd.read_csv('constructor_results.csv')
    constructor_standings = pd.read_csv('constructor_standings.csv')
    constructors = pd.read_csv('constructors.csv')
    driver_standings = pd.read_csv('driver_standings.csv')
    drivers = pd.read_csv('drivers.csv')
    lap_times = pd.read_csv('lap_times.csv')
    pit_stops = pd.read_csv('pit_stops.csv')
    qualifying = pd.read_csv('qualifying.csv')
    races = pd.read_csv('races.csv')
    results = pd.read_csv('results.csv')
    seasons = pd.read_csv('seasons.csv')
    sprint_results = pd.read_csv('sprint_results.csv')
    status = pd.read_csv('status.csv')
    
    return {
        'circuits': circuits,
        'constructor_results': constructor_results,
        'constructor_standings': constructor_standings,
        'constructors': constructors,
        'driver_standings': driver_standings,
        'drivers': drivers,
        'lap_times': lap_times,
        'pit_stops': pit_stops,
        'qualifying': qualifying,
        'races': races,
        'results': results,
        'seasons': seasons,
        'sprint_results': sprint_results,
        'status': status
    }

# Clean the datasets
def clean_data(dfs):
    # Clean results data
    results = dfs['results'].copy()
    
    # Handle non-numeric or inconsistent 'time' column values
    def convert_time(value):
        try:
            # Example: '1min 20.456s' -> 80.456 seconds
            if isinstance(value, str):
                if 'min' in value:
                    minutes, seconds = value.split('min')
                    total_seconds = float(minutes.strip()) * 60 + float(seconds.strip().replace('s', ''))
                    return total_seconds
                elif 's' in value:
                    return float(value.strip().replace('s', ''))
            return float(value)
        except ValueError:
            return None  # Handle non-convertible values

    # Apply the conversion and drop rows with invalid time
    results['time'] = results['time'].apply(convert_time)
    results = results.dropna(subset=['time'])
    
    # Update the cleaned results back in the dictionary
    dfs['results'] = results
    
    return dfs

if __name__ == "__main__":
    data = load_data()
    data = clean_data(data)
    print(data['results'].head())
