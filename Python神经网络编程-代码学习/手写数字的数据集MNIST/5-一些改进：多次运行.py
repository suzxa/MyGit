# 经过多次训练，可以提供更多爬下斜坡的机会，有助于在梯度下降过程进行权重更新
# 训练一次成为一个世代，以五个世代为宜

# 总共训练两次
epochs = 2

for e in range(epochs):
	for record in training_data_list:
		all_values = record.split(",")
		inputs = numpy.asfarray(all_values[1:]) / 255 * 0.99 + 0.01
		targets = numpy.zeros(output_nodes) + 0.01
		targets[int(all_values[0])] = 0.99
		n.train(inputs, targets)
		pass