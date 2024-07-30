import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Step 1: Generate Synthetic Wafer Data
def generate_wafer_data(num_dies=1000):
    np.random.seed(42)
    # Synthetic parameters for each die
    temperature = np.random.normal(loc=25, scale=5, size=num_dies)
    voltage = np.random.normal(loc=1.2, scale=0.1, size=num_dies)
    current = np.random.normal(loc=50, scale=5, size=num_dies)
    frequency = np.random.normal(loc=2.0, scale=0.2, size=num_dies)
    return pd.DataFrame({'Temperature': temperature, 'Voltage': voltage, 'Current': current, 'Frequency': frequency})

# Step 2: Wafer Probing
def wafer_probing(df):
    # Simulating probing by adding a 'Tested' column
    df['Tested'] = True
    return df

# Step 3: Parametric Testing
def parametric_testing(df):
    # Adding pass/fail criteria for each parameter
    df['Voltage_Pass'] = df['Voltage'].between(1.0, 1.4)
    df['Current_Pass'] = df['Current'].between(45, 55)
    df['Frequency_Pass'] = df['Frequency'].between(1.8, 2.2)
    return df

# Step 4: Functional Testing
def functional_testing(df):
    # Simulating functional testing
    df['Functional_Pass'] = df['Voltage_Pass'] & df['Current_Pass'] & df['Frequency_Pass']
    return df

# Step 5: Burn-In Testing
def burn_in_testing(df):
    # Simulating burn-in testing by adding a stress test result
    df['Burn_In_Pass'] = df.apply(lambda row: np.random.rand() > 0.05 if row['Functional_Pass'] else False, axis=1)
    return df

# Step 6: Reliability Testing
def reliability_testing(df):
    # Simulating reliability testing by adding a reliability result
    df['Reliability_Pass'] = df.apply(lambda row: np.random.rand() > 0.1 if row['Burn_In_Pass'] else False, axis=1)
    return df

# Step 7: Die Sort and Binning
def die_sort_and_binning(df):
    # Binning based on performance metrics
    bins = pd.qcut(df['Frequency'], q=4, labels=['Low', 'Medium', 'High', 'Very High'])
    df['Performance_Bin'] = bins
    return df

# Step 8: Visualization
def visualize_data(df):
    plt.figure(figsize=(10, 6))
    colors = {'Low': 'red', 'Medium': 'yellow', 'High': 'green', 'Very High': 'blue'}
    plt.scatter(df['Voltage'], df['Frequency'], c=df['Performance_Bin'].map(colors))
    plt.xlabel('Voltage')
    plt.ylabel('Frequency')
    plt.title('Die Performance Binning')
    plt.show()

# Main function to run the simulation
def main():
    # Generate synthetic wafer data
    wafer_data = generate_wafer_data()

    # Run the probe processes
    wafer_data = wafer_probing(wafer_data)
    wafer_data = parametric_testing(wafer_data)
    wafer_data = functional_testing(wafer_data)
    wafer_data = burn_in_testing(wafer_data)
    wafer_data = reliability_testing(wafer_data)
    wafer_data = die_sort_and_binning(wafer_data)

    # Visualize the results
    visualize_data(wafer_data)

    # Display the final data
    print(wafer_data.head())

if __name__ == "__main__": 
    main()