# 第一章 引言

- [第一章 引言](#第一章-引言)
  - [1.1 为何选择机器学习](#11-为何选择机器学习)
    - [1.1.1 机器学习能够解决的问题](#111-机器学习能够解决的问题)
    - [1.1.2 熟悉任务和数据](#112-熟悉任务和数据)
  - [1.2 为何选择Python](#12-为何选择python)
  - [1.3 scikit-learn](#13-scikit-learn)
  - [1.4 必要的库和工具](#14-必要的库和工具)
    - [1.4.1 Jupyter Notebook](#141-jupyter-notebook)
    - [1.4.2 NumPy](#142-numpy)
    - [1.4.3 SciPy](#143-scipy)
    - [1.4.4 matplotlib](#144-matplotlib)
    - [1.4.5 pandas](#145-pandas)
    - [1.4.6 mglearn](#146-mglearn)
  - [1.5 Python 2与Python 3的对比](#15-python-2与python-3的对比)
  - [1.6 本书用到的版本](#16-本书用到的版本)
  - [1.7 第一个应用：鸢尾花(Iris)分类](#17-第一个应用鸢尾花iris分类)

机器学习(machine learning)是从数据中提取知识，是统计学、人工智能和计算机科学交叉的研究领域，也被成为预测分析(predictive analytics)或统计学习(statistical learning)。

## 1.1 为何选择机器学习

人为制订决策规则的两个主要缺点：
1. 做决策所需要的逻辑只适用于单一领域和单项任务
2. 想要制订规则，需要对人类专家的决策过程有很深刻的理解

### 1.1.1 机器学习能够解决的问题

从输入/输出对中进行学习的机器学习算法叫作**监督学习算法(supervised learning algorithm)**。

监督机器学习任务的示例：
- 识别信封上手写的邮政编码
- 基于医学影像判断肿瘤是否为良性
- 监测信用卡交易中的诈骗行为

**无监督学习算法(unsupervised learning algorithm)**，只有输入数据是已知的，没有为算法提供输出数据。

无监督学习示例：
- 确定一系列博客文章的主题
- 将客户分成具有相似偏好的群组
- 检测网站的异常访问模式

在机器学习中，每个实体或数据表格中的每一行被称为一个**样本(sample)**或数据点，每一列（用来描述这些实体的属性）被称为**特征(feature)**。

构建良好的数据表征被称为**特征提取(feature extraction)**或**特征过程(feature engineering)**。

### 1.1.2 熟悉任务和数据

在机器学习过程中，最重要的部分很可能是**理解你正在处理的数据，以及这些数据与你想要解决的任务之间的关系**。

下面是在构建机器学习解决方案过程中应该回答的问题：
- 我想要回答的问题是什么？
- 以及收集到的数据能够回答这个问题么？
- 要将我的问题表示成机器学习问题，用哪种方法最好？
- 我收集的数据是否足够表达我想要解决的问题？
- 我提取了数据的哪些特征？
- 这些特征能否实现正确的预测？
- 如何衡量应用是否成功？
- 机器学习解决方案与我的研究或商业产品中的其他部分是如何相互影响的？

## 1.2 为何选择Python

Python现在是许多科学应用的通用语言。

机器学习和数据分析本质上都是迭代过程，由数据驱动分析。这些过程必须要有快速迭代和易于交互的工具。

## 1.3 scikit-learn

```
# install scikit-learn
> pip install numpy scipy matplotlib ipython scikit-learn pandas mglearn
```

## 1.4 必要的库和工具

scikit-learn是基于NumPy和SciPy科学计算库的，还会用到pandas和matplotlib。

### 1.4.1 Jupyter Notebook

Create `*.ipynb` file in VS Code.

### 1.4.2 NumPy

[numpy.ipynb](numpy.ipynb) 显示了ndarray类的创建与输出。

### 1.4.3 SciPy

scikit-learn利用SciPy中的函数集合来实现算法。

SciPy中最重要的是`scipy.sparse`：它可以给出**稀疏矩阵(sparse matrice)**，稀疏矩阵是scikit-learn中数据的另一种表示方法。

这个例子用稀疏矩阵来保存一个大部分元素都是0的二维数组：[scipy1.ipynb](scipy1.ipynb)

若直接创建稀疏表示(sparse representation)，使用COO格式：[scipy2.ipynb](scipy2.ipynb)

### 1.4.4 matplotlib

matplotlib是Python主要的科学绘图库。

在Jupyter Notebook中，可以使用`%matplotlib notebook`（可以提供交互环境）和`%matplotlib inline`命令，将图像直接显示在浏览器中。见示例代码：[matplotlib.ipynb](matplotlib.ipynb)

### 1.4.5 pandas

pandas是用于处理和分析数据的Python库，基于DataFrame数据结构，模仿了R语言中的DataFrame。这个代码使用字典数据结构创建DataFrame：[pandas.ipynb](pandas.ipynb)

### 1.4.6 mglearn

默认需要导入如下的库：

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
```

如果不使用Jupyter Notebook，就需要调用`plt.show`来显示图像。

## 1.5 Python 2与Python 3的对比

本教程使用Python 3。

## 1.6 本书用到的版本

点击[lib-version.ipynb](lib-version.ipynb)查看各个库的版本。

## 1.7 第一个应用：鸢尾花(Iris)分类

典型的监督学习中的分类(classification)问题。具体为三分类问题 - setosa, versicolor, virginica。

单个数据点（一朵鸢尾花）的预期输出是这朵花的品种，对于一个数据点来说，其品种叫作标签(label)。

问题分析可以从这个文件中参考：[iris.ipynb](iris.ipynb)

---

Last updtaed at 2026-02-21