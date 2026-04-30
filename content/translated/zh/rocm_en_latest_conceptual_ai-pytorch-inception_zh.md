---
title: "Deep learning: Inception V3 with PyTorch"
source_url: "https://rocm.docs.amd.com/en/latest/conceptual/ai-pytorch-inception.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-04-28
---

::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}

::: header-article-item
- [](../index.html){.nav-link aria-label="首页"}
- 深度学习...

header-article-items__end
header-article-item
article-header-buttons

# 深度学习：使用 PyTorch 的 Inception V3

## 目录



- [深度学习训练](#deep-learning-training){.reference .internal .nav-link}
- [训练阶段](#training-phases){.reference .internal .nav-link}
- [案例研究](#case-studies){.reference .internal .nav-link}
  - [Inception V3 与 PyTorch](#inception-v3-with-pytorch){.reference .internal .nav-link}
    - [评估预训练模型](#evaluating-a-pre-trained-model){.reference .internal .nav-link}
    - [训练 Inception V3](#training-inception-v3){.reference .internal .nav-link}
  - [使用 CIFAR-10 的自定义模型（基于 PyTorch）](#custom-model-with-cifar-10-on-pytorch){.reference .internal .nav-link}
  - [案例：TensorFlow 与 Fashion-MNIST](#case-study-tensorflow-with-ashion-mnist){.reference .internal .nav-link}
  - [案例：TensorFlow 与文本分类](#case-study-ensorflow-with-text-classification){.reference .internal .nav-link}

# 深度学习：Inception V3 与 PyTorch[\#](#deep-learning-inception-v3-with-pytorch "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026年1月23日



```html
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-try-time-svg} 31 分钟阅读时间
```

适用于 Linux 和 Windows

## 深度学习训练[\#](#deep-learning-training "Link to this heading"){.headerlink}

深度学习模型旨在捕捉问题的复杂性及其底层数据。这些模型是"深度"的，由多个组件层组成。训练是为每个模型层找到最佳参数以实现明确定义的目标。



训练数据由监督学习中的输入特征组成，类似于学习到的模型在评估或推理阶段预期看到的数据。训练数据中还包含目标输出，用于指导模型学习。作为训练的一部分，会定义损失指标来评估模型在训练过程中的表现。

训练还包括选择优化算法的过程，该算法通过调整模型参数来减少损失值。训练是一个迭代过程，训练数据通常被分成不同的批次输入，在一个训练轮次中遍历全部训练数据。训练通常会运行多个轮次。

## 训练阶段[\#](#training-phases "Link to this heading"){.headerlink}

训练对每个训练数据批次分多个阶段进行。下表对训练阶段类型进行了说明。

::: pst-scrollable-table-container
  阶段类型
  ------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  前向传播        输入特征被送入模型，模型的参数最初可能是随机初始化的。在该阶段中，每一层的激活值（输出）会被保留，以便在反向传播时用于损失梯度计算。
  损失计算    将输出与目标输出进行比较，并计算出损失值。
  反向传播       损失反向传播，计算并存储每个可训练参数的误差梯度。
  优化迭代   优化算法使用存储的误差梯度来更新模型参数。

训练不同于推理，尤其从硬件角度来看更是如此。下表展示了训练与推理之间的差异。

::: pst-scrollable-table-container
  训练                                                                                                                                                                                   推理
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  训练以小时/天为单位进行计量。                                                                                                                                                        推理以分钟为单位进行计量。
  训练通常在数据中心或云环境中离线运行。                                                                                                                                              推理在边缘设备上执行。
  训练的内存需求高于推理，因为需要存储中间数据，例如激活值和误差梯度。                                                                                                                  推理的内存需求低于训练。
  训练数据在训练过程之前就存在于磁盘上，通常数量较大。训练性能取决于数据批次的处理速度。                                   推理数据通常随机到达，可以进行批处理以提高性能。推理性能通常以处理数据批次的吞吐量速度和对输入的响应延迟（延迟时间）来衡量。

不同的量化数据类型通常在训练（FP32、BF16）和推理（FP16、INT8）之间进行选择。计算硬件对不同的数据类型有不同的专门优化，如果能够为相应任务选择更快的数据类型，则可以提升性能。

## 案例研究[\#](#案例研究 "链接到此标题"){.headerlink}

以下各节包含 Inception V3 模型的案例研究。

### Inception V3 使用 PyTorch[\#](#inception-v3-with-pytorch "Link to this heading"){.headerlink}

卷积神经网络（CNN）是人工神经网络的一种形式，常用于图像处理。该网络的核心层之一是卷积层，它用权重张量对输入进行卷积运算，并将结果传递到下一层。Inception V3 是对 ImageNet 竞赛冠军模型 AlexNet 的架构改进，采用更深更广的网络，同时努力满足计算和内存预算。

该实现使用 PyTorch 作为框架。本案例研究使用 [TorchVision](https://pytorch.org/vision/stable/index.html){.reference .external}（一个包含流行数据集和模型架构的仓库）来获取模型。TorchVision 还提供预训练权重作为起点，用于开发新模型或为新任务微调模型。



#### 评估预训练模型[\#](#evaluating-a-pre-tained-model "Link to this heading"){.headerlink}

Inception V3 模型展示了使用预训练模型的简单图像分类任务。这不涉及训练，而是利用来自 TorchVision 的已预训练模型。



本示例改编自 PyTorch 研究资源页面中关于 [Inception V3](https://pytorch.org/vision/master/models/inception.html){.reference .external} 的内容。

按照以下步骤：

1. 运行基于 PyTorch ROCm（Radeon Open Compute 平台）的 Docker 镜像，或参阅[安装 PyTorch](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html)部分来在 ROCm（Radeon Open Compute 平台）上设置 PyTorch 环境。

docker run -it -v $HOME:/data --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host --shm-size 8G rocm/pytorch:latest



2. 运行 Python shell 并导入用于模型创建的包和库。

::: highlight
        import torch
        import torchvision



3. 将模型设置为评估模式。评估模式指示 PyTorch 不存储中间数据，这些数据在训练中本应会被使用。

::: highlight
        model = torch.hub.load('pytorch/vision:v0.10.0', 'inception_v3', pretrained=True)
        model.eval()

4. 下载示例图像用于推理。

::: highlight
        import urllib
        url, filename = ("https://github.com/pytorch/hub/raw/master/images/dog.jpg", "dog.jpg")
        try: urllib.URLopener().retrieve(url, filename)
        except: urllib.request.urlretrieve(url, filename)



5. 导入 torchvision 和 PILImage 支持库。

::: highlight
        from PIL import Image
        from torchvision import transforms
        input_image = Image.open(filename)



6. 应用预处理和归一化。

::: highlight
        preprocess = transforms.Compose([
            transforms.Resize(299),
            transforms.CenterCrop(299),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

使用输入张量，并在稍后进行维度扩展。

```cuda
        input_tensor = preprocess(input_image)
        input_batch = input_tensor.unsqueeze(0)
        if torch.cuda.is_available():
            input_batch = input_batch.to('cuda')
            model.to('cuda')
```

8. 找出概率。

::: highlight
        with torch.no_grad():
            output = model(input_batch)
        print(output[0])
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        print(probabilities)



9. 要理解这些概率，请下载并查看 ImageNet 标签。

::: highlight
        wget https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt

10. 读取类别并显示图像的主要类别。

::: highlight
        with open("imagenet_classes.txt", "r") as f:
            categories = [s.strip() for s in f.readlines()]
        top5_prob, top5_catid = torch.topk(probabilities, 5)
        for i in range(top5_prob.size(0)):
            print(categories[top5_catid[i]], top5_prob[i].item())

#### 训练 Inception V3[\#](#training-inception-v3 "链接到此标题"){.headerlink}



上一节重点介绍了如何下载和使用 Inception V3 模型进行简单的图像分类任务。本节将逐步讲解如何使用新数据集训练该模型。

按以下步骤操作：

1. 请运行 PyTorch ROCm Docker 镜像，或参照 [Installing PyTorch](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html "(in ROCm installation on Linux v7.2.2)") 部分，了解如何在 ROCm 上配置 PyTorch 环境。



```docker
docker pull rocm/pytorch:latest
docker run -it --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host --shm-size 8G rocm/pytorch:latese
```

2.  下载 ImageNet 数据库。在本示例中，[`tiny-imagenet-200`{.docutils .literal .notranslate}]{.pre}（一个较小的 ImageNet 变体，包含 200 个图像类别以及包含 100,000 张图像的训练数据集）被调整为 64x64 彩色图像。



::: highlight
        wget http://cs231n.stanford.edu/tiny-imagenet-200.zip



3. 处理数据库以将验证目录设置为 PyTorch 的 [`DataLoader`{.docutils .literal .notranslate}] 所需的格式。

4.  运行以下脚本：



```python
import io
import glob
import os
from shutil import move
from os.path import join
from os import listdir, rmdir
target_folder = './tiny-imagenet-200/val/'
val_dict = {}
with open('./tiny-imagenet-200/val/val_annotations.txt', 'r') as f:
    for line in f.readlines():
        split_line = line.split('\t')
        val_dict[split_line[0]] = split_line[1]
```

```python
paths = glob.glob('./tiny-imagenet-200/val/images/*')
        for path in paths:
            file = path.split('/')[-1]
            folder = val_dict[file]
            if not os.path.exists(target_folder + str(folder)):
                os.mkdir(target_folder + str(folder))
                os.mkdir(target_folder + str(folder) + '/images')
```



```python
for path in paths:
            file = path.split('/')[-1]
            folder = val_dict[file]
            dest = target_folder + str(folder) + '/images/' + str(file)
            move(path, dest)
```

rmdir('./tiny-imagenet-200/val/images')

5. 打开一个 Python shell。

6. 导入依赖项，包括 Torch、OS 和 [TorchVision](https://github.com/pytorch/vision){.reference .external}。



::: highlight
        import torch
        import os
        import torchvision
        from torchvision import transforms
        from torchvision.transforms.functional import InterpolationMode



7. 设置参数以指导训练过程。

注意

设备被设置为 [`"cuda"`{.docutils .literal .notranslate}]{.pre}。在 PyTorch 中，[`"cuda"`{.docutils .literal .notranslate}]{.pre} 是一个用于表示 GPU 的通用关键字。

device = "cuda"

8. 设置 data_path 指向训练和验证数据的位置。在这种情况下，[`tiny-imagenet-200`{.docutils .literal .notranslate}]{.pre} 作为当前目录的子目录存在。

```highlight
        data_path = "tiny-imagenet-200"
```

训练图像尺寸会被裁剪后输入到 Inception V3。



train_crop_size = 299



9. 为了平滑图像使用双线性插值，这是一种重采样方法，通过对四个最近像素值进行距离加权平均来估算新的像素值。

::: highlight
        interpolation = "bilinear" :::

接下来的参数用于控制验证图像的裁剪和调整大小尺寸。

::: highlight
        val_crop_size = 299
        val_resize_size = 342

选择从 torchvision 下载预训练的 Inception V3 模型。

::: highlight
        model_name = "inception_v3"
        pretrained = True

在每个训练步骤中，会处理一批图像来计算损失梯度并执行优化。在以下设置中，确定批次大小。

```highlight
        batch_size = 32
```



这指的是数据加载器用于执行高效多进程数据加载的 CPU 线程数量。

num_workers = 16

[`torch.optim`{.docutils .literal .notranslate}]{.pre} 包提供了在训练过程中调整学习率的方法。本示例使用了 [`StepLR`{.docutils .literal .notranslate}]{.pre} 调度器，它每 [`lr_step_size`{.docutils .literal .notranslate}]{.pre} 个 epoch 将学习率衰减 [`lr_gamma`{.docutils .literal .notranslate}]{.pre} 倍。

::: highlight
        learning_rate = 0.1
        momentum = 0.9
        weight_decay = 1e-4
        lr_step_size = 30
        lr_gamma = 0.1
:::

注意

一个训练轮次是指神经网络对整个数据集进行一次前向传播和反向传播的过程。



::: highlight
        epochs = 90

训练和验证目录已被确定。

::: highlight
        train_dir = os.path.join(data_path, "train")
        val_dir = os.path.join(data_path, "val")

10. 设置训练和测试数据加载器。

::: highlight
        interpolation = InterpolationMode(interpolation)

`TRAIN_TRANSFORM_IMG = transforms.Compose([`
`        # 归一化并标准化图像`
`        transforms.RandomResizedCrop(train_crop_size, interpolation=interpolation),`
`            transforms.PILToTensor(),`
`            transforms.ConvertImageDtype(torch.float),`
`            transforms.Normalize(mean=[0.485, 0.456, 0.406],`
`                                std=[0.229, 0.224, 0.225] )`
`            ])`
`        dataset = torchvision.datasets.ImageFolder(`
`            train_dir,`
`            transform=TRAIN_TRANSFORM_IMG`
`        )`
`TEST_TRANSFORM_IMG = transforms.Compose([`
`            transforms.Resize(val_resize_size, interpolation=interpolation),`
`            transforms.CenterCrop(val_crop_size),`
`            transforms.PILToTensor(),`
`            transforms.ConvertImageDtype(torch.float),`
`            transforms.Normalize(mean=[0.485, 0.456, 0.406],`
`                                std=[0.229, 0.224, 0.225] )`
`            ])`

```python
dataset_test = torchvision.datasets.ImageFolder(
            val_dir,
            transform=TEST_TRANSFORM_IMG
        )
```

```python
print("创建数据加载器")
train_sampler = torch.utils.data.RandomSampler(dataset)
test_sampler = torch.utils.data.SequentialSampler(dataset_test)
```

```python
data_loader = torch.utils.data.DataLoader(
            dataset,
            batch_size=batch_size,
            sampler=train_sampler,
            num_workers=num_workers,
            pin_memory=True
        )
```



```python
data_loader_test = torch.utils.data.DataLoader(
            dataset_test, batch_size=batch_size, sampler=test_sampler, num_workers=num_workers, pin_memory=True
        )
```

注意



使用 torchvision 获取 Inception V3 模型。使用预训练模型权重来加速训练。

```python
print("Creating model")
print("Num classes = ", len(dataset.classes))
model = torchvision.models.__dict__[model_name](pretrained=pretrained)
```

11. 使 Inception V3 适应当前数据集。[`tiny-imagenet-200`{.docutils .literal .notranslate}]{.pre} 只包含 200 个类别，而 Inception V3 设计用于 1000 类输出。Inception V3 的最后一层被替换以匹配所需的输出特征。



::: highlight
        model.fc = torch.nn.Linear(model.fc.in_features, len(dataset.classes))
        model.aux_logits = False
        model.AuxLogits = None

12. 将模型移动到 GPU 设备上。

```markdown
::: highlight
        model.to(device)
```

13. 设置损失函数标准。本示例使用交叉熵损失。

::: highlight
        criterion = torch.nn.CrossEntropyLoss()

14. 将优化器设置为随机梯度下降。

::: highlight
        optimizer = torch.optim.SGD(
            model.parameters(),
            lr=learning_rate,
            momentum=momentum,
            weight_decay=weight_decay
        )



15. 设置学习率调度器。

```python
lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=lr_step_size, gamma=lr_gamma)
```

16. 遍历各个 epoch。每个 epoch 是对训练数据的完整一次遍历。

::: highlight
        print("Start training")
        for epoch in range(epochs):
            model.train()
            epoch_loss = 0
            len_dataset = 0

17. 遍历各个步骤。数据按批次进行处理，每个步骤都处理完整批次。



::: highlight
        for step, (image, target) in enumerate(data_loader):



将图像和目标传入 GPU 设备。

```python
image, target = image.to(device), target.to(device)
```

以下为训练的核心逻辑：

a. 图像被输入到模型中。

b. 将输出与训练数据中的目标值进行比较，以获得损失。

c. 该损失反向传播到所有需要优化的参数。

d. 优化器根据所选优化算法更新参数。



```python
output = model(image)
loss = criterion(output, target)
optimizer.zero_grad()
loss.backward()
optimizer.step()
```

训练周期损失已更新，步损失已打印。

    ::: highlight
                epoch_loss += output.shape[0] * loss.item()
                len_dataset += output.shape[0];
                if step % 10 == 0:
                    print('Epoch: ', epoch, '| step : %d' % step, '| train loss : %0.4f' % loss.item() )
            epoch_loss = epoch_loss / len_dataset
            print('Epoch: ', epoch, '| train loss :  %0.4f' % epoch_loss )



学习率在每个 epoch 结束时更新。



::: highlight
        lr_scheduler.step()

完成epoch训练后，模型对验证数据集进行评估。

::: highlight
        model.eval()
            with torch.inference_mode():
                running_loss = 0
                for step, (image, target) in enumerate(data_loader_test):
                    image, target = image.to(device), target.to(device)

output = model(image)
loss = criterion(output, target)



running_loss += loss.item()
running_loss = running_loss / len(data_loader_test)
print('Epoch: ', epoch, '| test loss : %0.4f' % running_loss )

19. 保存模型以用于推理任务。



::: highlight
    # 保存模型
    torch.save(model.state_dict(), "trained_inception_v3.pt")

绘制训练损失和测试损失可以观察到两个指标随着训练轮次的增加而下降。这一点在下图中展示。

![Inception V3 训练和损失图](../_images/inception-v3.png)

### 在 PyTorch 上使用 CIFAR-10 的自定义模型[\#](#custom-model-with-cifar-10-on-pytorch "Link to this heading"){.headerlink}

CIFAR-10数据集是Tiny Images数据集（包含从互联网收集的8000万张32x32图像）的子集，由60000张32x32彩色图像组成。这些图像标记为10个互斥类别之一：飞机、汽车、鸟、猫、鹿、狗、青蛙、游轮、马和卡车（但不包括皮卡车）。每个类别有6000张图像，每个类别5000张用于训练、1000张用于测试。让我们使用PyTorch框架为这些图像分类准备一个自定义模型，并按下图所示逐步进行。

请按以下步骤操作：

1. 导入依赖项，包括 Torch、OS 和 [TorchVision](https://github.com/pytorch/vision){.reference .external}。

```python
        import torch
        import torchvision
        import torchvision.transforms as transforms
        import matplotlib.pyplot as plot
        import numpy as np
```

2. torchvision 数据集的输出是 [`PILImage`{.docutils .literal .notranslate}]{.pre} 范围为 \[0, 1\] 的图像。将它们转换为归一化范围为 \[-1, 1\] 的张量。

```markdown
::: highlight
        transform = transforms.Compose(
                [transforms.ToTensor(),
                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
```

在每个训练步骤中，一批图像被处理以计算损失梯度并执行优化。在以下设置中，批大小被确定。



```highlight
batch_size = 4
```

3. 按如下方式下载训练集和测试集。指定批量大小，对数据集进行一次打乱，并指定工作进程数等于数据加载器执行高效多进程数据加载所使用的 CPU 线程数。

::: highlight
        train_set = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
        train_loader = torch.utils.data.DataLoader(train_set, batch_size=batch_size, shuffle=True, num_workers=2)

4. 对测试集执行相同的步骤。

::: highlight
        test_set = TorchVision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
        test_loader = torch.utils.data.DataLoader(test_set, batch_size=batch_size, shuffle=False, num_workers=2)
        print ("测试集和测试加载器")



5. 指定此数据集中图像的已定义类别。

::: highlight
        classes = ('Aeroplane', 'motorcar', 'bird', 'cat', 'deer', 'puppy', 'frog', 'stallion', 'cruise', 'truck')
        print("defined classes")



6. 对图像进行反归一化，然后对其进行迭代遍历。



::: highlight
        global image_number
        image_number = 0
        def show_image(img):
            global image_number
            image_number = image_number + 1
            img = img / 2 + 0.5     # 对输入图像进行反归一化
            npimg = img.numpy()
            plot.imshow(np.transpose(npimg, (1, 2, 0)))
            plot.savefig("fig{}.jpg".format(image_number))
            print("fig{}.jpg".format(image_number))
            plot.show()
        data_iter = iter(train_loader)
        images, labels = data_iter.next()
        show_image(torchvision.utils.make_grid(images))
        print(' '.join('%5s' % classes[labels[j]] for j in range(batch_size)))
        print("图像已创建并保存")

7.  导入 [`torch.nn`{.docutils .literal .notranslate}]{.pre} 用于构建神经网络，以及 [`torch.nn.functional`{.docutils .literal .notranslate}]{.pre} 来使用卷积函数。

::: highlight
        import torch.nn as nn
        import torch.nn.functional as F

8. 定义 CNN（卷积神经网络）及其相关激活函数



::: highlight
        class Net(nn.Module):
            def __init__(self):
                super().__init__()
                self.conv1 = nn.Conv2d(3, 6, 5)
                self.pool = nn.MaxPool2d(2, 2)
                self.conv2 = nn.Conv2d(6, 16, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv3 = nn.Conv2d(3, 6, 5)
                self.fc2 = nn.Linear(120, 84)
                self.fc3 = nn.Linear(84, 10)



```python
def forward(self, x):
                x = self.pool(F..relu(self.conv1(x)))
                x = self.pool(F.relu(self.conv2(x)))
                x = torch.flatten(x, 1) # flatten all dimensions except batch
                x = F..relu(self.fc1(x))
                x = F.relu(self.fc2(x))
                x = self.fc3(x)
                return x
        net = Net()
        print("created Net() ")
```

9. 将优化器设置为随机梯度下降。

::: highlight
        import torch.optim as optim

10. 设置损失函数。本示例使用 Cross Entropy Loss。

::: highlight
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

11. 遍历各个 epoch。每个 epoch 是对训练数据的完整一次遍历。

::: highlight
        for epoch in range(2):  # 多次遍历数据集



running_loss = 0.0
            for i, data in enumerate(train_loader, 0):
                # get the inputs; data is a list of [inputs, labels]
                inputs, labels = data



# 清零参数梯度
optimizer.zero_grad()

```python
# 前向传播 + 反向传播 + 优化
outputs = net(inputs)
loss = criterion(outputs, labels)
loss.backward()
optimizer.step()
```

# 打印统计信息
                running_loss += loss.item()
                if i % 2000 == 1999:    # 每2000个mini-batches打印一次
                    print('[%d, %5d] 损失: %.3f' % (epoch + 1, i + 1, running_loss / 2000))
                    running_loss = 0.0
        print('训练完成')

::: highlight
        PATH = './cifar_net.pth'
        torch.save(net.state_dict(), PATH)
        print("模型已保存至路径 :",PATH)
        net = Net()
        net.load_state_dict(torch.load(PATH))
        print("加载回保存的模型")
        outputs = net(images)
        _, predicted = torch.max(outputs, 1)
        print('预测: ', ' '.join('%5s' % classes[predicted[j]] for j in range(4)))
        correct = 0
        total = 0
:::

由于此时并非训练过程，因此无需计算输出的梯度。

::: highlight
        # calculate outputs by running images through the network
        with torch.no_grad():
            for data in test_loader:
                images, labels = data
                # calculate outputs by running images through the network
                outputs = net(images)
                # the class with the highest energy is what you can choose as prediction
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
        print('Accuracy of the network on the 10000 test images: %d %%' % ( 100 * correct / total))
        # prepare to count predictions for each class
        correct_pred = {classname: 0 for classname in classes}
        total_pred = {classname: 0 for classname in classes} :::



::: highlight
        # 同样不需要计算梯度
        with torch.no_grad():
            for data in test_loader:
                images, labels = data
                outputs = net(images)
                _, predictions = torch.max(outputs, 1)
                # 收集每个类别的正确预测数
                for label, prediction in zip(labels, predictions):
                    if label == prediction:
                        correct_pred[classes[label]] += 1
                    total_pred[classes[label]] += 1
        # 打印每个类别的准确率
        for classname, correct_count in correct_pred.items():
            accuracy = 100 * float(correct_count) / total_pred[classname]
            print("类别 {:5s} 的准确率为: {:.1f} %".format(classname,accuracy))
:::

### 案例研究：TensorFlow 与 Fashion-MNIST [#](#case-study-tensorflow-with-fashion-mnist "Link to this heading"){.headerlink}

Fashion-MNIST 是一个包含 70,000 张灰度图像的数据集，共 10 个类别。



使用 TensorFlow 框架实现并训练神经网络模型，对服装图像（如运动鞋和衬衫）进行分类。

该数据集包含 60,000 张图像用于训练网络，以及 10,000 张用于评估网络学习图像分类的准确程度。Fashion-MNIST 数据集可通过 TensorFlow 内部库访问。

从以下仓库访问源代码：

[ROCm/tensorflow_fashionmnist](https://github.com/ROCm/tensorflow_fashionmnist/blob/main/fashion_mnist.py){.github .reference .external}



要逐步理解代码，请按以下步骤操作：

导入 TensorFlow、NumPy 和 Matplotlib 等库来训练神经网络并计算和绘制图表。

::: highlight
        import tensorflow as tf
        import numpy as np
        import matplotlib.pyplot as plt

2. 要验证 TensorFlow 是否已安装，请使用下面的打印语句打印 TensorFlow 的版本：

::: highlight
        print(tf._version__) r



3. 从可用的内部库加载数据集，以在 Fashion-MNIST 数据集上分析和训练神经网络。加载数据集将返回四个 NumPy 数组。模型使用训练集数组 train_images 和 train_labels 进行学习。

4. 使用测试集 test_images 和 test_labels 数组对模型进行测试。

This is a technical translation request. I need to translate the English text to Simplified Chinese while following the specific rules:

1. Preserve ALL markdown formatting, code blocks, inline code, and links unchanged.
2. Keep technical terms like ROCm, HIP, GPU, CUDA, AMD, PyTorch, TensorFlow in their original English form.
3. Keep API names, function names, file paths, commands unchanged.
4. Output ONLY the translation — no explanations, no notes, no preamble.
5. Use technical Chinese that a GPU developer would expect.

The text provided is code in a markdown code block. Looking at it:
- It contains Python/TensorFlow code
- It uses `tf.keras.datasets.fashion_mnist` which is a technical reference
- The code itself should remain unchanged as it's code
- The comment/title "highlight" is markdown formatting

According to the rules:
- Preserve ALL markdown formatting, code blocks, inline code, and links unchanged
- Keep API names, function names, file paths, commands unchanged

Since this is a code block, and all the terms are either standard library/API references or technical terms that should remain in English, the appropriate translation would be to keep the code unchanged but perhaps add Chinese comments if there were any. However, there are no comments here.

Wait, let me reconsider. The instruction says to translate English text to Simplified Chinese. But the content here is entirely code. Code should not be translated - API names, function names, file paths, commands should remain unchanged. So the code block should remain as is.

Actually, looking more carefully at the context, this appears to be a snippet of code with markdown highlighting syntax. The user wants me to translate "the English text" but in this case, the "English text" is code. The rules explicitly state to keep API names, function names, file paths, commands unchanged.

So the answer should be the code block exactly as provided, perhaps with appropriate translation of any comments (but there are none here).

Let me just return the code block unchanged since:
1. It's code
2. The technical terms should remain in English
3. There's no natural language text to translate here

The output should be:
```markdown
::: highlight
        fashion_mnist = tf.keras.datasets.fashion_mnist
        (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
```

Actually, looking at the user's input again, it's just these two lines of code in a markdown block. Since there's no actual English prose/natural language text to translate - only code - and the rules say to keep code unchanged, I should output the code exactly as it is.




由于数据集中有10种类型的图像，分配从0到9的标签。每张图像分配一个标签。图像是28x28的NumPy数组，像素值范围从0到255。

5. 每张图像对应一个标签。由于类别名称未包含在数据集中，需要将其存储，后续在绘制图像时使用：



::: highlight
        class__names = ['T恤/上衣', '裤子', '套头衫', '连衣裙', '外套', '凉鞋', '衬衫', '运动鞋', '背包', '短靴']

6. 使用此代码通过了解其维度来探索数据集：



::: highlight
        train_images.shape
:::

7. 使用此代码打印此训练集的大小：

print(len(train_labels))

8. 使用此代码来打印此训练集的标签：

::: highlight
        print(train_labels)

9. 在训练网络之前先对数据进行预处理，您可以开始检查第一张图像，因为其像素值落在 0 到 255 的范围内。

::: highlight
        plt.figure()
        plt.imshow(train_images[0])
        plt.colorbar()
        plt.grid(False)
        plt.show()

![ ](../_images/mnist-1.png)



从上面的图片中可以看到，值的范围是从 0 到 255。在将其输入 neural network 进行训练之前，必须将其归一化到 0 到 1 的范围内。因此，将值除以 255。

::: highlight
        train_images = train_images / 255.0

test_images = test_images / 255.0

11. 为确保数据格式正确并准备好构建和训练网络，请显示训练集中的前25张图像，并在每张图像下方显示类别名称。

```python
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()
```

![ ](../_images/mnist-2.png)

神经网络的基本构建块是层。层从输入的数据中提取表示。深度学习由将简单层串联在一起组成。大多数层，例如 [`tf.keras.layers.Dense`{.docutils .literal .notranslate}]{.pre}，具有在训练过程中学习的参数。



```python
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])
```



网络中第一层 `tf.keras.layers.Flatten` 将图像的格式从二维数组（28 x 28 像素）转换为一维数组（28 * 28 = 784 像素）。可以将该层视为展开图像中的像素行并将它们排列起来。该层没有待学习的参数，它仅重新格式化数据。

像素被展平后，网络由两个连续的 [`tf.keras.layers.Dense`{.docutils .literal .notranslate}]{.pre} 层组成。这些是密集连接或全连接神经层。第一个 Dense 层有 128 个节点（或神经元）。第二个（也是最后一个）层返回一个长度为 10 的 logits 数组。每个节点包含一个分数，表示当前图像属于 10 个类别之一。



12. 您必须在模型编译时添加损失函数、指标和优化器。

::: highlight
        model.compile(optimizer='adam',
                    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                    metrics=['accuracy'])

- 损失函数---这用于衡量模型在训练过程中的准确程度，当你想要最小化这个函数来"引导"模型走向正确的方向时。



优化器——这是模型根据所看到的数据及其损失函数进行更新的方式。

- 指标 ---用于监控训练和测试步骤。

以下示例使用准确率，即正确分类图像的比例。

要训练神经网络模型，请按照以下步骤操作：

1. 将训练数据输入模型。在本例中，训练数据位于 `train_images` 和 `train_labels` 数组中。模型学习将图像与标签关联起来。

2. 让模型对测试集进行预测——在这个例子中，是 `test_images` 数组。

3. 验证预测结果是否与 test_labels 数组中的标签匹配。



4. 要开始训练，请调用 model.fit 方法，因为它会将模型"拟合"到训练数据上。



::: highlight
            model.fit(train_images, train_labels, epochs=10)

5. 比较模型在测试数据集上的表现。

        ::: highlight
            test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\n测试准确率:', test_acc)



6.  模型训练完成后，您可以使用它来对一些图像进行预测：模型的线性输出和 logits。附加一个 softmax 层，将 logits 转换为概率，使其更易于解释。

::: highlight
            probability_model = tf.keras.Sequential([model,
                                                    tf.keras.layers.Softmax()])

```python
predictions = probability_model.predict(test_images)
```

7. 模型已对测试集中每张图像进行了标签预测。查看第一个预测结果：

::: highlight
predictions[0]

一个预测是一个包含10个数字的数组。它们代表模型对该图像属于10种不同服装类别的“置信度”。你可以看到哪个标签具有最高的置信度值：

::: highlight
            np.argmax(predictions[0])

8. 绘制图表以查看完整的 10 个类别预测结果。

```python
def plot_image(i, predictions_array, true_label, img):
    true_label, img = true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
```

plt.imshow(img, cmap=plt.cm.binary)

predicted_label = np.argmax(predictions_array)
            if predicted_label == true_label:
                color = 'blue'
            else:
                color = 'red'



```python
plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                            100*np.max(predictions_array),
                                            class_names[true__label]),
                                            color=color)
```

def plot_value_array(i, predictions_array, true_label):
    true_label = true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

```
thisplot[predicted_label].set_color('red')
thisplot[true_label].set_color('blue')
```

9. 模型训练完成后，您可以使用它对一些图像进行预测。查看第0^th^张图像的预测和预测数组。正确的预测标签用蓝色表示，错误的预测标签用红色表示。数字表示预测标签的百分比（满分100）。

::: highlight
            i = 0
            plt.figure(figsize=(6,3))
            plt.subplot(1,2,1)
            plot_image(i, predictions[i], test_labels, test_images)
            plt.subplot(1,2,2)
            plot_value_array(i, predictions[i],  test_labels)
            plt.show()

![](../_images/mnist-3.png)

```
i = 12
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions[i],  test_labels)
plt.show()
```

![](../_images/mnist-4.png)

10. 使用训练后的模型对单张图像进行预测。



::: highlight
            # Grab an image from the test dataset.
            img = test_images[1]
            print(img.shape)

11. `tf.keras` 模型经过优化，可以一次对一批（即一组）样本进行预测。因此，即使你使用的是单个图像，也必须将其添加到列表中。

::: highlight
            # 将图像添加到批次中作为唯一的成员。
            img = (np.expand_dims(img,0))
:::

print(img.shape)

12. 预测这张图片的正确标签

::: highlight
            predictions_single = probability_model.predict(img)

print(predictions_single)

plot_value_array(1, predictions_single[0], test_labels)
            _ = plt.xticks(range(10), class_names, rotation=45)
            plt.show()



![ ](../_images/mnist-5.png)

13. [`tf.keras.Model.predict`{.docutils .literal .notranslate}]{.pre} 返回一个列表的列表——批次中的每个图像对应一个。获取我们（唯一的）图像在批次中的预测结果。

```highlight
np.argmax(predictions_single[0])
```

### 案例研究：TensorFlow 与文本分类[\#](#case-study-tensorflow-with-text-classification "Link to this heading"){.headerlink}

本教程演示了从存储在磁盘上的纯文本文本文件开始的文本分类。您将训练一个二分类器来对IMDB数据集进行情感分析。在笔记本的最后，有一个练习供您尝试，在该练习中，您将训练一个多分类器来预测Stack Overflow上编程问题的标签。

请按以下步骤操作



1. 导入必要的库。

::: highlight
        import matplotlib.pyplot as plt
        import os
        import re
        import shutil
        import string
        import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import losses

2. 获取文本分类的数据，并从给定的 IMDB 链接中提取数据库。

::: highlight
        url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"

dataset = tf.keras.utils.get_file("aclImdb_v1", url,
                                            untar=True, cache_dir='.',
                                            cache_subdir='')



```::: highlight
        正在从 https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz 下载数据
        84/4s 13/84 1s 25825 ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ - 1s 0us/step
        84/4s 499/84 1s 25825 ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ - 1s 0us/step
```

3. 从目录中获取数据。



```
::: highlight
        dataset_dir = os.path.join(os.path.dirname(dataset), 'aclImdb')
        print(os.listdir(dataset_dir))
```

4. 加载训练数据。

::: highlight
        train_dir = os.path.join(dataset_dir, 'train')
        os.listdir(train_dir)

::: highlight
        ['labeledBow.feat',
        'urls_pos.txt',
        'urls_unsup.txt',
        'unsup',
        'pos',
        'unsupBow.feat',
        'urls_neg.txt',
        'neg'] :::

5.  目录包含许多文本文件，每个文件都是一条影评。要查看其中一个，请使用以下方法：



::: highlight
        sample_file = os.path.join(train_dir, 'pos/1181_9.txt')
        with open(sample_file) as f:
        print(f.read())



6. 由于 IMDB 数据集包含额外的文件夹，请在使用此工具前将其删除。

::: highlight
        remove_dir = os.path.join(train_dir, 'unsup')
        shutil.rmtree(remove_dir)
        batch_size = 32
        seed = 42
:::

7. IMDB 数据集已经被划分为训练集和测试集，但缺少验证集。请使用下面的 validation_split 参数，通过 80:20 的分割比例从训练数据中创建验证集：



::: highlight
        raw_train_ds=tf.keras.utils.text_dataset_from_directory('aclImdb/train',batch_size=batch_size, validation_split=0.2,subset='training', seed=seed)

8. 正如你稍后将看到的，你可以通过直接将数据集传递给 [`model.fit`{.docutils .literal .notranslate}]{.pre} 来训练模型。如果你是初次使用 [`tf.data`{.docutils .literal .notranslate}]{.pre}，你也可以遍历数据集并打印几个示例，如下所示：

::: highlight
for text_batch, label_batch in raw_train_ds.take(1):
    for i in range(3):
        print("评论", text_batch.numpy()[i])
        print("标签", label_batch.numpy()[i])

9. 标签为0或一。要查看这些标签对应的是正面还是负面电影评论，请查看数据集的class_names属性。

::: highlight
        print("Label 0 corresponds to", raw_train_ds.class_names[0])
        print("Label 1 corresponds to", raw_train_ds.class_names[1])
:::



10. 接下来，创建验证和测试数据集。从训练集中剩余的 5,000 条评论中划分出 2,500 条用于验证，分为两类。

::: highlight
        raw_val_ds = tf.keras.utils.text_dataset_from_directory('aclImdb/train',
        batch_size=batch_size,validation_split=0.2,subset='validation', seed=seed)



raw_test_ds =
        tf.keras.utils.text_dataset_from_directory(
            'aclImdb/test',
            batch_size=batch_size)

要准备训练数据，请按以下步骤操作：

1. 使用实用的 [`tf.keras.layers.TextVectorization`{.docutils .literal .notranslate}]{.pre} 层对数据进行标准化、分词和向量化处理。



::: highlight
        def custom_standardization( input_data):
        lowercase = tf.strings.lower(input_ data)
        stripped_html = tf.strings.regex_replace(lowercase,

2. 创建一个 [`TextVectorization`{.docutils .literal .notranslate}]{.pre} 层。使用此层对我们的数据进行标准化、分词和向量化。将 output_mode 设置为 int，为每个分词符创建唯一的整数索引。请注意，我们使用的是默认的 split 函数和上面定义的自定义 standardization function。您还需要为模型定义一些常量，例如显式的 maximum sequence_length，这会导致该层将序列填充或截断到 exactly sequence_length 值。

::: highlight
        max_features = 10000
        sequence_length = 250
        vectorize_layer = layers.TextVectorization(
            standardize=custom_standardization,
            max_tokens=max_features,
            output_mode='int',
            output_sequence_length=sequence_length)
:::

3.  调用 adapt 使预处理层适配数据集的状态。这会导致模型建立一个字符串到整数的索引。



```highlight
        # Make a text-only dataset (without labels), then call adapt
        train_text = raw_train_ds.map(lambda x, y: x)
        vectorize_layer.adapt(train_text)
```

4. 创建一个函数来查看使用此层预处理一些数据的结果。



```python
def vectorize_text(text, label):
    text = tf.expand_dims(text, -1)
    return vectorize_layer(text), label
```



```python
text_batch, label_batch = next(iter(raw_train_ds))
first_review, first_label = text_batch[0], label_batch[0]
print("评论", first_review)
print("标签", raw_train_ds.class_names[first_label])
print("向量化后的评论", vectorize_text(first_review, first_label))
```

![ ](../_images/TextClassification-3.png)

5. 如上所示，每个 token 都已被替换为一个整数。通过对该层调用 `get_vocabulary()`，可以查找每个整数对应的 token（字符串）。

::: highlight
        print("1287 ---> ",vectorize_layer.get_vocabulary()[1287])
        print(" 313 ---> ",vectorize_layer.get_vocabulary()[313])
        print('词汇表大小: {}'.format(len(vectorize_layer.get_vocabulary())))

6. 您即将准备好训练您的模型。作为最后的预处理步骤，应用之前创建的 [`TextVectorization`{.docutils .literal .notranslate}]{.pre} 层对数据集进行训练、验证和测试。

The user wants me to translate the given English text to Simplified Chinese. This appears to be a code snippet from a machine learning/text classification tutorial, likely using TensorFlow.

Let me analyze:
1. This is a code block showing data preprocessing with TensorFlow's dataset API
2. The code maps the vectorize_text function to train, validation, and test datasets
3. It's likely part of a text classification tutorial using the IMDb dataset

I need to:
1. Preserve the markdown formatting (highlight, :::)
2. Preserve the code block unchanged
3. Translate only any explanatory text (but there's none here - just pure code)
4. Output only the translation

Since this is pure code with no English explanatory text to translate, I should just return it as-is. Code should never be translated - API names, function names, variable names all stay the same.

Let me output the exact same code block since it's purely technical content.


[`cache()`{.docutils .literal .notranslate}]{.pre} 函数在数据从磁盘加载后将其保留在内存中。这确保数据集在训练模型时不会成为瓶颈。如果你的数据集太大，无法放入内存，你也可以使用此方法来创建高性能的磁盘缓存，这比读取多个小文件更高效。

[`prefetch()`{.docutils .literal .notranslate}]{.pre} 函数在训练时将数据预处理和模型执行进行重叠处理。

::: highlight
        AUTOTUNE = tf.data.AUTOTUNE



```python
train_ds = train_ds.cache().prefetch(buffer_size=buffer_size)
val_ds = val_ds.cache().prefetch(buffer_size=buffer_size)
test_ds = test_ds.cache().prefetch(buffer_size=buffer_size)
```



7.  创建你的神经网络。



::: highlight
        embedding_dim = 16
        model = tf.keras.Sequential([layers.Embedding(max_features + 1, embedding_dim),layers.Dropout(0.2),layers.GlobalAveragePooling1D(),
        layers.Dropout(0.2),layers.Dense(1)])
        model.summary()

![ ](../_images/TextClassification-4.png)

8.  模型需要损失函数和优化器来进行训练。由于这是一个二分类问题且模型输出一个概率（带有sigmoid激活的单单元层），因此使用 [[`losses.BinaryCrossentropy`{.docutils .literal .notranslate}]{.pre}](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryCrossentropy){.reference .external} 损失函数。

```python
model.compile(loss=losses.BinaryCrossentropy(from_logits=True),
optimizer='adam',metrics=tf.metrics.BinaryAccuracy(threshold=0.0))
```

9. 通过将数据集对象传递给 fit 方法来训练模型。

::: highlight
        epochs = 10
        history = model.fit(train_ds,validation_data=val_ds,epochs=epochs)



![](../_images/TextClassification-5.png)

10. 查看模型的表现。返回两个值：损失值（loss，一个表示误差的数值，越小越好）和准确率（accuracy）。



::: highlight
        loss, accuracy = model.evaluate(test_ds)



print("损失: ", loss)
        print("准确率: ", accuracy)

注意

[`model.fit()`{.docutils .literal .notranslate}]{.pre} 返回一个 History 对象，该对象包含一个字典，记录了训练过程中发生的所有情况。

::: highlight
        history_dict = history.history
        history_dict.keys()

11. 在训练和验证期间，每个监控指标都有四个条目。使用这些可以绘制训练和验证损失以进行对比，以及训练和验证准确率：

::: highlight
        acc = history_dict['binary_accuracy']
        val_acc = history_dict['val_binary_accuracy']
        loss = history_dict['loss']
        val_loss = history_dict['val_loss']

epochs = range(1, len(acc) + 1)



# "bo" 代表"蓝色点"
        plt.plot(epochs, loss, 'bo', label='训练损失')
        # b 代表"实线蓝色"
        plt.plot(epochs, val_loss, 'b', label='验证损失')
        plt.title('训练和验证损失')
        plt.xlabel('轮次')
        plt.ylabel('损失')
        plt.legend()

plt.show()

下图展示了训练损失、验证损失、训练准确率和验证准确率。



![训练和验证损失](../_images/TextClassification-6.png)

![训练和验证准确率](../_images/TextClassification-7.png)

12. 导出模型。

::: highlight
        export_model = tf.keras.Sequential([
        vectorize_layer,
        model,
        layers.Activation('sigmoid')
        ])

```python
export_model.compile(
            loss=losses.BinaryCrossentropy(from_logits=False), optimizer="adam", metrics=['accuracy']
        )
```

# 使用 `raw_test_ds` 进行测试，它返回原始字符串
        loss, accuracy = export_model.evaluate(raw_test_ds)
        print(accuracy)

13. 要获取新样本的预测结果，请调用 model.predict()。

::: highlight
        examples = [
        "这部电影很棒！",
        "这部电影还可以。",
        "这部电影太糟糕了..."
        ]

export_model.predict(examples)

[](cmake-packages.html "上一页"){.left-prev}

上一页

The user wants me to translate "Using CMake" from English to Simplified Chinese. This is a heading/title typically found in documentation.

"Using CMake" is a common heading in technical documentation. I need to translate it while:
1. Preserving the formatting (this appears to be a heading)
2. Using appropriate technical Chinese

In technical documentation, "Using CMake" would typically be translated as:
- "使用 CMake" (literal translation)

This is the standard way to translate this heading in technical Chinese documentation.


[](../reference/api-libraries.html "下一页"){.right-next}

::: prev-next-info
next



ROCm（Radeon 开放计算平台）库

:::: sidebar-secondary-item
目录



- [深度学习训练](#deep-learning-training){.reference .internal .nav-link}
- [训练阶段](#training-phases){.reference .internal .nav-link}
- [案例研究](#case-studies){.reference .internal .nav-link}
  - [Inception V3 与 PyTorch](#inception-v3-with-pytorch){.reference .internal .nav-link}
    - [评估预训练模型](#evaluating-a-pre-trained-model){.reference .internal .nav-link}
    - [训练 Inception V3](#training-inception-v3){.reference .internal .nav-link}
  - [CIFAR-10 上的自定义模型与 PyTorch](#custom-model-with-cifar-10-on-pytorch){.reference .internal .nav-link}
  - [案例：TensorFlow 与 Fashion-MNIST](#case-study-tensorflow-with-fashion-mnist){.reference .internal .nav-link}
  - [案例：TensorFlow 与文本分类](#case-study-tensorflow-with-text-classification){.reference .internal .nav-link}