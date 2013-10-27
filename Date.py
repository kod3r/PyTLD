class Date:
    day, month, year = 1, 1, 1990

    def __init__(self, date):
        self.day, self.month, self.year = map(int, str(date).split("/"))

    def compareto(self, other):
        return [-1, [-1, [-1, 0, 1][cmp(self.day, other.day)+1], 1][cmp(self.month, other.month)+1], 1][cmp(self.year, other.year)+1]