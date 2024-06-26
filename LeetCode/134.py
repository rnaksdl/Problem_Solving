'''
134. Gas Station

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
'''


class Attempt1:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        sum = 0
        maxMargin = -999999999999
        result = -1

        for i in range(len(gas)):

            diff = gas[i] - cost[i]

            sum += diff

            if maxMargin < diff:
                result = i


        if sum >= 0 :
            return result
        else: return -1
        
'''
I need to figure out why its index is off by one
'''

class Attempt2:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        sum = 0
        maxMargin = -999999999999
        result = -1

        for i in range(len(gas)):

            margin = gas[i] - cost[i]

            sum += margin

            if maxMargin < margin:
                maxMargin = margin
                result = i


        if sum >= 0 :

            return result
        else: return -1

'''
this works with the given test cases, but my assumption that if you start with the most gas possible, you'll be able to circle around from that spot,
is a weak assumption..
'''


class Attempt2:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        result = -1
        maxMarginToNext = -99999999999

        for i in range(len(gas)):
            if i != len(gas) - 1 :
                margin = gas[i] - cost[i]

                if margin > 0:
                    marginToNext = margin + gas[i+1] - cost[i+1]
                    if marginToNext > 0 and maxMarginToNext < marginToNext:
                        maxMarginToNext = marginToNext
                        result = i

            else:
                margin = gas[i] - cost[i]

                if margin > 0:
                    marginToNext = margin + gas[0] - cost[0]
                    if marginToNext > 0 and maxMarginToNext < marginToNext:
                        maxMarginToNext = marginToNext
                        result = i

        return result

'''
hahaha.. passed the given testcases, but
'''