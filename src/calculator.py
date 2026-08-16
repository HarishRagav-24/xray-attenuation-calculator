import math

material_mu = {
    "lead": 1.5,
    "aluminum": 0.2,
    "water": 0.15,
    "bone": 0.3
}

while True:
    initial_intensity = float(input("Enter initial X-ray intensity: "))

    print("Available materials:", list(material_mu.keys()))
    material = input("Enter material name: ").lower()
    mu = material_mu[material]

    thickness = float(input("Enter material thickness (cm): "))

    final_intensity = initial_intensity * math.exp(-mu * thickness)

    print(f"Final X-ray intensity through {material}: {final_intensity}")

    again = input("Calculate again? (yes/no): ").lower()
    if again != "yes":
        break