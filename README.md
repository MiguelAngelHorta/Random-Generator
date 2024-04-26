# Random-Generator
This desktop app creates a tkinter GUI application that generates random stoic quotes, compliments, jokes, motivational quotes, and random facts upon button click.
![image](https://github.com/MiguelAngelHorta/Random-Generator/assets/106134627/72a9420e-0b70-4a3e-a2d2-07f018f6f661)

#### Summary of Functions:

1. **generate_stoic_quote():**
   - Returns a randomly chosen stoic quote from the `stoic_quotes` list.

2. **generate_compliment():**
   - Returns a randomly chosen compliment from the `compliments` list.

3. **generate_joke():**
   - Returns a randomly chosen joke from the `jokes` list.

4. **generate_motivation():**
   - Returns a randomly chosen motivational quote from the `motivations` list.

5. **generate_random_fact():**
   - Returns a randomly chosen random fact from the `random_facts` list.

6. **show_quote():**
   - Retrieves a stoic quote using `generate_stoic_quote()` and displays it in a message box titled "Stoicism Quote".

7. **show_compliment():**
   - Retrieves a compliment using `generate_compliment()` and displays it in a message box titled "Compliment".

8. **show_joke():**
   - Retrieves a joke using `generate_joke()` and displays it in a message box titled "Joke".

9. **show_motivation():**
   - Retrieves a motivational quote using `generate_motivation()` and displays it in a message box titled "Motivation".

10. **show_random_fact():**
    - Retrieves a random fact using `generate_random_fact()` and displays it in a message box titled "Random Fact".

11. **main():**
    - Initializes the Tkinter GUI window titled "Quote Generator".
    - Creates labels and buttons for displaying quotes, compliments, jokes, motivations, and random facts.
    - Associates each button with its respective function to display the corresponding content when clicked.
    - Enters the Tkinter event loop to handle user interactions and GUI updates.
