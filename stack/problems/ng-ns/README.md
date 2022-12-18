Nearest Greatest element to the right

2 approaches:

1. Brute force
   1. Start i with first index
   2. Start j with next index and traverse right to find the greater element


2. Using a stack

   Given Array = arr =
    _ _ _ _ _ _ _
   1 2 3 4 5 6 7

   The idea is:
   For any element i, we want to get the array to the right of i and traverse it

   Understanding the concept:  
   Concept Step 1:
   1. For every element i, get the array to the right of this element i.  
      For element 6, array to the right = 7   (add to stack)
      For element 5, array to the right = 6,7 (add to stack)
      For element 4, array to the right = 5,6,7  (add to stack)
      For element 3, array to the right = 4,5,6,7  (add to stack)
   2. Go through this array in each iteration, and find the greatest element  
      Complete code for the above first.

   Concept Step 2:
   1. For every element i, get the array to the right of this element i.  
      For element 6, array to the right = 7  (add to stack)
      For element 5, array to the right = 6,7  (add to stack)
      For element 4, array to the right = 5,6,7  (add to stack)
      For element 3, array to the right = 4,5,6,7  (add to stack)
   2. Go through this array, and find the greatest element
   3. Now, for element = i element to the right = iri element to the left = ili if i > iri, then all ili > iri see
      example

      Eg. element = 5 element to the right = 6 element to the left = 4 if 5 > 6, this is true for element 4 Thus, 6 is
      redundant for element 4

      element = 3 element to the right = 4 element to the left = 2 if 3 > 4, this is true for element 2 Thus, 4 is
      redundant for element 2

   Write code for the above.            