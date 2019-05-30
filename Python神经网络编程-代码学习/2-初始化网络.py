'''
		从此时开始，我们需要设置各层节点的数量——定义了神经网络的形状和尺寸，我们不会固定这些数量，
	保留选择的余地。
'''

class neuralNetwork:

	# 初始化神经网络
	def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
		# 初始化输入层、隐藏层、输出层的数量
		self.inodes = inputnodes
		self.hnodes = hiddennodes
		self.onodes = outputnodes
		# 初始化学习率
		self.lr = learningrate
		pass

	def train():
		pass

	def query():
		pass

# 设置输入层、隐藏层、输出层的数量
input_nodes = 3
hidden_nodes = 3
output_nodes = 3

# 设置学习率的值
learning_rate = 0.5

# 创建一个神经网络的实例
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)