#!/usr/bin/python
'''
Base class for Scanner Program
Created on Aug 15, 2014

@author: Hrishikesh Kumar
'''
import abc
class Base():
	__metaclass__ = abc.ABCMeta
	def __init__(self):
		print "You probably want to extend the Base class"

	@abc.abstractmethod
	def prepare(self, package_name = None, apk_path = None):
		"""
		prepare
		"""
		
	@abc.abstractmethod
	def run(self, report_dict):
		"""
		run
		"""
