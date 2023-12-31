class Main:
    def __init__(self) -> None:
        self.main()
    
    def main(self) -> None:
        try:
            n = int(input('Enter number of buildings -> '))
            heights = list(map(int, input(f'Enter heights of {n} buildings -> ').split(', ')))
            if (len(heights) != n):
                print(f"Expected height of {n} buildings! Got {len(heights)}.")
                exit(-1)
            total = 0
            for i in range(len(heights)):
                curr_height = heights[i]

                for j in range(i):
                    if heights[j] > curr_height:
                        break
                else:
                    total += 1

            print(total)
        except ValueError:
            print("Please enter a number!")


if __name__== '__main__':
    Main()
