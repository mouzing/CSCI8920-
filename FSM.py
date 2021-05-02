import random

#number_of_nodes_global = 18 # initial number of total nodes (not all have to be active)

class FSM:
	#number_of_nodes = number_of_nodes_global
	number_of_nodes = 18 # this value was found from a related paper
	def __init__(self, game_action_list, node_list=None):
		self.node_list = []
		if node_list == None:
			self.generateNodes(game_action_list)
		else:
			self.node_list = node_list
		self.fitness_score = 0
		self.current_state = 0 # index in the nodelist that represents the current state


	def generateNodes(self, game_action_list):
		for x in range(FSM.number_of_nodes):
			self.node_list.append(Node(game_action_list))

	def get_action(self):
		return self.node_list[self.current_state].action

	def update_state(self, opponent_action):
		self.current_state = self.node_list[self.current_state].transition_dict[opponent_action]

	def reset(self):
		self.current_state = 0

class Node:
	def __init__(self, game_action_list, action=None, transition_dict=None):
		#action = generateAction() -> removed with function "generateAction" becasue below line seems better
		if action == None:
			self.action = random.choice(game_action_list)
		else:
			self.action = action
		if transition_dict == None:
			self.transition_dict = self.generateIntialDict(game_action_list) # intial value for transitions is random
		else:
			self.transition_dict = transition_dict
		# (random.choice(game_name.action_list), random.randint(0, number_of_nodes) -> code that may be useful another time

	def generateIntialDict(self, game_action_list):
		transition_dict = {}
		for action in game_action_list:
			transition_dict[action] = random.randint(1, FSM.number_of_nodes) - 1
		return transition_dict


	# def generateAction(game_name):
	# 	return random.choice(game_name.action_list)
