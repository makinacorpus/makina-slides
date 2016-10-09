class ParamIterator:

    def __init__(self, csv_str):
        self.csv_str = csv_str
        self.position = 0
        self.done = False

    def __next__(self):
        if self.done:
            raise StopIteration
        comma_position = self.csv_str.find(",", self.position)
        if comma_position == -1:
            self.done = True
            return self.csv_str[self.position:]
        else:
            result = self.csv_str[self.position:comma_position]
            self.position = comma_position + 1
            return result

if __name__ == "__main__":
    it = ParamIterator("one,two,three")
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
