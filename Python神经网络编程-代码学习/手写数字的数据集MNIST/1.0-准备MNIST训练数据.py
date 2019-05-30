'''
		为了避免输入值过大，我们需要先将颜色值从较大的0到255缩小至0.01到1.0
		选择0.01是为了避免先前观察到的0值输入最终会人为地造成权重更新失败，没有选择0.99作为上限值
	是因为不需要避免输入1.0会造成这个问题，我们只需要避免输出值为1.0。
'''

data_file = open("mnist_train_100.csv", "r")
data_list = data_file.readlines()
data_file.close()
import numpy
import matplotlib.pyplot
all_values = data_list[0].split(",")


# 我们需要先将原始输入除以255，得到0到1的输入值；然后乘以0.99，把范围变成0.0到0.99；最后加上0.01
# 得到最终所需范围0.01到1.00
scaled_input = numpy.asfarray(all_values[1:]) / 255 * 0.99 + 0.01
print(scaled_input)

# 对于输出来说，无法生成0到1的值，于是我们认为规定范围0.01到0.99
# 因为标签有0到9十个数字，所以我们需要十个输出层节点
# 初始化目标矩阵和输出层节点数目
onodes = 10
# zeros()函数用来生成一个所有数值为0长度为onodes的数组，然后加0.01让数组中的数值等于0.01
targets = numpy.zeros(onodes) + 0.01
# 让以训练数值为索引的数值，在数组中取最高上限0.99
targets[int(all_values[0])] = 0.99