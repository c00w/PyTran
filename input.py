from collections import defaultdict

class Input():
    def __init__(self):
        self.record = defaultdict(str)
        self.source = source
        self.buffer = ""

    def read(source):
        if self.buffer:
            item = self.buffer
            self.buffer = ""
        else:
            item = self.source.read()
        self.record[source] += item
        return item

    def commit(source):
        if self.record[source]:
            del self.record[source]
            return True
        return False
    
    def cancel(source):
        if source not in self.record:
            return False
        self.buffer += self.record[source]
        del self.record[source]
        return True
   
