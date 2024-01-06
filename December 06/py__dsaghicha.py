
class Main:
    def __init__(self) -> None:
        self.main()
    
    def main(self) -> None:
        ancientScroll: list[str] = []
        wordsInput = input("Enter comma separated words -> ")
        encodedWords = [word.strip() for word in wordsInput.split(',')]
        for currWord, nextWord in zip(encodedWords, encodedWords[1:]):
            self.uniquePattern(currWord, nextWord) and ancientScroll.append(currWord)
        
        print(ancientScroll or "No valid chain.")
    
    def uniquePattern(self, currWord: str, nextWord: str)-> bool:
        return sum(charCombo != nextCharCombo for charCombo, nextCharCombo in zip(currWord, nextWord)) == 1



if __name__== '__main__':
    Main()