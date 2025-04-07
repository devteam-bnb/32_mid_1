import statistics

def compute_statistics(data):
    print("Data:", data)
    
    # Central Tendency Measures
    mean = statistics.mean(data)
    median = statistics.median(data)
    try:
        mode = statistics.mode(data)
    except statistics.StatisticsError:
        mode = "No unique mode found"

    # Dispersion Measures
    variance = statistics.variance(data)
    std_dev = statistics.stdev(data)

    # Display Results
    print("\nCentral Tendency Measures:")
    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)

    print("\nMeasure of Dispersion:")
    print("Variance:", variance)
    print("Standard Deviation:", std_dev)

# Example usage
if __name__ == "__main__":
    sample_data = [10, 20, 20, 30, 40, 40, 40, 50, 60]
    compute_statistics(sample_data)