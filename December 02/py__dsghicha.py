# arr = [2, 3, 2, 5, 4, 5, 2, 5,3]
# a = set(arr)
# for i in a:
#     print(f"{i} {arr.count(i)}")


class Main:
    def __init__(self) -> None:
        self.main()

    def main(self) -> None:
        try:
            input_str = input("Input -> ")
            numbers = [int(num) for num in input_str.split(',')]
            # print(f"Number {numbers}")
            unique_num = self.get_unique_list(numbers)
            # print(f"Unique {unique_num}")
            num_count: list[int] = []
            for i in unique_num:
                # print(f"Frequency of {i}: {numbers.count(i)}")
                num_count.append(numbers.count(i))
            print(num_count)

        except ValueError:
                print("Please enter a number!")
    
    def get_unique_list(self, list: list[int])-> list[int]:
        unique_list  = []
        for item in list:
            if item not in unique_list:
                unique_list.append(item)
        return unique_list 

if __name__== '__main__':
    Main()