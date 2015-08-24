class PageNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.val)

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = {}
        self.head = None
        self.tail = None
        self.count = 0

    # @return an integer
    def get(self, key):
        if key not in self.pages: return -1
        page = self.pages[key]
        self.moveToBack(page)
        return page.val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.pages:
            page = PageNode(key,value)
            self.pages[key] = page
            self.count += 1
            page.prev = self.tail
            self.tail = page
            self.tail.next = page
            if page.prev: page.prev.next = page
            else: self.head = self.tail
        else:
            page = self.pages[key]
            page.val = value
            self.moveToBack(page)

        if self.count > self.capacity:
            page = self.head
            self.head = page.next
            del self.pages[page.key]
            self.count -= 1

    def moveToBack(self, page):
        if page is self.tail: return
        if page is self.head:
            if self.count > 1:
                self.head = page.next
                page.next.prev = None
        else:
            page.prev.next = page.next
            if page.next: page.next.prev = page.prev
        
        page.prev = self.tail
        self.tail.next = page
        self.tail = page


lru = LRUCache(2)
lru.set(2,1)
lru.set(3,2)
lru.get(3)
lru.get(2)
# print lru.head, lru.tail
lru.set(2,3)
# print lru.head, lru.tail
lru.get(2)
print lru.pages, lru.head.next
print lru.get(3)
print lru.get(4)


