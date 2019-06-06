#------------------------------------------------------------------------------
# autodiff: c_generator.py
#
# C code generator from autodiff nodes.
#
#------------------------------------------------------------------------------


class CGenerator(object):
	"""Writes a file with C code, hardcoded function definitions,
		uses string accumulation for returning expressions.
	"""

	def __init__(self, filename = 'c_code', variable_count = 1, ispc = True, c_code = False):
		self.indent_level = 0
		self.filename=filename
		self.variable_count = 2 # number of variables
		self.count = 0
		self.ispc = ispc
		self.c_code = c_code
		f = open(self.filename+'.c','w')
		f.close()

	def _make_indent(self):
		return ' ' * self.indent_level

	def _make_header(self):

		if self.c_code:
			ext = '.c'

			f = open(self.filename+ext,'w')
			f.write("void compute(double values[], int num_points, double ders[]){\n\n")
			f.write("\tfor(int i = 0; i < num_points; ++i)\n\t{\n") # iterate over 
			f.close()


		if(self.ispc):
			ext = '.ispc'
			f = open('derivatives.ispc','w')
			f.write("export void compute(uniform double values[], uniform int num_points, uniform double ders[]){\n\n")
			f.write("\tforeach (i = 0 ... num_points)\n\t{\n") # iterate over 
			# f.write("\tfor (int i = 0; i < num_points; ++i){\n")
			f.close()

	def _generate_expr(self, var, derivative_string):

		if self.c_code:

			ext = '.c'		
			f = open(self.filename+ext,'a')
			f.write("\t\tders[i]"+"= "+derivative_string+";\n")
			f.close()		
		

		if(self.ispc):

			ext = '.ispc'	
			f = open('derivatives.ispc','a')
			f.write("\t\tders[i]"+" = "+derivative_string+";\n")
			f.close()	
		self.count += 1	

	def _declare_vars(self, var, index):

		if self.c_code:

			ext = '.c'			
			f = open(self.filename+ext,'a')
			f.write("\t\tdouble %s = values[i];\n" % (var))
			f.close()

		if(self.ispc):

			ext = '.ispc'				
			f = open('derivatives.ispc','a')
			f.write("\t\tdouble %s = values[i];\n" % (var))
			# f.write("\t\tprint(\"k = %\\n\",k);");
			f.close()			

	def _make_footer(self):

		if self.c_code:

			ext = '.c'			
			f = open(self.filename+ext,'a')
			f.write("\t}\n}\n\n")
			f.close()	

		if (self.ispc):

			ext = '.ispc'				
			f = open('derivatives.ispc','a')
			f.write("\t}\n}\n\n")	
			f.close()		


	def _write(self,derivative_string):
		self._make_header()
		self._generate_expr(derivative_string)
		self._make_footer()


