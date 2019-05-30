import numpy
import scipy.special
import matplotlib.pyplot	# 引入绘制图形的python库

class neuralNetwork:

	def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
		self.inodes = inputnodes
		self.hnodes = hiddennodes
		self.onodes = outputnodes
		
		self.lr = learningrate
		
		self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
		self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

		self.activation_function = lambda x: scipy.special.expit(x)
		pass

	def train(self, inputs_list, targets_list):
		inputs = numpy.array(inputs_list, ndmin=2).T
		targets = numpy.array(targets_list, ndmin=2).T
	
		hidden_inputs = numpy.dot(self.wih, inputs)
		hidden_outputs = self.activation_function(hidden_inputs)

		final_inputs = numpy.dot(self.who, hidden_outputs)
		final_outputs = self.activation_function(final_inputs)

		output_errors = targets - final_outputs
		hidden_errors = numpy.dot(self.who.T, output_errors)

		self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), \
					numpy.transpose(hidden_outputs))
		self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), \
					numpy.transpose(inputs))
		pass

	def query(self, inputs_list):
		inputs = numpy.array(inputs_list, ndmin=2).T

		hidden_inputs = numpy.dot(self.wih, inputs)
		hidden_outputs = self.activation_function(hidden_inputs)

		final_inputs = numpy.dot(self.who, hidden_outputs)
		final_outputs = self.activation_function(final_inputs)
		
		return final_outputs

# 输入层节点、隐藏层节点和输出层节点的数量
# 输入层节点数量是因为训练数据集共有784个数值，这是28乘以28的结果
# 隐藏层节点数量没有最佳方法选择，不能太大也不能太小，最好的办法是进行实验确定
input_nodes = 784
hidden_nodes = 100
output_nodes = 10

# 学习率设为0.3
learning_rate = 0.3

# 创建一个神经网络实例
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

# 将MNIST训练数据集载入列表中
training_data_file = open("mnist_train_100.csv", "r")
training_data_list = training_data_file.readlines()
training_data_file.close()

# 逐一将训练数据集中的记录进行训练
for record in training_data_list:
	all_values = record.split(",")
	inputs = numpy.asfarray(all_values[1:]) / 255 * 0.99 + 0.01
	targets = numpy.zeros(output_nodes) + 0.01
	targets[int(all_values[0])] = 0.99
	n.train(inputs, targets)
	pass