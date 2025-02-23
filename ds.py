def logical_operations(p, q):
   
    conjunction = p and q

  
    disjunction = p or q


   
    conditional = (not p) or q

   
    biconditional = p == q

    return conjunction, disjunction, conditional, biconditional

def truth_value(text):
    while True:
        try:
            value = int(input(text))
            if value not in [0, 1]:
                raise ValueError("Input must be 0 or 1.")
            return bool(value)
        except ValueError as e:
            print(f"Error found: {e}. You must enter 0 for False or 1 for True.")


p = truth_value("Enter truth value for p (0 for False, 1 for True): ")
q = truth_value("Enter truth value for q (0 for False, 1 for True): ")


conjunction, disjunction, conditional, biconditional = logical_operations(p, q)


print(f"Conjunction (p AND q): {conjunction}")
print(f"Disjunction (p OR q): {disjunction}")
print(f"Conditional (p → q): {conditional}")
print(f"Biconditional (p ↔ q): {biconditional}")