'''
		有些人喜欢稍微复杂的方法来创建出随机权重。
		他们使用正态概率分布来采样权重，其中平均值为0，标准方差为节点传入链接数目的开方，即：
	1/((传入链接数目)^(1/2))
 '''
'''
		我们将正态分布中心设定为0.0。与下一层中节点相关的标准方差的表达式是中间的式子，表示节点数目的
	-0.5次方。最后一个参数，就是我们的numpy数组的形状大小！
'''
# 初始化权重的更新代码如下：
self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
self.who = numpy.random.normal(0.0, pow(self.onodse, -0.5), (self.onodes, self.hnodes))
