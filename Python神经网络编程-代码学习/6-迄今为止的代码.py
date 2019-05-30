import numpy
import scipy.special

class neuralNetwork:

	# 初始化神经网络
	def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
		# 初始化输入层、隐藏层、输出层的数量
		self.inodes = inputnodes
		self.hnodes = hiddennodes
		self.onodes = outputnodes
		# 初始化学习率
		self.lr = learningrate

		# 初始化权重的更新代码如下：
		self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
		self.who = numpy.random.normal(0.0, pow(self.onodse, -0.5), (self.onodes, self.hnodes))

		# 为方便使用，定义希望使用的激活函数
		self.activation_function = lambda x: scipy.special.expit(x)
		pass

	def train():
		pass

	def query(self, inputs_list):
		# 将inputs_list数组变为维数最小为2的数组，然后将其转置！
		# 因为我们一般输入的列表都是单位行向量，求取隐藏层节点输入信号时，要将其转置为单位列向量！
		inputs = numpy.array(inputs_list, ndmin=2).T

		# 求出输入隐藏层节点的信号
		hidden_inputs = numpy.dot(self.wih, inputs)

		# 求出隐藏层节点的输出信号
		hidden_outputs = self.activation_function(hidden_inputs)

		# 与上面的情形相似，可以求出输出层的输入信号和输出信号
		final_inputs = numpy.dot(self.who, hidden_outputs)
		final_outputs = self.activation_function(final_inputs)
		pass
