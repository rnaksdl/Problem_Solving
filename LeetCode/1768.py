'''
1768. Merge Strings Alternately
You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
'''

# this solution only works when word2 is longer
class Attempt1:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        position = 0
        result = ""
        
        while position < len(word1):
            result += word1[position]
            result += word2[position]
            position += 1
        
        while position < len(word2):
            result += word2[position]
            position += 1
        
        return result
    
# fixed the attepmt1's issue by checking which one's longer and handling them differently in each case
class Attempt2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        position = 0
        result = ""
        
        if len(word1) >= len(word2):
            for i, char in enumerate(word2):
                result += word1[i]
                result += word2[i]
                position += 1
            for i in range(position, len(word1)):
                result += word1[i]
            return result
        
        if len(word1) < len(word2):
            for i, char in enumerate(word1):
                result += word1[i]
                result += word2[i]
                position += 1
            for i in range(position, len(word2)):
                result += word2[i]
            return result
        
'''
this solution is very similar to my solution.
but it utilizes array
    appending stings as characters to an array is more efficient than appending strings
and I was thinking about how to not check the length of word1 and word2
this solution fixes it by
    having i and j incremented together
    and stop looping when either of them are at the end of the word
    then append whatever is left in word1 or word2 from i or j to the end
then "".join(result)
    joins all the characters in the array
    "" is the delimiter, meaning "" will be in between characters when appending
'''
class Others:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        result = []
        
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[i])
            i += 1
            j += 1
        result.append(word1[i:])
        result.append(word2[j:])


        return "".join(result)

    

attempt1 = Attempt1()
print(attempt1.mergeAlternately("ab", "pqrs") == "apbqrs")

attempt2 = Attempt2()
print(attempt2.mergeAlternately("abcd", "pq") == "apbqcd")

others = Others()
print(others.mergeAlternately("abcd", "pq") == "apbqcd")