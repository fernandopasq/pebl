"""Classes and functions for learning with sparse data"""

from pebl import prior, config, evaluator, result, network
from pebl.learner.base import Learner
from pebl.taskcontroller.base import Task

class SparseLearner(Learner):
	"""docstring for SparseLearner"""
	_params = (
		config.StringParameter(
			'sparselearner.experiments',
			"""List with variables covered by each experiment""", 
			default=''
		)
	)
	
	def __init__(self, data_=None, prior_=None, experiments=None):
		"""Create a SparseLearner learner
		
		experiments should be a list of experiments, consisting of a tuple of (which variables are covered, experiment size)
		
		"""
		super(SparseLearner, self).__init__(data_,prior_)
		self.experiments = experiments
		
	def run(self):
		self.result = result.LearnerResult(self)
		self.evaluator = evaluator.fromconfig(self.data, prior_=self.prior)
		self.result.start_run()
		
		# algorithm here!
		print 'Yay! Nothing to see here...'
		# get prior!
		# complete datasets!
		# self.evaluator.score_network()

		self.result.stop_run()
		return self.result
