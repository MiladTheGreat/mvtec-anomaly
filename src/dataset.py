import os
from torch.utils.data import Dataset
from PIL import Image
from torchvision import transforms


class BottleDataset(Dataset):
    def __init__(self,root_dir,transform=None,label=None):

        
        self.root_dir = root_dir
        self.image_files = [i for i in os.listdir(self.root_dir) if i.endswith(('jpg','png'))]
        self.transform = transform
        self.label = label
    def __len__(self):
        return len(self.image_files)
    
    def __getitem__(self, index):
        img_path = os.path.join(self.root_dir,self.image_files[index])
        image = Image.open(img_path).convert('RGB')

        if self.transform:
            image = self.transform(image)
        
        return image

