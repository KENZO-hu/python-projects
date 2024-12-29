import random

def generate_reaction():
    # List of common elements and compounds
    elements = ["H2", "O2", "N2", "Cl2", "C", "H2O", "CO2", "CH4", "Na", "K"]
    
    # Randomly pick reactants and products
    reactants = random.sample(elements, 2)
    products = random.sample(elements, 2)

    return reactants, products

def balance_equation(reactants, products):
    # For simplicity, this program does not truly balance equations.
    # You can expand it with balancing logic using stoichiometry.
    balanced_reaction = {
        "reactants": reactants,
        "products": products
    }
    return balanced_reaction

def display_equation(reaction):
    reactants = " + ".join(reaction["reactants"])
    products = " + ".join(reaction["products"])
    equation = f"{reactants} -> {products}"
    print("Generated Equation:", equation)

# Main function
def main():
    print("Chemical Equation Generator")
    while True:
        reactants, products = generate_reaction()
        balanced_reaction = balance_equation(reactants, products)
        display_equation(balanced_reaction)

        choice = input("Generate another equation? (y/n): ").strip().lower()
        if choice != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
