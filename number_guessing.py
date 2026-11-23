import random
def num_to_guess():
    num_to_guess=random.randint(1,100)
    attempts=0
    while True:
        try:
            guess=int(input("Enter a guess:"))
            attempts+=1
            if guess<num_to_guess:
                print("too low, try again")
            elif guess>num_to_guess:
                print("too high, try again")
            else:
                print(f"Congrats you took {attempts} attempts")
                break
        except ValueError:
            print("Enter valid number")
if __name__=="__main__":
    num_to_guess()