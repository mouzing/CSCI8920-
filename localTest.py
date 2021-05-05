from testGame import testGame
from FSM import *
from BotS import BattleOfTheSexes
from TravDem import TravelersDilemma
import random
import copy

lower_num_games = 25
upper_num_games = 25
# number of rounds for each game for scoring for upcoming generation
num_rounds = random.randint(lower_num_games, upper_num_games) 
noise = False


#game = testGame()
#game = BattleOfTheSexes()
game = TravelersDilemma()


def make_child(fsm):
	child_fsm = copy.deepcopy(fsm)

	child_fsm.fitness_score = 0
	child_fsm.payoff_list.clear()
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
	choice = random.choice(game.action_list)
	while choice == node.action:
		choice = random.choice(game.action_list)
	node.action = choice

# this is too aggressive -> cut balls off later
def change_transition_destination(node):
	max_change = len(game.action_list) # maximum number of allowed changes
	for i in range(max_change):
		chance = random.uniform(0, 1)
		if chance <= (1/(i+1)):
			transition_action = random.choice(game.action_list) # random so as to not "favor" lower indexes
			# change the value for the above key in node's dictionary
			node.transition_dict[transition_action] = random.randint(1, FSM.number_of_nodes) - 1
		else: 
			break # breaks if "chance" doesn't make the cutoff -> favors low numbers of changes

# def noise(action):
# 	noise_chance = 0.05
# 	if random.uniform(0, 1) < noise_chance:
# 		if 


def evaluate(fsm): 
	total_payoff = 0
	for i in range(game.player_count): 
		game.opponent_last_action = game.default_action
		fsm.reset()
		current_payoff = 0
		for j in range(num_rounds):
			# get player actions
			p1_action = fsm.get_action()
			p2_action = game.get_action(i)
			#player_actions = p1_action + p2_action
			current_payoff += game.get_payoff(p1_action, p2_action)
			# update information before next round
			fsm.update_state(p2_action)
			game.opponent_last_action = p1_action
		fsm.payoff_list.append(current_payoff)
		total_payoff += current_payoff
	
	fsm.fitness_score = total_payoff


population = [] # list of all current individuals
population_size = 50
for x in range(population_size):
	population.append(FSM(game.action_list))	

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

	# if rounds_since >= 50:
	# 	break

	# redfine num rounds for upcoming generation
	next_generation = []
	for member in population:
		next_generation.append(make_child(member))
	population.extend(next_generation)
	population.sort(key=lambda x: x.fitness_score, reverse=True)
	population = population[0:population_size]
	if iterations > 500:
		break
	iterations += 1


print(sum_total)
print(starting)
print(population[0].fitness_score)
print(population[0].fitness_score - starting)
print(rounds_since)
print()
print(population[0].payoff_list)
print(len(population[0].payoff_list))
print()
for i, node in enumerate(population[0].node_list):
	for j in game.action_list:
		print(f"{i} -> {node.transition_dict[j]} [label = \"{node.action}/{j}\"];")


print(population[0].payoff_list)
print(population[0].fitness_score)




# print()
# fsm = population[0]
# fsm.reset()
# current_payoff = 0
# for i in range(num_rounds):
# 	player1_action = fsm.get_action()
# 	player2_action = game.get_action(2)
# 	player_actions = player1_action + player2_action
# 	current_payoff += game.payoff[player_actions][0]
# 	print(f"{i}: {player_actions}")
# 	print(f"{i}: {game.payoff[player_actions][0]}")
# 	print()
# 	# update information before next round
# 	fsm.update_state(player2_action)
# 	game.opponent_last_action = player1_action


# print(current_payoff)
