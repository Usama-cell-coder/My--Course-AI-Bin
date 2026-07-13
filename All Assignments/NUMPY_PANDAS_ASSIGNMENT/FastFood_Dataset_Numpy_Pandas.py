import numpy as np
import pandas as pd

try:
    # Load the fast food restaurant data using pandas (more robust for CSV parsing)
    # Use on_bad_lines='skip' to skip problematic rows
    df = pd.read_csv('E:\DataSets_AI_Course\FastFoodRestaurants.csv', 
                     on_bad_lines='skip',
                     encoding='utf-8')
    
    print(f"Successfully loaded {len(df)} restaurants")
    print(f"Columns in dataset: {list(df.columns)}")
    
    # Extract latitude and longitude
    lat = df['latitude'].values
    long = df['longitude'].values
    
    # Convert to float and handle any missing values
    lat = np.array(lat, dtype=float)
    long = np.array(long, dtype=float)
    
    # Replace any NaN values with 0
    long = np.nan_to_num(long, nan=0.0)
    lat = np.nan_to_num(lat, nan=0.0)
    
    # Create synthetic price data based on location
    # Since there's no actual price column, we'll use a combination of coordinates
    # This is just for demonstration - you can replace with actual data if available
    price = np.abs(long + lat) * 100000 + np.abs(long - lat) * 50000
    
    print("\n" + "="*60)
    print("FAST FOOD RESTAURANTS - Statistics Operations")
    print("="*60)
    
    # Statistics operations
    print(f"Number of restaurants: {len(price)}")
    print(f"Price mean: {np.mean(price):.2f}")
    print(f"Price average: {np.average(price):.2f}")
    print(f"Price standard deviation: {np.std(price):.2f}")
    print(f"Price median: {np.median(price):.2f}")
    print(f"Price 25th percentile: {np.percentile(price, 25):.2f}")
    print(f"Price 75th percentile: {np.percentile(price, 75):.2f}")
    print(f"Price 3rd percentile: {np.percentile(price, 3):.2f}")
    print(f"Price minimum: {np.min(price):.2f}")
    print(f"Price maximum: {np.max(price):.2f}")
    
    print("\n" + "="*60)
    print("FAST FOOD RESTAURANTS - Mathematical Operations (First 5 values)")
    print("="*60)
    
    # Show first 5 values for mathematical operations
    price_sample = price[:5]
    
    print(f"Price squared: {np.square(price_sample)}")
    print(f"Price square root: {np.sqrt(price_sample)}")
    print(f"Price absolute: {np.abs(price_sample)}")
    
    print("\n" + "="*60)
    print("FAST FOOD RESTAURANTS - Basic Arithmetic with Coordinates")
    print("="*60)
    
    # Basic arithmetic operations on longitude and latitude
    addition = long + lat
    subtraction = long - lat
    multiplication = long * lat
    
    # Handle division by zero
    with np.errstate(divide='ignore', invalid='ignore'):
        division = np.where(lat != 0, long / lat, 0)
    
    print(f"Longitude + Latitude (first 5): {addition[:5]}")
    print(f"Longitude - Latitude (first 5): {subtraction[:5]}")
    print(f"Longitude * Latitude (first 5): {multiplication[:5]}")
    print(f"Longitude / Latitude (first 5): {division[:5]}")
    
    print("\n" + "="*60)
    print("FAST FOOD RESTAURANTS - Trigonometric Functions (First 5 values)")
    print("="*60)
    
    # Prepare price for trigonometric functions
    price_pie = (price_sample / np.pi) + 1
    
    # Trigonometric functions
    sine_values = np.sin(price_pie)
    cosine_values = np.cos(price_pie)
    tangent_values = np.tan(price_pie)
    
    print(f"Sine values: {sine_values}")
    print(f"Cosine values: {cosine_values}")
    print(f"Tangent values: {tangent_values}")
    
    print("\n" + "="*60)
    print("FAST FOOD RESTAURANTS - Exponential and Logarithmic Functions (First 5 values)")
    print("="*60)
    
    # Exponential and logarithmic functions
    print(f"Exponential values: {np.exp(price_pie)}")
    
    # Handle negative values for logarithm
    price_pie_positive = np.abs(price_pie)  # Ensure positive values for log
    log_array = np.log(price_pie_positive)
    log10_array = np.log10(price_pie_positive)
    
    print(f"Natural logarithm values: {log_array}")
    print(f"Base-10 logarithm values: {log10_array}")
    
    print("\n" + "="*60)
    print("FAST FOOD RESTAURANTS - Hyperbolic Functions (First 5 values)")
    print("="*60)
    
    # Hyperbolic functions
    sinh_values = np.sinh(price_pie)
    cosh_values = np.cosh(price_pie)
    tanh_values = np.tanh(price_pie)
    asinh_values = np.arcsinh(price_pie)
    
    print(f"Hyperbolic Sine values: {sinh_values}")
    print(f"Hyperbolic Cosine values: {cosh_values}")
    print(f"Hyperbolic Tangent values: {tanh_values}")
    print(f"Inverse Hyperbolic Sine values: {asinh_values}")
    
    print("\n" + "="*60)
    print("FAST FOOD RESTAURANTS - 2D Array Operations")
    print("="*60)
    
    # Create 2D array from coordinates
    d2_coords = np.array([long, lat])
    
    print(f"2D Coordinates array shape: {d2_coords.shape}")
    print(f"2D Coordinates array dimensions: {d2_coords.ndim}")
    print(f"Total elements in 2D array: {d2_coords.size}")
    print(f"2D Coordinates array data type: {d2_coords.dtype}")
    
    # Slicing operations (show first few columns)
    slice_1 = d2_coords[:1, :5]
    slice_2 = d2_coords[:1, 4:15:4]
    
    print(f"\nSlicing operations:")
    print(f"d2_coords[:1, :5]: {slice_1}")
    print(f"d2_coords[:1, 4:15:4]: {slice_2}")
    
    # Indexing
    if slice_1.size > 0 and slice_2.size > 2:
        print(f"\nIndexing operations:")
        print(f"Element at [0,1] in first slice: {slice_1[0, 1] if slice_1.shape[1] > 1 else 'N/A'}")
        print(f"Element at [0,2] in second slice: {slice_2[0, 2] if slice_2.shape[1] > 2 else 'N/A'}")
    
    print(f"\nIterating through 2D array (first 10 elements):")
    for i, elem in enumerate(np.nditer(d2_coords)):
        if i < 10:
            print(f"Element {i}: {elem:.6f}")
        else:
            break
    
    # Reshape operation
    d2_reshaped = np.reshape(d2_coords, (1, -1))
    print(f"\nReshaped array (first 10 elements): {d2_reshaped[:, :10]}")
    print(f"Reshaped array size: {d2_reshaped.size}")
    print(f"Reshaped array dimensions: {d2_reshaped.ndim}")
    print(f"Reshaped array shape: {d2_reshaped.shape}")
    
    # Additional statistics about the dataset
    print("\n" + "="*60)
    print("FAST FOOD RESTAURANTS - Dataset Overview")
    print("="*60)
    
    # Count unique restaurant chains
    if 'name' in df.columns:
        top_chains = df['name'].value_counts().head(10)
        print(f"\nTop 10 Fast Food Chains:")
        for chain, count in top_chains.items():
            print(f"  {chain}: {count} locations")
    
    # Geographic distribution
    print(f"\nGeographic Range:")
    print(f"  Latitude range: {np.min(lat):.4f} to {np.max(lat):.4f}")
    print(f"  Longitude range: {np.min(long):.4f} to {np.max(long):.4f}")
    
    # Count by state if province column exists
    if 'province' in df.columns:
        top_states = df['province'].value_counts().head(10)
        print(f"\nTop 10 States by Restaurant Count:")
        for state, count in top_states.items():
            print(f"  {state}: {count} locations")
    
