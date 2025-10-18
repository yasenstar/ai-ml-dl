 Essential GraphRAG

# 1. Improving LLM Accuracy

Integrating knowledge graphs into RAG pipelines can overcome LLM limitations, enhance data retrieval, and facilitate a holistic approach to managing and using diverse data types across domains like healthcare, finance, and technical support.


## 1.1 Introduction to LLMs
 
LLMs are built ontransformer  architecture (Vaswani et al., 2017), which enables them to process and generate text efficiently.


### The model doesn't store specific facts, events, or information from its training dataset. Instead, it develops complex mathematical representations of the language it is trained on.

### While LLMs can provide seemingly knowledgeable answers, their responses are based on those learned weights rather than explicit memory.

### To quote Andrej Karpathy: "We kind of understand that they (LLMs) build and maintain some kind of knowledge database, but even this knowledge base is very strange and imperfect and weird"

## 1.2 Limitations of LLMs

### 1.2.1 KNowledge Cutoff Problem

#### The most obvious limitations is that LLMs are unaware of events or information not included in their training dataset.
 
In the context of LLMs, theknowledge cutoff date  refers to the most recent point at which the model's training data includes information.


### 1.2.2 Outdated Information

#### A less obvious limitation is that LLMs can sometimes provide outdated responses.

#### This highlights the importance of regularly updating training data for models or enabling them to access real-time information.

#### This limitation underlines the importance of ensuring I systems remain accurate and relevant in dynamic environments.

### 1.2.3 Pure Hallucinations (幻觉)

#### The well-known limitation of LLMs is their tendency to provide assertive, confident answers - even when those answers contains incorrect or fabricated information.

#### Hallucinations occur because LLMs are not reasoning engines. They are probabilistic language models trained to predict what sounds like a good next token, based on patterns in their training data.
 
The LLMs don't knowfacts  the way humans do.


#### The LLMs generate text by guessing the most likely continuation, regardless of whether it's true.

#### This fundamental difference between statistical pattern matching and actual understanding is what separates LLMs from human cognition.

### 1.2.4 Lack of Private Information

### More limitations of LLMs

#### Bias in Responses

##### LLMs can sometimes generate biased responses, reflecting biases present in the training data

#### Lack of Understanding and Context

##### LLMs, despite their complexity, do not truly understand the text.

##### They process language based on patterns learned from data, which means they can miss nuances and contextual subtleties. (它们根据从数据中学习到的模式来处理语言，这意味着它们可能会忽略细微差别和上下文的微妙之处。)

#### Vulnerability to Prompt Injection

##### LLMs are susceptible to prompt injection attacks, where malicious users craft inputs to manipulate the model into generating inappropriate, biased, or harmful responses.

#### Inconsistent Responses

##### LLMs can produce different answers to the same question across multiple interactions.

## 1.3 Overcoming the Limitations of LLMs

### 1.3.1 Supervised Finetuning

#### Steps of training of an LLM like ChatGPT

##### 1. Pretraining

##### 2. Supervised Finetuning

##### 3. Reward Modeling

##### 4. Reinforcement Learning

### 1.3.2 Retrieval-Augmented Generation

## 1.4 Knowledge Graphs as the Data Storage for RAG Applications

# 2. Vector Similarity Search and Hybrid Search

# 3. Advanced Vector Retrieval Strategies

# 4. Generating Cypher Queries from Natural Language Questions

# 5. Agentic RAG

# 6. Constructing Knowledge Graphs with LLMs

# 7. Microsoft's GraphRAG Implementations

# 8. RAG Application Evaluation
