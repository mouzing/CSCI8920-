from testGame import testGame
from FSM import *
import random
import copy
import sys

lower_num_games = 25
upper_num_games = 25
# number of rounds for each game for scoring for upcoming generation
num_rounds = random.randint(lower_num_games, upper_num_games) 

# for x in range(18):
# 	print(fsm.node_list[x].transition_dict)

def make_child(fsm):
	child_fsm = copy.deepcopy(fsm)
	if id(child_fsm) == id(fsm):
		print("fsm are same")
		sys.exit()
	if id(child_fsm.node_list) == id(fsm.node_list):
		print("node_list are same")
		sys.exit()

	child_fsm.fitness_score = 0
	chance_to_mutate = .25
	for node in child_fsm.node_list:	
		chance = random.uniform(0, 1)
		if chance <= chance_to_mutate:
			chance = random.uniform(0, 1)
			if chance < 0.5:
				change_node_action(node)
			else:
				change_transition_destination(node)

	evaluate(child_fsm)
	return child_fsm

#mutation functions
# the same transition value but points to a different active state
def change_node_action(node):
	choice = random.choice(testGame.action_list)
	while choice == node.action:
		choice = random.choice(testGame.action_list)
	node.action = choice

# this is too aggressive -> cut balls off later
def change_transition_destination(node):
	max_change = len(testGame.action_list) # maximum number of allowed changes
	for i in range(max_change):
		chance = random.uniform(0, 1)
		if chance <= (1/(i+1)):
			transition_action = random.choice(testGame.action_list) # random so as to not "favor" lower indexes
			# change the value for the above key in node's dictionary
			node.transition_dict[transition_action] = random.randint(1, FSM.number_of_nodes) - 1
		else: 
			break # breaks if "chance" doesn't make the cutoff -> favors low numbers of changes


def evaluate(fsm): 
	total_payoff = 0
	for i in range(testGame.player_count): # might change testGame to be classless -> just a file with methods
		testGame.opponent_last_action = testGame.default_action
		fsm.reset()
		for j in range(num_rounds):
			# get player actions
			player1_action = fsm.get_action()
			player2_action = testGame.get_action(i)
			player_actions = player1_action + player2_action
			total_payoff += testGame.payoff[player_actions][0]
			# update information before next round
			fsm.update_state(player2_action)
			testGame.opponent_last_action = player1_action
	
	fsm.fitness_score = total_payoff


population = [] # list of all current individuals
population_size = 50
for x in range(population_size):
	population.append(FSM(testGame.action_list))	

for member in population:
	evaluate(member)

population.sort(key=lambda x: x.fitness_score, reverse=True)
sum_total = 0
for member in population:
	sum_total += member.fitness_score

sum_total = sum_total / population_size

starting = population[0].fitness_score

iterations = 0
best_score = population[0].fitness_score
rounds_since = 0
while True:
	if population[0].fitness_score > best_score:
		best_score = population[0].fitness_score
		rounds_since = 0
	else:
		rounds_since += 1

	if rounds_since >= 50:
		break

	# redfine num rounds for upcoming generation
	next_generation = []
	for member in population:
		next_generation.append(make_child(member))
	population.extend(next_generation)
	population.sort(key=lambda x: x.fitness_score, reverse=True)
	population = population[0:population_size]
	if iterations > 5000:
		break
	iterations += 1

	

for i, x in enumerate(population):
	print(f"{i}: {x.fitness_score}")


print(sum_total)
print(starting)
print(population[0].fitness_score)
print(population[0].fitness_score - starting)
print(iterations)


# fsm = FSM(game)
# print(fsm.node_list[0].transition_dict)
# print()
# change_transition_destination(fsm.node_list[0])
# print(fsm.node_list[0].transition_dict)