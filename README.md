# X-ray Attenuation Calculator

A simple interactive Python tool that calculates X-ray intensity attenuation through various materials, based on the Beer-Lambert law.

## About

This calculator models how X-ray radiation intensity decreases as it passes through matter — a foundational concept in medical physics and radiology. It supports multiple materials with different attenuation coefficients (μ), and lets users run repeated calculations without restarting the program.

## Physics Background

The attenuation of X-rays follows the exponential law:

I = I₀ × e^(−μx)

Where:
- I₀ = initial X-ray intensity
- I = intensity after passing through the material
- μ = linear attenuation coefficient (material-specific)
- x = material thickness (cm)

## Features

- Interactive command-line input
- Built-in material database (lead, aluminum, water, bone)
- Repeat calculations without restarting
- Clear, readable output

## How to Run

```bash
python src/calculator.py
```
## Example
```
Enter initial X-ray intensity: 100
Available materials: ['lead', 'aluminum', 'water', 'bone']
Enter material name: lead
Enter material thickness (cm): 2
Final X-ray intensity through lead: 4.978706836786395
```
## Technologies Used

- Python 3
- Built-in math module

## Author

Harish Ragav S
