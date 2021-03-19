import copy
import string
string.ascii_uppercase
global Largest_list
class Node:
    def __init__(self):
        self.state = []
        self.cost = 0
        self.parent = None
        self.action = ""
        self.heuristic = (2*disks_num)+1


class PriorityQueue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	# for checking if the queue is empty
	def isEmpty(self):
		return len(self.queue) == 0

	# for inserting an element in the queue
	def insert(self, data):
		self.queue.append(data)

	# for popping an element based on Priority
	def delete(self):
		try:
			min = 0
			for i in range(len(self.queue)):
				if self.queue[i].cost < self.queue[min].cost:
					min = i
            # item is the object with the lowest cost
			item = self.queue[min]
            # delete the item (one with the lowest cost)
			del self.queue[min]
            # and expand to its children
			return item
		except IndexError:
			print()
			exit()


def give_next(initial,heu):
    visited_before = []
    copy_init = copy.deepcopy(initial.state)

    for indx,block in enumerate(initial.state):
        copy_init = copy.deepcopy(initial.state)

        '''
        If block is empty move to the next block
        '''
        if not block: # empty?
            continue # change the block
        elif block: # full?
            packet = copy_init[indx][0]
            sender_position = indx
            # True if there is an empty sublist
            x = [True for i in initial.state if len(i) == 0]
            # Enter if there is no empty sublist
            if not any(x):
                if packet > max([0 if sublist == block  else sublist[-1] for sublist in initial.state]):
                    continue
            copy_init[indx].remove(packet)
            ''' Check the Cost to take a disk out from this stack'''

            ''' Create the action statement-phase1-'''
            act = "Move Disk "+str(packet)+" From Stack "+alphabet_list[indx]

            '''
            After this step, a disk is selected to be moved
            '''
        for indx2, position in enumerate(initial.state):
            copy_init2 = copy.deepcopy(copy_init)
            '''
        There are four cases:
        1. new postion is the old position          So Change the position
        2. position is empty                        So add at index 0
        3. position is full with elements > packet  So add at index 0
        4. position is full with elements < packet  So Change the position   
            '''
            if block == position:
                continue # Don't return the disk to the first place !!
            elif not position: # empty?
                copy_init2[indx2].insert(0,packet)

            elif position[-1] > packet:
                copy_init2[indx2].insert(0,packet)

            elif position[-1] < packet:
                continue # Not allowed movment, SO change the block

            '''
        # Check if the predicted step is in the Largest_list:
        # if YES: change the block, in a try to predict a new step
        # if  NO: add the step to the Largest_list and finish
            '''
            if copy_init2 in Largest_list:
                continue
            elif copy_init2 not in Largest_list:
                Largest_list.insert(-1, copy_init2)
                ''' Check the Cost to reach this state'''
                pay = 0
                if indx in wide_stacks and indx2 in wide_stacks:
                    pay += 4
                elif indx not in wide_stacks and indx2 not in wide_stacks :
                    pay += 2
                else:
                    pay += 3
                ''' Create the action statement-phase2-'''
                ion = " to Stack "+ alphabet_list[indx2]
                # new child from Node()
                child = Node()
                child.parent = initial
                child.cost = pay
                child.state = copy_init2
                child.action = act + ion
                '''Calculate the heuristc value:'''
                if heu == 0 :
                    q1.insert(child)
                elif heu == 1 :
                    dest_block = goal[Final_disks_position]
                    # Num of disks in its required position
                    dest_block_len = len(dest_block)
                    # Num of disks need to move to its required position
                    dest_block_len = disks_num - dest_block_len
                    child.heuristic = 2**dest_block_len-1
                    child.cost += child.heuristic
                    q2.insert(child)
                if heu == 2:
                    dest_block = goal[Final_disks_position]
                    # Num of disks in its required position
                    dest_block_len = len(dest_block)
                    # Num of disks need to move to its required position
                    dest_block_len = disks_num - dest_block_len
                    empty_wide = [True for i in wide_stacks if len(copy_init2[i]) == 0]
                    if any(empty_wide):
                        # probability of moving a disk to an empty wide stack
                        probability = len(empty_wide) / (stacks_num-1)
                    else:
                        # probability of moving a disk to/from a non-empty wide stack
                        probability = 0
                        for el in wide_stacks:
                            for inx,ii in enumerate(copy_init2):
                                if inx== el or packet < copy_init2[el][0]:
                                    probability = probability + (1/(stacks_num-1))
                    child.heuristic = probability
                    # add the heuristic value to the cost
                    child.cost += child.heuristic
                    q3.insert(child)
                # else:



