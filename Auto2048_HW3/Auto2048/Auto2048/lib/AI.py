from lib.Grid import * 
import asyncio
import random
import multiprocessing
import time
from os import cpu_count
class AI:
	def __init__(self, multi_core=False):
		self.multi_core = multi_core
		self.init_dict()
	def multi_process_sim_game(self, game_state, proc_n_games, n_games, pilId = -1, pil_fmName = "", pil_scName = ""):
		cpuNum = cpu_count()
		divide_n_games = int(n_games/cpuNum)
		pilFm = shared_memory.ShareableList(name = pil_fmName)
		pilSc = shared_memory.ShareableList(name = pil_scName)
		for i in range(proc_n_games):
			result = self.sim_game(copy.deepcopy(game_state))
			pilFm[divide_n_games*pilid + i] = int(result[0])
			pilSc[divide_n_games*pilid + i] = result[1]
		pilFm.shm.close()
		pilFm.shm.unlink()
		pilSc.shm.close()
		pilSc.shm.unlink()
	def sim_game(self, game_state):
		temp_game = Grid(template = game_state)
		first_move = random.choice(list(Moves))
		temp_game.move(first_move)
		while True:
			if not temp_game.move(random.choice(list(Moves))): break
		return (first_move, temp_game.score())
	def next_move(self, game_state, n_games):
		start = time.time()
		results = []
		for i in range(n_games):
			results.append(self.sim_game(copy.deepcopy(game_state)))
		end = time.time()
		print("sim_ngame: " + str(end - start))
		for result in results:
			self.move_results[result[0]].append(result[1])
		choices = []
		for i in Moves:
			if len(self.move_results[i]) == 0: continue
			choices.append((i, sum(self.move_results[i]) / len(self.move_results[i])))
		choices.sort(key=lambda x: x[1], reverse=True)
		self.init_dict()
		print(choices[0][0].name)
		return choices[0][0]

	def init_dict(self):
		self.move_results = {}
		for i in Moves:
			self.move_results[i] = []