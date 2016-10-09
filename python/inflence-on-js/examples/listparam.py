class ListParam:

    def __init__(self, csv_str):
        self.csv_str = csv_str
        self.params = self.csv_str.split(",")

    def __str__(self):
        return self.csv_str

    def __iter__(self):
        return iter(self.params)
