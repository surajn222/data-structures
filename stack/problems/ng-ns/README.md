Nearest Greatest element to the right

2 approaches:

1. Brute force
    1. Start i with first index
    2. Start j with next index and start moving right to find the greater element


2. Using a stack

   Given Array = arr =
    _ _ _ _ _ _ _
   1 2 3 4 5 6 7

   Understanding the concept:
   Concept Step 1:
   1. For every element i, get the array to the right of this element i.  
   For element 6, array to the right = 7  
   For element 5, array to the right = 6,7  
   For element 4, array to the right = 5,6,7  
   For element 3, array to the right = 4,5,6,7  
   2. Go through this array, and find the greatest element  
   Write code for this first. Concept Step 2:
            