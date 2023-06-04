from torchvision import datasets
import os

# Load the image datasets using ImageFolder
def className(path):
    image_datasets = {x: datasets.ImageFolder(os.path.join(path, x)) for x in ['Training', 'Test']}

    # Get the class names
    return image_datasets['Training'].classes
    