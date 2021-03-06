# Author : Henri Toussaint
# Latest revision : 01/17/2017

# Class that identifies the metaphor candidates in the annotated text
from .datastructs.candidate_group import CandidateGroup

class CandidateIdentifier:

	def __init__(self, annotatedText):
		self.annotatedText = annotatedText
		self.candidates = None

	def IDCandidates(self, identificationFunction):
		self.candidates = identificationFunction(self.annotatedText)

	def getCandidates(self):
		return self.candidates