def collect_info():
    global wide_stacks, alphabet_list, current, goal, disks_num, Final_disks_position, stacks_num
    stacks_num = int(input("The number of stacks (3 to 6): "))
    disks_num = int(input("The number of disks (3 to 10): "))

    alphabet_list = list(string.ascii_uppercase[:stacks_num])
    wide_stacks = input("Which are the wide stacks? "+str(alphabet_list)+": ")
    wide_stacks = wide_stacks.split(",")

    current_state = input("Which is the current state? "+str(alphabet_list)+": ")
    current_state = current_state.upper()

    goal_state = input("Which is the goal state? "+str(alphabet_list)+": ")
    goal_state = goal_state.upper()

    ''' Manipulate Information'''
    all_disks = [num for num in range(1, disks_num + 1)]
    # Map alphabet input to list of lists "Current"
    Initial_disks_position = alphabet_list.index(current_state)
    # Map alphabet input to list of lists "goal"
    Final_disks_position = alphabet_list.index(goal_state)
    # Current and goal states as list of lists
    current = [all_disks if inx == Initial_disks_position  else [] for inx,_ in enumerate(range(stacks_num))]
    goal = [all_disks if inx == Final_disks_position  else [] for inx,_ in enumerate(range(stacks_num))]
    # Map the wide_stacks in its alphabet form to its numeric form
    wide_stacks = [i for i,_ in enumerate(alphabet_list) if _ in wide_stacks]


''' Run the UCS Algorithm:'''
# Require the user to enter the info:
collect_info()
# Create the node (obj) that holds the initial state
n1 = Node()
n1.state = current
# Create a queue obj to handle the objects based on the cost
q1 =PriorityQueue()
# insert the current state to the queue
q1.insert(n1)
# Expand the current state
Largest_list = []
give_next(n1,0)
# return the obj with the least cost
least = q1.delete()
while least.state != goal:
    least = q1.delete()
    give_next(least,0)

# trace back to reach the root
par = copy.deepcopy(least)
list_of_actions = []
while par != None:
    # save the parent of the current node in par
    list_of_actions.insert(0, par.action)
    par = par.parent

file_handler = open("movements.txt","w+")
file_handler.write("Follow these steps to reach the goal:")
for stmt in list_of_actions:
    file_handler.write(stmt+"\n")
file_handler.close()
print("--"*20)
print("Uniform Cost Search Algorithm:")
print("The number of expanded nodes is:",len(Largest_list))
print("--"*20)
''' Run the A* Algorithm (1st heurstic):'''
# Create the node (obj) that holds the initial state
n2 = Node()
n2.state = current
# Create a queue obj to handle the objects based on the cost
q2 =PriorityQueue()
# insert the current state to the queue
q2.insert(n2)
# Expand the current state
Largest_list = []
give_next(n2,1)
# return the obj with the least cost
least = q2.delete()
while least.state != goal:
    least = q2.delete()
    give_next(least,1)

# trace back to reach the root
par = copy.deepcopy(least)
list_of_actions = []
while par != None:
    # save the parent of the current node in par
    list_of_actions.insert(0, par.action)
    par = par.parent

print("A* Algorithm (1st heurstic):")
print("Depending on the number of disks "+"\n"+"that not in the goal stack as a heurstic value")
print("The number of expanded nodes is:", len(Largest_list))
print("--"*20)

''' Run the A* Algorithm (2nd heurstic):'''
# Create the node (obj) that holds the initial state
n3 = Node()
n3.state = current
# Create a queue obj to handle the objects based on the cost
q3 =PriorityQueue()
# insert the current state to the queue
q3.insert(n3)
# Expand the current state
Largest_list = []
give_next(n3,2)
# return the obj with the least cost
least = q3.delete()
while least.state != goal:
    least = q3.delete()
    give_next(least,2)

# trace back to reach the root
par = copy.deepcopy(least)
list_of_actions = []
while par != None:
    # save the parent of the current node in par
    list_of_actions.insert(0, par.action)
    par = par.parent

print("A* Algorithm (2nd heurstic):")
print("Depending on the possibility of moving"+"\n"+"a disk from/to a wide stack as a heurstic value")
print("The number of expanded nodes is:", len(Largest_list))
print("--"*20)

