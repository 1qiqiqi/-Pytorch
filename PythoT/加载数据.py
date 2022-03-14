from PIL import Image
import os
from torch.utils.data import Dataset
class Mydata(Dataset):
    def __init__(self,root_dir,label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir,self.label_dir)
        self.img_path = os.listdir(self.path)
    def __getitem__(self, idx):
        img_name = self.img_path[idx]
        img_item_path = os.path.join(self.root_dir,self.label_dir,img_name)
        img = Image.open(img_item_path)
        label = self.label_dir
        return img,label
    def __len__(self):
        return len(os.path.join(self.img_path))
root_dir = '神经网络\\Dataset\\train'
label_dir = 'ants'
mydata = Mydata(root_dir,label_dir)
print(mydata[0])



