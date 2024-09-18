import random
class RandomList(list):
    def get_random_element(self):
        if not self:
            raise IndexError("list is emty")
        random_index = random.randint(0, len(self) - 1)
        return self.pop(random_index)
    
listt = RandomList([1, 2, 3, 4, 5, 6])
print(listt.get_random_element())
print(listt)