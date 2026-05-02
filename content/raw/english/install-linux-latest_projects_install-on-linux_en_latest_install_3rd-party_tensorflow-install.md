---
title: "TensorFlow on ROCm installation"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/tensorflow-install.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:14:18.517738+00:00
content_hash: "f1ede01b5fe3a0cc"
---

# TensorFlow on ROCm installation[#](#tensorflow-on-rocm-installation)

2026-04-16

6 min read time

[TensorFlow](https://tensorflow.org) is an open-source library for solving machine learning,
deep learning, and AI problems.

This topic covers setup instructions and the necessary files to build, test, and run
TensorFlow with ROCm support in a Docker environment. To learn more about TensorFlow
on ROCm, including its use cases, recommendations, as well as hardware and software compatibility,
see [TensorFlow compatibility](https://rocm.docs.amd.com/en/latest/compatibility/ml-compatibility/tensorflow-compatibility.html).

Note

As of ROCm 6.1.0, `tensorflow-rocm`

packages are found at [https://repo.radeon.com/rocm/manylinux](https://repo.radeon.com/rocm/manylinux).
Prior to ROCm 6.1.0, packages were found at [https://pypi.org/project/tensorflow-rocm](https://pypi.org/project/tensorflow-rocm).

ROCm version |
TensorFlow version |
|---|---|
7.2.x |
2.20.0, 2.19.1, 2.18.1 |
7.1.x |
2.20.0, 2.19.1, 2.18.1 |
7.0.x |
2.19.1, 2.18.1, 2.17.1 |
6.4.x |
2.18.1, 2.17.1, 2.16.2 |
6.3.x |
2.17.0, 2.16.2 2.15.1 |

## Install TensorFlow[#](#install-tensorflow)

To install TensorFlow for ROCm, you have the following options:

### Use a prebuilt Docker image with TensorFlow pre-installed[#](#use-a-prebuilt-docker-image-with-tensorflow-pre-installed)

The recommended setup to get a TensorFlow environment is through Docker, as it avoids potential installation issues.
The tested, prebuilt image includes TensorFlow, ROCm, and other dependencies. See [Docker image support](#tensorflow-docker-support).
To install ROCm on bare metal, follow [ROCm installation overview](../install-overview.html).

Download the latest public

[TensorFlow Docker image](https://hub.docker.com/r/rocm/tensorflow).pull rocm/tensorflow:latest

Once you have pulled the image, run it by using the command below:

run -it \ --network=host \ --device=/dev/kfd \ --device=/dev/dri \ --ipc=host \ --shm-size 16G \ --group-add video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/tensorflow:latest \ /bin/bash


### Docker image support[#](#docker-image-support)

AMD validates and publishes ready-made TensorFlow images with ROCm backends on Docker Hub. The following Docker image tags and associated inventories are validated for ROCm 7.2.2.

### Use a wheels package[#](#use-a-wheels-package)

To install TensorFlow using the wheels package, use the following command.

```
install --user tensorflow-rocm==[wheel-version] -f [repo] --upgrade
```

`[wheel-version]`

is the[TensorFlow version](#install-tensorflow-versions).`[repo]`

is`https://repo.radeon.com/rocm/manylinux/rocm-rel-X.Y/`

for versions 6.1 and later, where`X.Y`

indicates the[ROCm version](#install-tensorflow-versions).

Note

Prior to ROCm 6.1, `[wheel-version]`

followed the `<TensorFlowVersion>.<ROCmVersion>`

format.

## Test the TensorFlow installation[#](#test-the-tensorflow-installation)

To test the installation of TensorFlow, run the container as specified in
[Installing TensorFlow](#install-tensorflow-options). Ensure you have access to the Python
shell in the Docker container.

```
-c 'import tensorflow' 2> /dev/null && echo ‘Success’ || echo ‘Failure’
```

## Run a TensorFlow example[#](#run-a-tensorflow-example)

To quickly validate your TensorFlow environment, run a basic TensorFlow example.

The MNIST dataset is a collection of handwritten digits that may be used to train a Convolutional Neural Network (CNN) for handwriting recognition. This dataset is included with your TensorFlow installation.

Run the following sample code to load the MNIST dataset, then train and evaluate it.

```
import tensorflow as tf
print("TensorFlow version:", tf.__version__)
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
model = tf.keras.models.Sequential([
tf.keras.layers.Flatten(input_shape=(28, 28)),
tf.keras.layers.Dense(128, activation='relu'),
tf.keras.layers.Dropout(0.2),
tf.keras.layers.Dense(10)
])
predictions = model(x_train[:1]).numpy()
tf.nn.softmax(predictions).numpy()
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1], predictions).numpy()
model.compile(optimizer='adam',
loss=loss_fn,
metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test, verbose=2)
```

If successful, you should see the following output indicating the image classifier is now trained to around 98% accuracy on this dataset.
