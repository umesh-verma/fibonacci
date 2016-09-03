'''prints fibonacci series upto 20 values
this module provides a Class print Fib.
'''
class Fib() :
	'''
	documentation for class Fib
	methods ::
		print fibonacci
		print hello world
	'''
	def print_srs(self,n):
		'''documentation for method print_srs
		prints the fibbonacci series upto 20 terms'''
		a=0
		y=1
		print a
		print y
		for i in range(1,n):
			s=a+y
			a=y
			y=s
			print s
		
	def hello(self):
		''' this method prints hello world
		'''
		print "hello world"
		