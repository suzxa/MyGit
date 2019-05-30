# 训练神经网络
def train(self, inputs_list, targets_list):
	# 将输入列表和目标列表转置
	inputs = numpy.array(inputs_list, ndmin=2).T
	targets = numpy.array(targets_list, ndmin=2).T

	# 隐藏层的输入输出信号
	hidden_inputs = numpy.dot(self.wih, inputs)
	hidden_outputs = self.activation_function(hidden_inputs)

	# 输出层的输入输出信号
	final_inputs = numpy.dot(self.who, hidden_outputs)
	final_outputs = self.activation_function(final_inputs)

	# 计算误差
	# 隐藏层与输出层之间用output_errors优化，输入层与隐藏层之间用hidden_errors优化
	output_errors = targets - final_outputs
	hidden_errors = numpy.dot(self.who.T, output_errors)

	# 隐藏层与输出层：学习率*输出层输出信号的误差*输出层输出(1-输出层输出)*隐藏层输出信号的转置
	self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), \
				numpy.transpose(hidden_outputs))
	# 输入层与隐藏层：学习率*隐藏层输出信号的误差*隐藏层输出(1-隐藏层输出)*输入层输出信号的转置
	self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), \
				numpy.transpose(inputs))
	pass