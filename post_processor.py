import os
import post_process

class PostProcessor:
	def __init__(self, output):
		self.output = output
		print 'output'
		print output
		self.scripts = []
		try:
			self.gather_scripts()
		except Exception as e:
			print 'gathering post process scripts'
			print e
	def gather_scripts(self):
		for name in post_process.__all__:
			script = getattr(post_process, name)
			try:
				# see if the script has a 'register' attribute
				register_plugin = script.register
			except AttributeError:
				# raise an exception, log a message, 
				# or just ignore the problem
				print 'no register'
				pass
			else:
				# try to call it, without catching any errors
				register_plugin()
			self.scripts.append(script)
	# def gather_scripts(self):
	# 	current_directory = os.path.dirname(os.path.realpath(__file__))
	# 	plugin_directory = os.path.join(current_directory, 'post_process')
	def run_scripts(self):
		print 'run scripts'
		for script in self.scripts:
			script.process(self.output)
