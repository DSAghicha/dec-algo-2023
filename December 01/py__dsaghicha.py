class Main:
    def __init__(self) -> None:
        self.main()

    def main(self):
        numberOfPlayers = input("Enter number of players -> ")
        try:
            length = int(numberOfPlayers)
            scores = list(map(int, input(f"Enter scores of {numberOfPlayers} players (space-separated numbers) -> ").split()))
            if len(scores) != length:
                print(f"Expected {length} scores! Got {len(scores)} scores.")
                exit(-1)
            print(f"Total score of team is {sum(scores)}")
            print(f"Maximum score is {max(scores)} scored by player at index {scores.index(max(scores))}.")        

        except ValueError:
                print("Please enter a number!")

if __name__== '__main__':
    Main()