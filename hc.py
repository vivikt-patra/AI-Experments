def objective_function(x):
    return (-(x-5)**2)+25

'''for i in range(0,10):
    print(objective_function(i))'''

#hill climbing function
def hill_climbing(start, step_size, max_iterations):
    current= start
    current_value= objective_function(current)

    for i in range(max_iterations):
        left= current - step_size
        right= current + step_size

        left_value = objective_function(left)
        right_value = objective_function(right)

        #move to the better neighbour
        if left_value > current_value:
            current = left
            current_value = left_value
        elif right_value > current_value:
            current = right
            current_value = right_value
        else:
            break
    return current, current_value

#main program
start = float(input("Enter the starting value: "))
step_size = float(input("Enter the step value: "))
max_iterations = int(input("Enter maximum iterations: "))

best_position, best_value = hill_climbing(start, step_size, max_iterations)

print("\n Best Postion= ",best_position)
print("Maximum Value = ",best_value)



