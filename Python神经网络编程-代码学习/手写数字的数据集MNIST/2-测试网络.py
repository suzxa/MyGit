import numpy
import matplotlib.pyplot

# 首先要获取测试记录
test_data_file = open("mnist_test_10.csv", "r")
test_data_list = test_data_file.readlines()
test_data_file.close()

all_values = test_data_list[0].split(",")
print(all_values[0])

image_array = numpy.asfarray(all_values[1: ]).reshape((28, 28))
matplotlib.pyplot.imshow(image_array, cmap="Greys", interpolation="None")

matplotlib.pyplot.show()

# 综上写出测试神经网络的代码
# 初始化计分卡，匹配成功添加1，不成功添加0
scorecard = []
for record in test_data_list:
	all_values = record.split(",")
	# 将正确结果放到correct_label中保存起来
	correct_label = int(all_values[0])
	print(correct_label, "corret label")
	inputs = numpy.asfarray(all_values[1:]) / 255 * 0.99 + 0.01
	# 查询网络
	# 具有最大值的输出节点就是网络认为的答案
	outputs = n.query(inputs)
	# 将最大值的数组下标(索引)赋值给label
	label = numpy.argmax(outputs)
	print(label, "network's answer")
	# 如果网络的结果与正确值一致，添加1到scorecard中。否则添加0
	if(label == correct_label):
		scorecard.append(1)
	else:
		scorecard.append(0)

# 输出计分卡可以清楚看到有多少个数值是匹配的
print(scorecard)

# 取计分卡中的平均数，计算准确率
scorecard_array = numpy.asarray(scorecard)
print("performance = ", scorecard_array.sum() / scorecard_array.size)