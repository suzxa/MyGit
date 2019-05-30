'''
		可以从受人尊敬的神经网络研究员Yann LeCun的网站http://yann.lecun.com/exdb/mnist/得到MNIST数据集
		但是，MNIST数据库的格式不容易使用，因此有人创建了相对简单的数据文件格式，参见
	http://pjreddie.com/projects/mnist-in-csv
'''

# 用python语言打开文件并获取其中的内容
# 这里注意数据集文件对于代码文件的路径，r告诉我们以只读方式打开，无法写入和修改
data_file = open("mnist_train_100.csv", "r")
# 使用readlines()函数将文件中的所有行读入变量data_list，它包含了一个列表，一项就是一行字符串
data_list = data_file.readlines()
# 关闭文件，释放内存
data_file.close()

print(len(data_list))
print(data_list[0])

import numpy
import matplotlib.pyplot
# %matplotlib inline	# 在IPython中，坚持在Notebook上绘制图形，不在独立的外部窗口绘制，需要添加这句

# all_values接收的data_list[0]，并根据逗号将这一长串进行了拆分
all_values = data_list[0].split(",")
# asfarray()函数将文本字符串转换成实数，并创建这些数字的数组；reshape()函数可以确保数字里列表每28个
# 元素折返一次，形成28乘以28的放行矩阵
image_array = numpy.asfarray(all_values[1: ]).reshape((28, 28))
# 用imshow()函数绘制image_array。cmap用来选择调色板，代码中调用灰度(Greys)调色板。
matplotlib.pyplot.imshow(image_array, cmap="Greys", interpolation="None")

# 这一句至关重要，书本上并没有说明，但是不添加这句，图形无法显示！
matplotlib.pyplot.show()