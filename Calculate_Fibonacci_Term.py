
def retrieve_input():
    desired_term = int(input('Please enter a positive integer: '))
    return desired_term

def calculate(desired_term):    
    k = 3
    term1 = 1
    term2 = 1
    if desired_term == 1 or desired_term == 2:
        fib_sum = 1
    else:
        while k <= desired_term:
            fib_sum = term1 + term2
            term1 = term2
            term2 = fib_sum
            k += 1
    return fib_sum

def print_output(fib_sum):
    print('Term #', desired_term, 'of the Fibonacci sequence is', fib_sum)

def restart():
    start_over = input('Would you like to restart?  Please enter "yes" or "no". ')
    if start_over == "yes":
        return True
    if start_over == "no":
        return False


rerun = True
while rerun:
    desired_term = retrieve_input()
    fib_sum = calculate(desired_term)
    print_output(fib_sum)
    rerun = restart()
