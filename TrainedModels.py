from keras.applications import vgg16, vgg19, xception, inception_v3,  inception_resnet_v2, mobilenet, densenet, nasnet, mobilenet_v2

vgg_model = vgg16.VGG16(weights='imagenet')

vgg19_model = vgg19.VGG19(weights='imagenet')

mobilenet_v2_model = mobilenet_v2.MobileNetV2(input_shape=None, alpha=1.0,
                                       include_top=True,
                                       weights='imagenet')

nasnetmobile_model = nasnet.NASNetMobile(weights="imagenet")

densenet_model = densenet.DenseNet201(weights="imagenet")

mobilenet_model = mobilenet.MobileNet(weights="imagenet")

inception_resnet_v2_model = inception_resnet_v2.InceptionResNetV2(include_top=True, weights='imagenet',
                                                input_tensor=None, input_shape=None, pooling=None, classes=1000)

inception_v3_model = inception_v3.InceptionV3(include_top=True, weights='imagenet', input_tensor=None,
                                   input_shape=None, pooling=None, classes=1000)

xception_model = xception.Xception(include_top=True, weights='imagenet', input_tensor=None,
                              input_shape=None, pooling=None, classes=1000)

large_nasnet_model = nasnet.NASNetLarge(input_shape=None, include_top=True, weights='imagenet',
                                  input_tensor=None, pooling=None, classes=1000)
