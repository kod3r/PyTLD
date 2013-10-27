from Date import Date


class TLDList:
    start, end, count, tlds = 0, 0, 0, {}

    def __init__(self, start, end):
        self.start, self.end = Date(start), Date(end)

    def addtld(self, tld, date):
        if date.compareto(self.start) != -1 and date.compareto(self.end) != 1:
            self.tlds[tld] = self.tlds.get(tld, 0) + 1
            self.count += 1

    def getcount(self):
        return self.count

    def gettldcount(self, tld):
        return self.tlds.get(tld, 0)