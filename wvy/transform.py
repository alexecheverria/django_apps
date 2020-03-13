from sympy import Function,Symbol, simplify
class Transform:
	transform_name = ''
	var_char = 'z'
	equation = ''
	numerator = {} #First Element is s
	denominator = {}
	operators = [' ', '+', '-', '/', '*', '^', '!','(',')']
   
	s

	def getTransform_Name(self):
		return self.transform_name

	def setTransform_Name(self, new_name):
		self.transform_name = new_name

	def getVarChar(self):
		return self.var_char

	def setVarChar(self, new_var_char):
		self.var_char = new_var_char

	def getEquation(self):
		return self.equation
	
	def setEquation(self, new_num, new_den):
		new_num = ''
		#TODO Modify to take in different equations then 
		'''
		Symbol(self.getVarChar())
		new_num_eq = Function('1+2')
		new_num_eq = simplify(new_num)
		new_den_eq = Function(new_den)
		new_den_eq = simplify(new_den)

		self.equation = Function(new_num_eq/new_den_eq)
		print(self.equation)
		'''
	def getCoefficients(self):
	 	return [self.numerator, self.denominator]

	def setCoefficients(self, new_numerator, new_denominator):
	 	self.numerator = new_numerator
	 	self.denominator = new_denominator
	 	new_de = '('
	 	for power in new_numerator:
	 		new_de += '+'
	 		if(power == 0):
	 			new_de += str(new_numerator[power])+' '
	 		else:
	 			new_de += str(new_numerator[power])+'z'+'^'+ str(power) + ' '
	 	new_de += ')/('
	 	for power in new_denominator:
	 		new_de += '+'
	 		if(power == 0):
	 			new_de += str(new_denominator[power])+' '
	 		else:
	 			new_de += str(new_denominator[power])+'z'+'^'+ str(power) + ' '
	 	new_de += ')'
	 	self.equation = new_de
	 	print(self.equation)

