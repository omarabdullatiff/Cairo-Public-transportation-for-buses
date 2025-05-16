import pandas as pd
import os
from datetime import datetime, timedelta
import random
from sqlalchemy import create_engine

# Database connection using SQLite
engine = create_engine('sqlite:///cairo_bus.db')

# Path to GTFS files
gtfs_path = 'Cairo GTFS Bus Metro'

# Read GTFS files
stops_df = pd.read_csv(os.path.join(gtfs_path, 'stops.txt'))
routes_df = pd.read_csv(os.path.join(gtfs_path, 'routes.txt'))
trips_df = pd.read_csv(os.path.join(gtfs_path, 'trips.txt'))
stop_times_df = pd.read_csv(os.path.join(gtfs_path, 'stop_times.txt'))

# Process Stops
print("Processing Stops...")
stops_output = pd.DataFrame({
    'Name': stops_df['stop_name'],
    'Latitude': stops_df['stop_lat'].astype(float),
    'Longitude': stops_df['stop_lon'].astype(float)
})
stops_output.to_sql('Stops', engine, if_exists='replace', index=False)

# Process Routes
print("Processing Routes...")
routes_output = pd.DataFrame({
    'Origin': routes_df['route_long_name'],
    'Destination': routes_df['route_long_name']
})
routes_output.to_sql('Routes', engine, if_exists='replace', index=False)

# Create dummy Drivers
print("Creating dummy Drivers...")
driver_names = ['Ahmed Mohamed', 'Mohamed Ali', 'Sara Hassan', 'Karim Ibrahim', 'Fatima Mahmoud']
drivers_output = pd.DataFrame([{
    'Name': name,
    'PhoneNumber': f'01{random.randint(100000000, 999999999)}',
    'LicenseNumber': f'LIC{random.randint(10000, 99999)}'
} for name in driver_names])
drivers_output.to_sql('Drivers', engine, if_exists='replace', index=False)

# Create dummy Buses
print("Creating dummy Buses...")
bus_models = ['Mercedes O500', 'Volvo B7R', 'Scania K320', 'MAN Lion\'s Coach']
buses_output = pd.DataFrame([{
    'LicensePlate': f'CTE{random.randint(1000, 9999)}',
    'Model': random.choice(bus_models),
    'Capacity': random.randint(30, 50),
    'Status': 'Active',
    'CurrentLatitude': float(stops_df['stop_lat'].iloc[0]),
    'CurrentLongitude': float(stops_df['stop_lon'].iloc[0]),
    'DriverId': random.randint(1, len(driver_names)),
    'RouteId': random.randint(1, len(routes_df))
} for _ in range(20)])
buses_output.to_sql('Buses', engine, if_exists='replace', index=False)

# Process RouteStop
print("Processing RouteStop...")
route_stop_output = []
for route_id in range(1, len(routes_df) + 1):
    stops_for_route = random.sample(range(1, len(stops_df) + 1), min(10, len(stops_df)))
    for order, stop_id in enumerate(stops_for_route, 1):
        route_stop_output.append({
            'RouteId': route_id,
            'StopId': stop_id,
            'Order': order
        })
pd.DataFrame(route_stop_output).to_sql('RouteStop', engine, if_exists='replace', index=False)

# Process Trips
print("Processing Trips...")
start_time = datetime.now()
trips_output = pd.DataFrame([{
    'BusId': random.randint(1, 20),
    'RouteId': random.randint(1, len(routes_df)),
    'StartTime': start_time,
    'EndTime': start_time + timedelta(hours=2)
} for _ in range(len(trips_df))])
trips_output.to_sql('Trips', engine, if_exists='replace', index=False)

# Process TrackingData
print("Processing TrackingData...")
tracking_output = []
for bus_id in range(1, 21):
    for _ in range(10):  # 10 tracking points per bus
        tracking_output.append({
            'Latitude': float(stops_df['stop_lat'].iloc[random.randint(0, len(stops_df)-1)]),
            'Longitude': float(stops_df['stop_lon'].iloc[random.randint(0, len(stops_df)-1)]),
            'Timestamp': datetime.now() - timedelta(minutes=random.randint(0, 60)),
            'BusId': bus_id
        })
pd.DataFrame(tracking_output).to_sql('TrackingData', engine, if_exists='replace', index=False)

# Create dummy LostItems
print("Creating dummy LostItems...")
items = ['Backpack', 'Phone', 'Wallet', 'Laptop', 'Umbrella']
lost_items_output = pd.DataFrame([{
    'ImagePath': f'/images/lost_item_{random.randint(1, 100)}.jpg',
    'BusNumber': f'CTE{random.randint(1000, 9999)}',
    'Description': f'Lost {random.choice(items)}',
    'ReportedAt': datetime.now() - timedelta(days=random.randint(0, 7)),
    'Name': f'Person {random.randint(1, 100)}',
    'Phone': f'01{random.randint(100000000, 999999999)}'
} for _ in range(10)])
lost_items_output.to_sql('LostItems', engine, if_exists='replace', index=False)

print("Data import completed successfully! Database file created: cairo_bus.db") 