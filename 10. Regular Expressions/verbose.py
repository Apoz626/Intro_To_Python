import re

## add comments within regex using re.VERBOSE
re.compile(r'''
(\d\d\d-)|    # area code (without parens, with dash)
(\(\d\d\d\ )  # -or- area code with parens and no dash
\d\d\d     # first 3 digits
-          # second dash
\d\d\d\d   # last 4 digits
\sx\d[2,4] # extension, like x1234''', re.VERBOSE)

## using or operator to add multiple arguments to re.compile
re.compile(r'''
(\d\d\d-)|    # area code (without parens, with dash)
(\(\d\d\d\ )  # -or- area code with parens and no dash
\d\d\d     # first 3 digits
-          # second dash
\d\d\d\d   # last 4 digits
\sx\d[2,4] # extension, like x1234''', re.IGNORECASE | re.DOTALL | re.VERBOSE)
