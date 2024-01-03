class Main:
    def __init__(self) -> None:
        self.main()

    def main(self) -> None:
        try:
            input_str = input("Input -> ")
            amounts = [int(num) for num in input_str.split(',')]
            avg: int = sum(amounts) / len(amounts)
            newAmounts = [amt for amt in amounts if amt >= avg]
            print(sum(newAmounts))
            
        except ValueError:
                print("Please enter a number!")

if __name__== '__main__':
    Main()