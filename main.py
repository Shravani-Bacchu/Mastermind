import random as rnd



num = rnd.randrange(1000, 10000)

n = int(input("Guess the 4 digit number: "))

if n == num:
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    ctr = 1  

    while n != num:
        count = 0
        n_str = str(n)
        num_str = str(num)

        correct = ['X'] * 4

        for i in range(4):
            if n_str[i] == num_str[i]:
                count += 1
                correct[i] = n_str[i]

        if count > 0:
            print(f"Not quite the number. But you did get {count} digit(s) correct!")
            print("Correct digits so far: " + " ".join(correct))
        else:
            print("None of the numbers in your input match.")

        print()
        n = int(input("Enter your next choice of numbers: "))
        ctr += 1
    again = input("\nWould you like to play again? (y/n): ").lower()
    if again == 'n':
        print("Thanks for playing! Goodbye 👋")
        