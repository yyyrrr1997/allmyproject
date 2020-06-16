
import numpy as np
import tensorflow as tf
import random


Train_labels = np.loadtxt("train_labels_h.txt")
Train_data = np.loadtxt("Train.txt")
Train_data = np.reshape(Train_data,(330,1,100,3))# 将数据处理成 1*100的矩阵；训练集：330张 1*100*3的图片

Train_labels = np.reshape(Train_labels,(330,4)) #标签：330个标签，4 种类型

#将图片进行打乱
index = [i for i in range(330)]
random.shuffle(index)
Train_data = Train_data[index]
Train_labels = Train_labels[index]


Test_labels = np.loadtxt("test_labels_h.txt")
Test_data = np.loadtxt("Test.txt")
Test_data = np.reshape(Test_data,(60,1,100,3)) #测试集：60张1*100*3的图片

Test_labels = np.reshape(Test_labels,(60,4)) #标签：60个标签，4种类型

input_height = 1 #“图片”高度为1
input_width = 100 #“图片”宽度为100
num_labels = 4 #标签有4 种
num_channels = 3 #xyz轴三个通道相当于RGB三通道

batch_size = 20 #每批送入的图片数量
kernel_size = 1*10*6 #卷积核大小 1*10，有6个

learning_rate = 0.0001 #学习率
training_epochs = 1000 #偏历数据集的次数

def CNN(input_tensor, train, regularizer):
    with tf.variable_scope('layer1-conv1'):
        #第一层——卷积层
        #设置卷积核 60组权值(对一张输入进行60种卷积，输出60张特征图) initializer 初始化方式
        conv1_weights = tf.get_variable("weight",[1,10,3,60],initializer=tf.truncated_normal_initializer(stddev=0.1))
        conv1_biases = tf.get_variable("bias",[60],initializer=tf.constant_initializer(0.0)) #偏置值
        #卷积叠加求和计算
        #第一个参数，输入数据
        # 第二个参数，卷积核大小和数量设置
        #第三个参数，卷积核步长 只能设置[1,1,1,1]中间两个值，分别表示水平滑动和垂直滑动的步长，输出1*90的特征图
        # 第四个参数 padding='SAME'卷积数据不够丢弃
        conv1 = tf.nn.conv2d(input_tensor, conv1_weights, strides=[1,1,1,1],padding='VALID')
        #通过激活函数——采用relu函数 输出
        # 卷积计算结果和偏置值通过激活函数
        relu1 = tf.nn.relu(tf.nn.bias_add(conv1, conv1_biases))
    with tf.name_scope('layer2-pool1'):
        # 第二层——池化层
        #采用最大池化法
        #第一个参数，上一层输出的feature map
        # 第二个参数，选择器大小为1*2
        #第二个参数，采样器步长为2
        # 第四个参数 采样数据不够丢弃
        pool1 = tf.nn.avg_pool(relu1, ksize=[1,1,2,1],strides=[1,1,2,1],padding="VALID")
        print(pool1.get_shape().as_list())#1*45*10
    with tf.variable_scope('layer3-conv2'):
        # 第三层——卷积层
        #设置卷积核大小，大小1*5，深度60
        conv2_weights = tf.get_variable("weight",[1,10,60,10],initializer=tf.truncated_normal_initializer(stddev=0.1))
        conv2_biases = tf.get_variable("bias",[10],initializer=tf.constant_initializer(0.0))
        #卷积运算输出
        conv2 = tf.nn.conv2d(pool1, conv2_weights, strides=[1,1,1,1],padding='VALID')
        #运算结果和偏置通过激活函数输出
        relu2 = tf.nn.relu(tf.nn.bias_add(conv2, conv2_biases))

    # 将第四层池化层的输出转化为第五层全连接层的输入格式。
    pool_shape = relu2.get_shape().as_list()  # 获取上一层输出的feature map的数据形状，列表形式
    print(pool_shape)  # 1*36*10种
    nodes = pool_shape[1] * pool_shape[2] * pool_shape[3]  # 所有数据排列开来后的数量
    print(nodes)#360
    reshaped = tf.reshape(relu2, [-1, nodes])
    with tf.variable_scope('layer4-fc1'):
        #第五层——全连接层
        fc1_weights = tf.get_variable("weight",[nodes,100],initializer=tf.truncated_normal_initializer(stddev=0.1))#权值设置，nodes表示一组多少个权值
        if regularizer != None:
            tf.add_to_collection('loss', regularizer(fc1_weights)) #给损失函数加入正则化
        fc1_biases = tf.get_variable("bias", [100], initializer=tf.constant_initializer(0.1))
        fc1 = tf.nn.tanh(tf.matmul(reshaped, fc1_weights) + fc1_biases) #将数据、权值计算后加上偏置值，通过tanh函数输出结果
        if train:# 是否防止过拟合
            fc1 = tf.nn.dropout(fc1, 0.5)
    with tf.variable_scope('layer5-fc2'):
        # 第五层——全连接层
        fc2_weights = tf.get_variable("weight", [100,4],initializer=tf.truncated_normal_initializer(stddev=0.1))# 4 组权值,4 种结果；
        if regularizer != None:
            tf.add_to_collection('loss', regularizer(fc2_weights))
        fc2_biases = tf.get_variable("bias", [4], initializer=tf.constant_initializer(0.1))
        logits = tf.nn.softmax(tf.matmul(fc1, fc2_weights) + fc2_biases) #实际输出
    return logits
#设置输入CNN网络中的数据类型，数据形状（1*100*3）
X = tf.placeholder(tf.float32, shape=[None,input_height,input_width,num_channels])
#期望输出
Y = tf.placeholder(tf.float32, shape=[None,num_labels])

regularizer = tf.contrib.layers.l2_regularizer(0.001)#正则化
y_ = CNN(X, False, regularizer) #获取CNN网络的输出结果。
loss = -tf.reduce_sum(Y*tf.log(y_)) #损失函数
#loss = tf.nn.sigmoid_cross_entropy_with_logits(labels=Y,logits=y_)

optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)
correct_prediction = tf.equal(tf.argmax(y_, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as session:
    tf.initialize_all_variables().run()

    for epoch in range(training_epochs):
        _, tra_ = session.run([optimizer, accuracy], feed_dict={X: Train_data, Y: Train_labels})
        testa = session.run(accuracy, feed_dict={X: Test_data, Y: Test_labels})
        print("Epoch: ", epoch, " Training Accuracy: ",session.run(accuracy, feed_dict={X: Train_data, Y: Train_labels}))
       # print("Testing Accuracy:", session.run(accuracy, feed_dict={X: Test_data, Y: Test_labels}))
