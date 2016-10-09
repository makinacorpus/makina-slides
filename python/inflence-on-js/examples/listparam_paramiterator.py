from paramiterator import ParamIterator


class ListParam:

    def __init__(self, csv_str):
        self.csv_str = csv_str

    def __str__(self):
        return self.csv_str

    def __iter__(self):
        return ParamIterator(self.csv_str)


for param in ListParam("un,deux,trois"):
    print(param)
