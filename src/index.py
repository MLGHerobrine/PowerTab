#!/usr/bin/env python3

# Imports
import tkinter as tk
from tkinter import ttk
import json
import random
# Definitions

def sort_teams(teams):
	output = {} # Dictionary of teams, sorted by wins. Ex: output['1'] = ['Speaker1-Speaker2', 'Speaker1-Speaker2', 'Speaker1-Speaker2']
	for k, v in teams.items():
		if not v['wins'] in output:
			output[v['wins']] = [k]
		else: # Better to replace with a else if and throw error if elif doesn't work
			output[v['wins']].append(k)
	return output

def pair_teams(teams):
	keys = teams.keys()
	pairs = []
	for k in keys:
		for t in teams[k]:
			# Get and remove two teams
			teams[k].remove(0)
			t2 = teams[k].pop()

			# Append the two chosen teams to pairs
			pairs.append((t, t2))
class App(ttk.Frame):
	def _init__(self, master=None):
		super().__init__(master)
		self.pack()

		# Create widgets with TTK

# Main
def main():
	teams = json.load(open('test_round1.json'))
	round1 = sort_teams(teams)
	print(round1)

if __name__ == '__main__': main()