except FileNotFoundError:
    print("Error: FastFoodRestaurants.csv file not found!")
    print("Please make sure the file is in the correct directory.")
    print(f"Current working directory: {os.getcwd()}")
except Exception as e:
    print(f"An error occurred: {e}")
    print("\nTrying alternative approach...")
    
    # Alternative approach: Use python's csv module to handle problematic rows
    import csv
    
    latitudes = []
    longitudes = []
    
    try:
        with open('FastFoodRestaurants.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip header
            
            # Find latitude and longitude column indices
            try:
                lat_idx = header.index('latitude')
                long_idx = header.index('longitude')
            except ValueError:
                # If exact match not found, try case-insensitive
                header_lower = [col.lower() for col in header]
                lat_idx = header_lower.index('latitude')
                long_idx = header_lower.index('longitude')
            
            for row_num, row in enumerate(reader, 2):
                try:
                    if len(row) > max(lat_idx, long_idx):
                        lat_val = row[lat_idx].strip()
                        long_val = row[long_idx].strip()
                        
                        if lat_val and long_val:
                            latitudes.append(float(lat_val))
                            longitudes.append(float(long_val))
                except (ValueError, IndexError):
                    continue  # Skip problematic rows
        
        print(f"Successfully loaded {len(latitudes)} valid coordinates")
        
        # Convert to numpy arrays
        lat = np.array(latitudes)
        long = np.array(longitudes)
        
        # Continue with analysis...
        print("\nData loaded successfully with alternative method!")
        
    except Exception as e2:
        print(f"Alternative method also failed: {e2}")