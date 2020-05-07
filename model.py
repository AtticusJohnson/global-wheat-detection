import warnings
import mxnet as mx
import gluoncv as gcv


def init_model(ctx=mx.cpu()):
    net = gcv.model_zoo.yolo3_darknet53_custom(["wheat"])
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        net.initialize(mx.init.Xavier(), ctx=ctx)
    return net

def load_model(path, ctx=mx.cpu()):
    net = gcv.model_zoo.yolo3_darknet53_custom(["wheat"], pretrained_base=False)
    net.load_parameters(path, ctx=ctx)
    return net
