import tkinter as tk
from tkinter import messagebox
import random

stoic_quotes = [
    "The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "Wealth consists not in having great possessions, but in having few wants. - Epictetus",
    "It is not events that disturb people, it is their judgments concerning them. - Epictetus",
    "The soul becomes dyed with the color of its thoughts. - Marcus Aurelius",
    "No man is free who is not master of himself. - Epictetus",
    "Waste no more time arguing about what a good man should be. Be one. - Marcus Aurelius",
    "He who indulges in empty fears earns himself real fears. - Seneca",
    "What we fear doing most is usually what we most need to do. - Tim Ferriss",
    "The greater the difficulty, the more glory in surmounting it. - Epictetus",
    "The only way to happiness is to cease worrying about things which are beyond the power of our will. - Epictetus",
    "The mind that is anxious about future events is miserable. - Seneca",
    "Difficulties strengthen the mind, as labor does the body. - Seneca",
    "He is a wise man who does not grieve for the things which he has not, but rejoices for those which he has. - Epictetus",
    "It is not the man who has too little, but the man who craves more, that is poor. - Seneca",
    "Wealth consists in not having great possessions, but in having few wants. - Epictetus",
    "Caretake this moment. Immerse yourself in its particulars. Respond to this person, this challenge, this deed. - Epictetus",
    "If you want to improve, be content to be thought foolish and stupid. - Epictetus",
    "The soul becomes dyed with the color of its thoughts. - Marcus Aurelius",
    "The greatest obstacle to living is expectancy, which hangs upon tomorrow and loses today. - Seneca",
    "The key is to keep company only with people who uplift you, whose presence calls forth your best. - Epictetus",
    "You have power over your mind - not outside events. Realize this, and you will find strength. - Marcus Aurelius",
    "The only wealth which you will keep forever is the wealth you have given away. - Marcus Aurelius",
    "No person has the power to have everything they want, but it is in their power not to want what they don't have, and to cheerfully put to good use what they do have. - Seneca",
    "Happiness and freedom begin with a clear understanding of one principle: Some things are within our control, and some things are not. - Epictetus",
    "He who fears death will never do anything worthy of a living man. - Seneca",
    "True happiness is to enjoy the present, without anxious dependence upon the future. - Seneca",
    "To live a good life: We have the potential for it. If we can learn to be indifferent to what makes no difference. - Marcus Aurelius",
    "It is not the man who has too little, but the man who craves more, that is poor. - Seneca",
    "Everything we hear is an opinion, not a fact. Everything we see is a perspective, not the truth. - Marcus Aurelius",
    "The impediment to action advances action. What stands in the way becomes the way. - Marcus Aurelius",
]

compliments = [
    "You're a great listener.",
    "You have impeccable manners.",
    "Your positivity is infectious.",
    "You're incredibly thoughtful.",
    "You have a great sense of humor.",
    "You're a fantastic friend.",
    "Your kindness is a balm to all who encounter it.",
    "You're more helpful than you realize.",
    "You have the best laugh.",
    "You're an awesome friend.",
]

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "How does a penguin build its house? Igloos it together!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "What did one wall say to the other wall? I'll meet you at the corner!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What do you call a fish wearing a bowtie? Sofishticated!",
]

motivations = [
    "Believe you can and you're halfway there. -Theodore Roosevelt",
    "The only way to do great work is to love what you do. -Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. -Winston Churchill",
    "It does not matter how slowly you go as long as you do not stop. -Confucius",
    "The only limit to our realization of tomorrow will be our doubts of today. -Franklin D. Roosevelt",
    "The journey of a thousand miles begins with one step. -Lao Tzu",
    "Don't watch the clock; do what it does. Keep going. -Sam Levenson",
    "You are never too old to set another goal or to dream a new dream. -C.S. Lewis",
    "Quality is not an act, it is a habit. -Aristotle",
    "You are never too old to set another goal or to dream a new dream. -C.S. Lewis",
]

random_facts = [
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
    "The only letter that doesn't appear in any U.S. state name is Q.",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
    "If you shuffled a deck of cards every second, it would take approximately 1.3 × 10^17 years to shuffle them into a new order.",
    "The dot over the letter 'i' is called a tittle.",
    "The national animal of Scotland is the unicorn.",
    "The first oranges weren’t orange.",
    "The 'Windy City' name has nothing to do with Chicago weather. It was first used by 19th-century journalists to describe the city’s residents as 'full of hot air'.",
    "Pineapples used to be so expensive that they were rented out for parties as a display of wealth.",
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible."
]

def generate_stoic_quote():
    return random.choice(stoic_quotes)

def generate_compliment():
    return random.choice(compliments)

def generate_joke():
    return random.choice(jokes)

def generate_motivation():
    return random.choice(motivations)

def generate_random_fact():
    return random.choice(random_facts)

def show_quote():
    quote = generate_stoic_quote()
    messagebox.showinfo("Stoicism Quote", quote)

def show_compliment():
    compliment = generate_compliment()
    messagebox.showinfo("Compliment", compliment)

def show_joke():
    joke = generate_joke()
    messagebox.showinfo("Joke", joke)

def show_motivation():
    motivation = generate_motivation()
    messagebox.showinfo("Motivation", motivation)

def show_random_fact():
    random_fact = generate_random_fact()
    messagebox.showinfo("Random Fact", random_fact)

def main():
    root = tk.Tk()
    root.title("Quote Generator")

    label = tk.Label(root, text="Welcome to the Quote Generator!")
    label.pack(pady=10)

    quote_button = tk.Button(root, text="Stoic Quote \U0001F4AC", command=show_quote)
    quote_button.pack(pady=5)

    compliment_button = tk.Button(root, text="Compliment \U0001F64C", command=show_compliment)
    compliment_button.pack(pady=5)

    joke_button = tk.Button(root, text="Joke \U0001F602", command=show_joke)
    joke_button.pack(pady=5)

    motivation_button = tk.Button(root, text="Motivation \U0001F4AA", command=show_motivation)
    motivation_button.pack(pady=5)

    fact_button = tk.Button(root, text="Random Fact \U0001F914", command=show_random_fact)
    fact_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
