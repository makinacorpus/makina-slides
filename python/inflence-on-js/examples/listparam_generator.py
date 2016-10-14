class ListParam:

    def __init__(self, csv_str):
        self.csv_str = csv_str

    def __str__(self):
        return self.csv_str

    def __iter__(self):
        position = 0
        comma_position = self.csv_str.find(",", position)
        while comma_position != -1:
            yield self.csv_str[position:comma_position]
            position = comma_position + 1
            comma_position = self.csv_str.find(",", position)
        yield self.csv_str[position:]


for param in ListParam("un,deux,trois"):
    print(param)
