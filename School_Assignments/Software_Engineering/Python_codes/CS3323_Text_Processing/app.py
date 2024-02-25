"""
Kyumin Lee
CS3323
Homework6
"""

import re

#	Reading the file
with open('test_case_1.txt', 'r') as file:
  data = file.read()

"""
  RegEx:
  r''			    : raw String
  \s+			    : one or more white space
  (\d{9})	  	: 9 digits
  (\d+)		    : one or more digits
  ([A-Za-z]+)	: one or more A to Z and a to z
  ([EL])		  : E or L

  (?:\s+[A-Za-z\s]+)?
    ?:				    : doesn't captures
    ([A-Za-z/s]+)	: one or more A to Z and a to z and white spce
    ?			      	: optional
"""
pattern = r'(\d{9})\s+([A-Za-z]+)\s+([A-Za-z]+)\s+(\d+)\s+([EL])(?:\s+[A-Za-z\s]+)?'
records = re.findall(pattern, data.replace('\n', ' '))

# Converting ID and score to integers and putting into tuples in a list
records = [(int(ID), first, last, int(score), eagerness) for ID, first, last, score, eagerness in records]

#	Ranking the grades
n = len(records)
a_cutoff = n // 3	    	# //  : floor division
b_cutoff = 2 * n // 3
f_cutoff = -(-n // 10)  # -(- a // b)	: Ceiling division

# Assigning raked grades
"""
  first, it sorts the record by grade in decending order, if tied the eagerness breaks the tie
  second, enumerated for loop checks the ranking and the list comprehension gives each student the appropriate grades.
"""
records = [
  (ID, first, last,
   'A' if i < a_cutoff else
   'B' if i < b_cutoff else
   'F' if i >= n - f_cutoff else
   'C' if eagerness == 'E' else
   'D')
   for i, (ID, first, last, score, eagerness)
   in enumerate( 
    sorted(records, key=lambda x: (-x[3], x[4])))
]

# Sorting by last name, first name then ID
records.sort(key=lambda x: (x[2], x[1], x[0]))

# Generating HTML table
html_output = '<table>\n<tr><th>ID</th><th>First Name</th><th>Last Name</th><th>Grade</th></tr>\n' + \
    ''.join([f'<tr><td>{ID}</td><td>{first}</td><td>{last}</td><td>{grade}</td></tr>\n' for ID, first, last, grade in records]) + \
    '</table>'

# Writing to output.html
with open('output.html', 'w') as file:
  file.write(html_output)