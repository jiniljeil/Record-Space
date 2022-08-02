## TensorFlow 
> TensorFlow is an open source software library for numerical computation using <strong>data flow graphs</strong>.

#### What is data flow graphs? 
> - Nodes in the graph represent mathematical operations.
> - Edges represent the multidimensional data arrays(tensors) communicated between them. 

#### Installing TensorFlow
```sh 
pip install --upgrade tensorflow
pip install --upgrade tensorflow-gpu
```

#### Check installation and version 
```python 
>>> import tensorflow as tf
>>> tf.__version__
```

##### TensorFlow Hello World!

```python 
hello = tf.constant("Hello, TensorFlow!")
sess = tf.Session()
print(sess.run(hello))

>>> b'Hello, TensorFlow!
```

##### Computational Graph 

```python 
node1 = tf.constant(3.0)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2) 

print("node1:",node1, "node2:",node2 )
print("node3:",node3) 

sess = tf.Session()
print("sess.run(node1, node2):", sess.run(node1,node2)) 
print("sess.run(node3):", sess.run(node3))
```