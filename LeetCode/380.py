'''
380. Insert Delete GetRandom O(1)

Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
'''

class RandomizedSet:

    def __init__(self):

        # init hashmap to handle duplicates, insert, remove
        self.numMap = {}
        # init list to handle random
        self.numList = []

    def insert(self, val: int) -> bool:

        valNotInMap = val not in self.numMap

        # if we don't have val
        if valNotInMap:
            # setting the val as the key and the length of the list as the value
            self.numMap[val] = len(self.numList)
            # appending the val to the end of the list
            self.numList.append(val)

        return valNotInMap

    def remove(self, val: int) -> bool:

        valInMap = val in self.numMap

        # if we have val
        if valInMap:

            # setting index
            index = self.numMap[val]

            # setting lastVal
            lastVal = self.numList[-1]

            # swap lastVal and val
            self.numList[index] = lastVal

            # pop the val (which is now at the end)
            self.numList.pop()

            # edit the lasVal value as the index
            self.numMap[lastVal] = index

            # delete the val
            del self.numMap[val]

        return valInMap

    def getRandom(self) -> int:

        # this returns a random available index in a list
        return random.choice(self.numList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

'''
I'm not 
'''