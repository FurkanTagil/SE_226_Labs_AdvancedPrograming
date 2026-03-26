num = int(input("Please enter the number of tasks: "))
#print(type(num)

tasks = {}

for x in range(num):
    taskName = input("Enter task name: ")
    numberOfDep = int(input("How many dependencies for " + taskName + "? "))

    depList = []
    
    for x in range(numberOfDep):
        print("Enter dependency ",(x+1), ": ")
        dep = input()
        depList.append(dep)

    tasks[taskName] = depList


print("TASK STRUCTURE:")
for task in tasks:
    print(task, '->', tasks[task])

print('INITIAL TASKS (no dependencies):')
initial = []

for task in tasks:
    if len(tasks[task]) == 0:
        print(task)
        initial.append(task)

if not initial:
    print('None')


completed = set()
execution_order = []

print('EXECUTION ORDER:')
step = 1

while len(completed) < len(tasks):
    progress = False

    for task in tasks:
        if task not in completed:
            can_execute = True
            for dep in tasks[task]:
                if dep not in completed:
                    can_execute = False
                    break
            
            if can_execute:
                print(f"Step {step}: {task}")
                execution_order.append(task)
                completed.add(task)
                step += 1
                progress = True
    
    if not progress:
        break

if len(completed) != len(tasks):
    print("No task can be started." if len(completed) == 0 else "")
    print("ERROR: Circular dependency detected!")
    print("These tasks could not be completed:")
    for task in tasks:
        if task not in completed:
            print(task)
else:
    print("ALL TASKS COMPLETED SUCCESSFULLY")