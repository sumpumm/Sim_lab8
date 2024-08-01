import numpy as np

# Simplified function to get t-critical value for 95% confidence level and common degrees of freedom
def get_t_critical_value(n):
    # Approximate t-critical values for 95% confidence level
    t_critical_values = {
        1: 12.71, 2: 4.30, 3: 3.18, 4: 2.78, 5: 2.57,
        6: 2.45, 7: 2.36, 8: 2.31, 9: 2.26, 10: 2.23,
        11: 2.20, 12: 2.18, 13: 2.16, 14: 2.14, 15: 2.13,
        16: 2.12, 17: 2.11, 18: 2.10, 19: 2.09, 20: 2.09,
        25: 2.06, 30: 2.04, 40: 2.02, 50: 2.01, 60: 2.00,
        80: 1.99, 100: 1.98, 1000: 1.96
    }
    # Return the closest value from the table
    return t_critical_values[min(t_critical_values.keys(), key=lambda k: abs(k - n))]

def calculate_confidence_interval(sample, confidence_level=0.95):
    # Calculate sample mean
    sample_mean = np.mean(sample)
    
    # Calculate sample standard deviation
    sample_std = np.std(sample, ddof=1)  # ddof=1 provides sample standard deviation
    
    # Sample size
    n = len(sample)
    
    # Get the t-critical value for the given sample size
    t_critical = get_t_critical_value(n)
    
    # Calculate the margin of error
    margin_of_error = t_critical * (sample_std / np.sqrt(n))
    
    # Calculate the confidence interval
    confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
    
    return confidence_interval

# Example usage
sample = [12, 15, 14, 10, 13, 15, 16, 14, 12, 11]

confidence_interval = calculate_confidence_interval(sample)

print(f"Confidence Interval: {confidence_interval}")
