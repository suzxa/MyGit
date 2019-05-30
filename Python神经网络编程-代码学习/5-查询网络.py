# 矩阵乘法:输入层与隐藏层之间的链接权重，乘以输入层节点输入值
# 求出输入隐藏层节点的信号
hidden_inputs = numpy.dot(self.wih, inputs)

# S函数在scipy库中，名字为expit()
import scipy.special

# 为方便使用，定义希望使用的激活函数
# lambda函数这里是创建了一个函数，这个函数接受了x，返回scipy.special.expit(x)。但是这个函数没有名字
# 这里分配给它一个名字self.activation_function()。
self.activation_function = lambda x: scipy.special.expit(x)

# 求出隐藏层节点的输出信号
hidden_outputs = self.activation_function(hidden_inputs)

# 与上面的情形相似，可以求出输出层的输入信号和输出信号
final_inputs = numpy.dot(self.who, hidden_outputs)
final_outputs = self.activation_function(final_inputs)