from collections import defaultdict

class Input():
    def __init__(self, source, size):
        self.record = defaultdict(str)
        self.source = source
        self.buffer = ""
        self.size = size

    def read(self, source):
        if self.buffer:
            item = self.buffer
            self.buffer = ""
        else:
            item = self.source.read(self.size)
        self.record[source] += item
        return item

    def commit(self, source):
        if self.record[source]:
            del self.record[source]
            return True
        return False
    
    def cancel(self, source):
        if source not in self.record:
            return False
        self.buffer += self.record[source]
        del self.record[source]
        return True
   
