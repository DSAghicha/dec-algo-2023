class Main:
    def __init__(self) -> None:
        self.main()
    
    def main(self) -> None:
        word = input("Enter word -> ")
        wordLen = len(word)
        smallestWord: str = None

        for i in range(wordLen):
            # print(f'SW {smallestWord}')
            for j in range(i + 1, wordLen + 1):
                newWord = word[i:j]
                if (self.isMirror(newWord) and len(newWord) > 1):
                    # print('New word -> ' + newWord)
                    if (smallestWord is None or len(newWord) < len(smallestWord)):
                        smallestWord = newWord

        print(smallestWord or "Error")

    def isMirror(self, word: str)-> bool:
        return word == word[::-1]


if __name__== '__main__':
    Main()
