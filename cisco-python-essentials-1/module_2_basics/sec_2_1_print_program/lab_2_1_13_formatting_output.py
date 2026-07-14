"""Scenario : 
We strongly encourage you to play with the code we've written for you, and make some (maybe even destructive) amendments. Feel free to modify any part of the code, but there is one condition ‒ learn from your mistakes and draw your own conclusions.

Try to:

1) minimize the number of print() function invocations by inserting the \n sequence into the strings;
2) make the arrow twice as large (but keep the proportions)
3) duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring" (we'll tell you more about it soon)
4) remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error ‒ is this the place where the error really exists?
5) do the same with some of the parentheses;
6) change any of the print words into something else, differing only in case (e.g., Print) ‒ what happens now?
7) replace some of the quotes with apostrophes; watch what happens carefully.
Given :
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")         """

print("Minimizing print functions")

print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****") # arrow is printed with only one print function using \n sequence

print("Arrow twice large")

print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")

print("Duplicating the arrow")

print("        *         "*2)
print("       * *        "*2)
print("      *   *       "*2)
print("     *     *      "*2)
print("    *       *     "*2)
print("   *         *    "*2)
print("  *           *   "*2)
print(" *             *  "*2)
print("******     ****** "*2)
print("     *     *      "*2)
print("     *     *      "*2)
print("     *     *      "*2)
print("     *     *      "*2)
print("     *     *      "*2)
print("     *     *      "*2)
print("     *******      "*2)

# Removing the quotes

# print(        *        )
# print(       * *       )
# print(      *   *      ) # When we remove quotes it will give syntaxError
# print(     *     *     )
# print(    *       *    )
# print(   *         *   )
# print(  *           *  )
# print( *             * )
# print(******     ******)
# print(     *     *     )
# print(     *     *     )
# print(     *     *     )
# print(     *     *     )
# print(     *     *     )
# print(     *     *     )
# print(     *******     )

# Removing parenthesis

# print"        *         "
# print"       * *        "
# print"      *   *       "
# print"     *     *      "
# print"    *       *     " # Removing parenthesis will give syntaxError
# print"   *         *    "
# print"  *           *   "
# print" *             *  "
# print"******     ****** "
# print"     *     *      "
# print"     *     *      "
# print"     *     *      "
# print"     *     *      "
# print"     *     *      "
# print"     *     *      "
# print"     *******      "

# Changing print words into something

# Print("*")  # It will give NameError

# Changing double quotes to apostrophes

print('Ali Suleman') # Python allows to use single(apostrophes), double and triple quotes for a string