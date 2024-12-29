import random

def random_philosopher_and_quote():
    # Dictionary of philosophers and their popular quotes
    philosophers = {
        "Socrates": "An unexamined life is not worth living.",
        "Plato": "The greatest wealth is to live content with little.",
        "Aristotle": "Knowing yourself is the beginning of all wisdom.",
        "Descartes": "I think, therefore I am.",
        "Nietzsche": "He who has a why to live can bear almost any how.",
        "Kant": "Science is organized knowledge. Wisdom is organized life.",
        "Confucius": "It does not matter how slowly you go as long as you do not stop.",
        "Lao Tzu": "The journey of a thousand miles begins with one step.",
        "Rumi": "You were born with wings, why prefer to crawl through life?",
        "Voltaire": "Judge a man by his questions rather than by his answers."
    }

    # Choose a random philosopher and their quote
    philosopher, quote = random.choice(list(philosophers.items()))
    return philosopher, quote

if __name__ == "__main__":
    philosopher, quote = random_philosopher_and_quote()
    print(f"Philosopher: {philosopher}\nQuote: \"{quote}\"")
