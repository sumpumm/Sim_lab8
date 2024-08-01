import numpy as np

def calculate_point_estimation_and_bias(sample, population_mean):
    # Calculate sample mean (point estimation)
    sample_mean = np.mean(sample)
    
    # Calculate bias
    bias = sample_mean - population_mean
    
    return sample_mean, bias

# Example usage
sample = [12, 15, 14, 10, 13, 15, 16, 14, 12, 11]
population_mean = 13  # Given population mean

sample_mean, bias = calculate_point_estimation_and_bias(sample, population_mean)

print(f"Sample Mean (Point Estimation): {sample_mean}")
print(f"Bias: {bias}")
