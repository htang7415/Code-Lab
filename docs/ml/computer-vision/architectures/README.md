# Vision Architectures

CNN architectures mainly differ in how they trade depth, width, skip connections, and classifier heads.

## Current Anchors

- LeNet-5 (`modules/ml/computer-vision/lenet-5`)
- AlexNet (`modules/ml/computer-vision/alexnet`)
- VGGNet (`modules/ml/computer-vision/vggnet`)
- ResNet (`modules/ml/computer-vision/resnet`)
- Pooling (`modules/ml/computer-vision/pooling`)
- Global average pooling (`modules/ml/computer-vision/global-average-pooling`)

## Concepts to Cover Well

- Early CNNs as progressively deeper feature hierarchies
- Pooling vs stride for spatial downsampling
- VGG-style repeated blocks vs ResNet skip connections
- Global average pooling as a lighter classifier head than flattening
- Why architecture choices change parameter count, stability, and translation tolerance
