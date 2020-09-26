class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.age = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage.remove(self.storage[self.age])
            self.storage.insert(self.age, item)
            if self.age + 1 < self.capacity:
                self.age +=1
            else:
                self.age = 0

    def get(self):
        return self.storage

ring_buffer = RingBuffer(3)
print(ring_buffer.get())
ring_buffer.append('a')
ring_buffer.append('b')
ring_buffer.append('c')
print(ring_buffer.get())
ring_buffer.append('d')
print(ring_buffer.get())
ring_buffer.append('e')
ring_buffer.append('f')
print(ring_buffer.get())
ring_buffer.append('g')
print(ring_buffer.get())

ring_buffer_numbers= RingBuffer(5)
for i in range(50):
    ring_buffer_numbers.append(i)
print(ring_buffer_numbers.get())