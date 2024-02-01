def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI (Body Mass Index) based on weight (in kilograms) and height (in meters).
    Formula: BMI = weight / (height^2)
    """
    bmi = weight_kg / (height_m ** 2)
    return bmi

def determine_bmi_category(bmi):
    """
    Determine the BMI category based on the calculated BMI value.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    # Input: Weight in kilograms
    weight_kg = float(input("Enter your weight in kilograms: "))

    # Input: Height in meters
    height_m = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight_kg, height_m)

    # Determine BMI category
    bmi_category = determine_bmi_category(bmi)

    # Display results
    print(f"\nBMI: {bmi:.2f}")
    print(f"Category: {bmi_category}")

if __name__ == "__main__":
    main()
