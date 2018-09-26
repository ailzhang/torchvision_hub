from torchvision.models.resnet import resnet18

def wrapper(pretrained=False, **kwargs):
    model = resnet18(pretrained, **kwargs)
    return model

