#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys, os

class Master(object):
	
	def __init__(self, name):
		self.name = name
		self.tier = 99 # 0 => leader, 99 = inactif
		self.tierNodeList = 99*[None] # Adresse réseaux des autres tiers
		self.rulesDataset = {} # Régle synchronisée par les tiers
		
	def Promote(self):
		if self.tier == 0:
			return False
		else:
			self.tier -= 1
		
		self.tierNodeList
		

	@property
	def NextTier(self): # Noeud de niveau inferieur (ou None si on est le dernier)
		pass
		
	@property
	def PreviousTier(self): # Noeud de niveau superieur (ou None si on est le leader)
		pass
