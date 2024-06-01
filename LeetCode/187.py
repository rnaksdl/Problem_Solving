'''
187. Repeated DNA Sequences

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
'''

class Attempt:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        sequences = set()
        result = []

        for l in range(len(s) - 9):
            currentSequence = s[l:l+10]
            if currentSequence in sequences:
                result.append(currentSequence)

            sequences.add(currentSequence)

        return result
    
'''
result must be a set too
'''