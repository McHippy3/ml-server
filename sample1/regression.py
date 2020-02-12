import numpy as np
import tensorflow.compat.v1 as tf
import matplotlib.pyplot as plt
from datetime import datetime
tf.disable_v2_behavior()

def generate_dataset(dataset, y_label):
    x_batch = np.linspace(0,dataset.count()-1, dataset.count())
    y_batch = []
    for item in dataset:
        y_batch.append(getattr(item, y_label))
    return x_batch, y_batch

def create_variables():
    x = tf.placeholder(tf.float32, shape=(None, ), name='x')
    y = tf.placeholder(tf.float32, shape=(None, ), name='y')

    with tf.variable_scope('lreg') as scope:
        w = tf.Variable(np.random.normal(), name='W')
        b = tf.Variable(np.random.normal(), name='b')

        y_pred = tf.add(tf.multiply(w, x), b)

        loss = tf.reduce_mean(tf.square(y_pred - y))

    return x, y, w, b, y_pred, loss

def run_regression(dataset, y_label):
  x_batch, y_batch = generate_dataset(dataset, y_label)
  x, y, w, b, y_pred, loss = create_variables()

  optimizer = tf.train.GradientDescentOptimizer(0.001)
  train_op = optimizer.minimize(loss)

  with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    feed_dict = {x: x_batch, y: y_batch}
	
    for i in range(10000):
      session.run(train_op, feed_dict)
      print(i, "loss:", loss.eval(feed_dict))

    print('Finished')
    print('w: {}, b: {}'.format(session.run(w), session.run(b)))
    results = {"w": float(session.run(w)), "b": float(session.run(b)), "loss": float(loss.eval(feed_dict))}
    y_pred_batch = session.run(y_pred, {x : x_batch})

  #Saving Graph
  plt.scatter(x_batch, y_batch)
  plt.plot(x_batch, y_pred_batch, color='red')
  plt.xlim(0, 30)
  plt.ylim(0, 20000)
  plt.savefig("templates/results/{}.png".format(datetime.now().strftime("%H_%M_%S")))
  plt.clf()

  return results