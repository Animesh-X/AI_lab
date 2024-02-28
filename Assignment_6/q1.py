import sympy


def hill_climbing(eq, start, end, jmp_size):
    x = sympy.Symbol('x')
    calc_x = start
    current_value = eq.subs('x', calc_x)
    next_x = calc_x + jmp_size
    while next_x <= end:
        next_x = calc_x + jmp_size
        next_value = eq.subs('x', next_x)
        if next_value < current_value or next_x > end:
            return (calc_x, current_value)        
        calc_x = next_x
        current_value = next_value
    
    return calc_x


def main():
    
    fn = input(f"Enter the function: ")
    low = float(input(f"Enter the lower limit: "))
    high = float(input(f"Enter the higher limit: "))
    step_size = float(input(f"Enter the step size: "))
    fn = sympy.simplify(fn)
    print(hill_climbing(fn, low, high, step_size))
    

main()