from FSM import *
from testGame import testGame
from BotS import BattleOfTheSexes
from TravDem import TravelersDilemma

lower_num_games = 25
upper_num_games = 25
# number of rounds for each game for scoring for upcoming generation
num_rounds = random.randint(lower_num_games, upper_num_games) 
noise = False

#game = testGame()
#game = BattleOfTheSexes()
game = TravelersDilemma()

class t4t_fsm():
	def __init__(self):
		self.internal_node_list = []
		self.create_nodes()
		self.create_transitions()
		self.fsm = FSM(game.action_list, node_list=self.internal_node_list)

	def create_nodes(self):
		for action in game.action_list:
			node = Node(game.action_list, action=action, transition_dict="placeholder")
			self.internal_node_list.append(node)

	def create_transitions(self):
		temp_dict = {}
		for i, action in enumerate(game.action_list):
			temp_dict[action] = i
		for node in self.internal_node_list:
			node.transition_dict = temp_dict

			
def evaluate(fsm): 
	total_payoff = 0
	for i in range(game.player_count): 
		game.opponent_last_action = game.default_action
		fsm.reset()
		if game.game_name == "Travelers Dilemma": # hard code for testing purposes
			print("IN HERE")
			fsm.current_state = 4
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


test = t4t_fsm()
evaluate(test.fsm)
print(test.fsm.payoff_list)
print(test.fsm.fitness_score)

