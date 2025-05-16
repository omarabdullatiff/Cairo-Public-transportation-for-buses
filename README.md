# Cairo Public Transportation for Buses

This project processes GTFS (General Transit Feed Specification) data for Cairo's bus transportation system and converts it into a SQLite database format.

## Features

- Processes GTFS data from Cairo's bus system
- Creates a SQLite database with the following tables:
  - Stops
  - Routes
  - Drivers
  - Buses
  - RouteStop
  - Trips
  - TrackingData
  - LostItems

## Requirements

- Python 3.x
- pandas
- sqlalchemy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/omarabdullatiff/Cairo-Public-transportation-for-buses.git
cd Cairo-Public-transportation-for-buses
```

2. Install required packages:
```bash
pip install pandas sqlalchemy
```

## Usage

1. Place your GTFS files in the `Cairo GTFS Bus Metro` directory
2. Run the script:
```bash
python clean_data.py
```

The script will create a `cairo_bus.db` SQLite database file containing all the processed data.

## Project Structure

- `clean_data.py`: Main script for processing GTFS data and creating the database
- `test_data_import.py`: Test script that exports data to CSV files
- `Cairo GTFS Bus Metro/`: Directory containing GTFS data files
- `test_data/`: Directory containing test data exports

## Database Schema

The database includes the following tables:
- Stops: Bus stop locations
- Routes: Bus routes
- Drivers: Driver information
- Buses: Bus fleet information
- RouteStop: Route-stop relationships
- Trips: Bus trip records
- TrackingData: Real-time bus location data
- LostItems: Lost and found items

## License

This project is licensed under the MIT License - see the LICENSE file for details. 