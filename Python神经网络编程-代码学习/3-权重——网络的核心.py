'''
		创建网络的节点和链接。网络中最重要的部分是链接权重，我们使用这些权重来计算前馈信号、反向传播误
	差，并且在试图改进网络时优化链接权重本身。
		使用矩阵可以方便地表示权重：输入层与隐藏层之间的链接权重矩阵W(input_hidden)，大小为
	hidden_nodes乘以input_nodes；隐藏层和输出层之间的链接权重矩阵W(hidden_output)，大小为output_nodes
	乘以hidden_nodes。
'''

# 要使用numpy的扩展包，需要在代码顶端导入库
# 若没有，使用pip install numpy指令在命令提示符窗口直接输入下载
import numpy

# 初始化权重初始值，用numpy函数生成一个数组，数组中元素为0~1的随机值，大小为rows乘以columns
# numpy.random.rand(rows, columns)
# 但是权重可以为正也可以为负，范围可以在-1.0到+1.0之间，为了简单起见，可以全部数值减去0.5
# numpu.random.rand(rows, columns) - 0.5
# 综上，可以初始化输入层与隐藏层之间的链接权重矩阵wih，和隐藏层与输出层之间的链接权重矩阵who
self.wih = numpy.random.rand(self.hnodes, self.inodes) - 0.5
self.who = numpy.random.rand(self.onodes, self.hnodes) - 0.5