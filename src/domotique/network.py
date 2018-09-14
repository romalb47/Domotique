#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys, os, network, json

class NetworkDevice(object):
	def __init__(self, name, address):
		self.name = name
		self.address = address
		self.socket = None

	def send(self, data):
		temp = json.dumps(data)
		#TODO Envoyées les données

