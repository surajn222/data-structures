Resources:
https://docs.google.com/spreadsheets/d/170U9LyJJ5e57LLqNijsjtLg8FpHU8B0m1MMyqP8wuR8/edit#gid=62697856

    In the Sorted Stack Sheet, start with the easy questions.
    All questions are grouped.

Stack:  
Balanced parenthesis:

1. Balanced parenthesis
2. Balanced parenthsiss with operators
3. Number of balanced parenthesis
4. Longest expression of balanced parenthesis


1. Balanced Parenthesis:

     (    (    (    )    )    )
    __   __   __   __   __   __   
    Push Push Push Pop  Pop  Pop

2. Index of parenthesis:

             (    (    (    a    +    b    )   )   )
            __   __   __   __    __   __  __  __  __  
            Push Push Push Push Push Push Pop Pop Pop
    Inde     0     1    2    3    4    5   6   7   8
                                            While loop at 6  
                                            Go back upto 2  

3. Max depth of balanced parenthesis:

             (    (    (    a    +    b    )   )   (  a  + b  )  )
            __   __   __   __    __   __  __  __  __ __ __ __ __ __  
            Push Push Push                Pop Pop Pop         Pop Pop
    Inde     0     1    2    3    4    5   6   7   8
             +1    +1   +1                 -1   -1  -1

Push = Push to stack Pull = Pull from stack

If else clause:  
If else can always be interchanged  
If clause should be applied where condition is known Else clause to be applied where condition is not known




