class Tensor(object):
	def __init__(self, ndims, shape, elements):
		self.ndims = ndims
		self.shape = shape
		self.elements = elements

	def ndims(self):
		return self.ndims

	def shape(self):
		return self.shape

	def elements(self):
		return self.elements

	# indexing
	def __getitem__(self, key):
		return self.elements[key]

	def __setitem__(self, key, value):
		self.elements[key] = value

	# elementwise operations
	def __add__(self, other):
		if isinstance(other, Tensor):
			result = Tensor(self.ndims, self.shape, [])
			for i in range(len(self.elements)):
				result.elements.append(self.elements[i] + other.elements[i])
			return result
		else:
			raise Exception("{} must be a tensor".format(other))


## blas operations
def matmul(left, right):
	pass

## lapack operations
def det(tensor):
	pass
