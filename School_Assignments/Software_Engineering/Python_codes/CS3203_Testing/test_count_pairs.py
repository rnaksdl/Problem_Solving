def count_pairs(numbers, target):
    num_set = set()
    pair_count = 0
    
    for num in numbers:
        complement = target - num
        if complement in num_set:
            pair_count += 1
            num_set.remove(complement)
        else:
            num_set.add(num)
            
    return pair_count

import io
import unittest

class CustomTextTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_outcomes = []
    
    def addSuccess(self, test):
        super().addSuccess(test)
        self.test_outcomes.append({"test_name": str(test), "status": "Success"})
    
    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.test_outcomes.append({"test_name": str(test), "status": "Failure"})
        
    def addError(self, test, err):
        super().addError(test, err)
        self.test_outcomes.append({"test_name": str(test), "status": "Error"})

class CustomTextTestRunner(unittest.TextTestRunner):
    resultclass = CustomTextTestResult

class TestCountPairs(unittest.TestCase):
    
    def test_non_empty_list_valid_target(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 6), 2)
        
    def test_non_empty_list_no_valid_pairs(self):
        self.assertEqual(count_pairs([1, 2, 3], 10), 0)
        
    def test_empty_list(self):
        self.assertEqual(count_pairs([], 5), 0)
        
    def test_list_with_one_element(self):
        self.assertEqual(count_pairs([1], 1), 0)
        
    def test_list_with_repeated_elements(self):
        self.assertEqual(count_pairs([1, 2, 2, 3], 3), 1)
        
    def test_target_itself_in_list(self):
        self.assertEqual(count_pairs([5, 1, 4], 5), 1)
        
    def test_list_with_negative_numbers(self):
        self.assertEqual(count_pairs([-1, 1, 2], 1), 1)
        
    def test_list_with_zero_and_target(self):
        self.assertEqual(count_pairs([0, 5], 5), 1)
        
    def test_list_with_multiple_valid_pairs_for_same_number(self):
        self.assertEqual(count_pairs([1, 2, 2, 1, 3], 3), 2)

# Run the unit tests and capture the results
stream = io.StringIO()
runner = CustomTextTestRunner(stream=stream)
result = runner.run(unittest.TestLoader().loadTestsFromTestCase(TestCountPairs))

# Display the results
result.test_outcomes
