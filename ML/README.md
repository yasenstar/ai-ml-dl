# Machine Learning

## Supervised vs Reinforcement vs Unsupervised

Thanks for source: https://www.geeksforgeeks.org/supervised-vs-reinforcement-vs-unsupervised/

![s-r-u](img/supervised-reinforcement-unsupervised.png)

| Item | Supervised Learning | Reinforcement Learning | Unsupervised Learning |
| :-- | :-- | :-- | :-- |
| Deinition | Supervised learning is akin to learning with a teacher. In this paradigm, the algorithm is trained on a labeled dataset, which means that each training example is paired with an output label. The goal is for the model to learn a mapping from inputs to outputs so that it can predict the output for new, unseen inputs. | The Reinforcement learning (RL) is an interactive type of machine learning where an agent learns to make decisions by the interacting with its environment. The agent takes actions and receives rewards or penalties based on its performance with the aim of maximizing the cumulative rewards over time. | The Unsupervised learning deals with the data that has no labeled outcomes. The model is tasked with the identifying patterns, structures or relationships within the dataset. Since there are no labels, the model doesn’t receive direct feedback or guidance on what the correct output should be. |
| Key Characteristics | - **Labeled Data**: Supervised learning requires a dataset where the input data is labeled with the correct output. This allows the model to learn by comparing its predictions with the actual outcomes and adjusting accordingly.<br>- **Types of Problems**: It is primarily used for classification and regression problems. Classification involves predicting discrete labels (e.g., spam or not spam), while regression involves predicting continuous values (e.g., house prices).<br>- **Algorithms**: Common algorithms include linear regression, logistic regression, support vector machines (SVM), decision trees, and neural networks. | - **Interaction with Environment**: The agent learns by taking actions in an environment to maximize cumulative reward overtime.<br>- **No Labeled Data Required**: Unlike supervised learning, RL does not require labeled input/output pairs but learns from feedback received from its actions.<br>- **Algorithms**: Includes Q-learning, SARSA (State-Action-Reward-State-Action), and Deep Q Networks (DQN). | - **Unlabeled Data**: The model works with data that has no predefined labels. It tries to find hidden structures or groupings in the data.<br>- **Types of Problems**: Commonly used for clustering and associaton tasks. Clustering involves grouping similar data points together, while association involves discovering interesting relations between variables.<br>- **Algorithms**: Popular algorithms include K-means clustering, hierarchical clustering, principal component analysis (PCA), and autoencoders. |
| Types | - **Classification**: The model predicts a categorical label. e.g. detecting if an email is spam or not.<br>- **Regression**: The model predicts continuous output. e.g. predicting house prices on historical data. | | |



## Python机器学习(第三版)

![Python-ML-III](img/Python-ML-III-book-cover.png)

## 机器学习基础