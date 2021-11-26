    if guessed_letter.lower() in chosen.lower():
            for i in range(len(chosen)):
                if chosen[i].lower() == guessed_letter.lower():
                    revealed = revealed[:i] + guessed_letter + revealed[i+1:]
            
            print ("\nCorrect")
        else:
            print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
            print(stages[counter])
            counter += 1