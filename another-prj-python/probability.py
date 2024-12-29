import math

def simple_probability(successes, total_outcomes):
    if total_outcomes == 0:
        raise ValueError("Total outcomes must be greater than zero.")
    return successes / total_outcomes

def conditional_probability(p_a_and_b, p_b):
    if p_b == 0:
        raise ValueError("Probability of B must be greater than zero.")
    return p_a_and_b / p_b

def binomial_probability(n, k, p):
    if not (0 <= p <= 1):
        raise ValueError("Probability must be between 0 and 1.")
    coefficient = math.comb(n, k)
    return coefficient * (p ** k) * ((1 - p) ** (n - k))

def main():
    print("Probability Calculator")
    print("1. Simple Probability")
    print("2. Conditional Probability")
    print("3. Binomial Probability")
    
    choice = input("Choose the type of probability to calculate (1/2/3): ")
    
    try:
        if choice == "1":
            successes = int(input("Enter the number of successful outcomes: "))
            total_outcomes = int(input("Enter the total number of outcomes: "))
            probability = simple_probability(successes, total_outcomes)
            print(f"The simple probability is {probability:.4f}")

        elif choice == "2":
            p_a_and_b = float(input("Enter the probability of A and B (P(A \u2229 B)): "))
            p_b = float(input("Enter the probability of B (P(B)): "))
            probability = conditional_probability(p_a_and_b, p_b)
            print(f"The conditional probability P(A|B) is {probability:.4f}")

        elif choice == "3":
            n = int(input("Enter the number of trials (n): "))
            k = int(input("Enter the number of successes (k): "))
            p = float(input("Enter the probability of success on a single trial (p): "))
            probability = binomial_probability(n, k, p)
            print(f"The binomial probability is {probability:.4f}")

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
