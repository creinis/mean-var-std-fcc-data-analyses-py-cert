# Mean-Variance-Standard Deviation Calculator

###### Technologies:
<p align="center">
<img src="https://img.icons8.com/color/75/000000/python.png" width="75" height="75" alt="Python" style="margin: 10px 15px 0 15px;" />
<img src="https://img.icons8.com/color/75/000000/numpy.png" width="75" height="75" alt="Numpy" style="margin: 10px 15px 0 15px;" />
</p>

### Try it!

To run the Mean-Variance-Standard Deviation Calculator application, follow the instructions in the Setup section below.

## Project Structure

- `mean_var_std.py`: Contains the implementation of the `calculate` function that performs the calculations.
- `main.py`: Used for development and testing the `calculate` function.

## Setup

### Prerequisites

- Python 3 installed
- Numpy installed

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/creinis/mean-var-std-fcc-data-analyses-py-cert.git
   cd mean-var-std-fcc-data-analysis-py-cert
   ```

2. Run the Mean-Variance-Standard Deviation Calculator script:
   ```bash
   python3 main.py
   ```

## Mean-Variance-Standard Deviation Calculator

### Functionality

The Mean-Variance-Standard Deviation Calculator computes the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

### calculate Function

#### Parameters

- `list`: A list containing 9 digits.

#### Returns

- A dictionary with the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

#### Raises

- `ValueError`: If the input list does not contain exactly 9 elements.

### Practical Use Case

This calculator is useful for statistical analysis and provides a comprehensive summary of a 3 x 3 matrix, including row-wise, column-wise, and overall statistics.

### Benefits

- **Statistical Analysis:** Quickly compute essential statistics for data analysis.
- **Python Standard Library:** Utilizes Numpy for efficient numerical calculations.

## How to Use

1. Pass a list containing 9 digits to the `calculate` function.
2. The function will return a dictionary with the calculated statistics.

### Example Usage

```python
import mean_var_std

result = mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)
```

### Example Output

```plaintext
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

### Additional Information

- **Reshaping:** Converts the list into a 3 x 3 Numpy array for calculations.
- **Comprehensive Statistics:** Computes a variety of statistical measures for thorough analysis.

---
#### This is a FreeCodeCamp Challenge for Data Analysis with Python Projects Certification.
<p align="center">
<img src="https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg" width="250" height="75" alt="freeCodeCamp" style="margin: 0 15px; opacity: 0.6" />
</p>
