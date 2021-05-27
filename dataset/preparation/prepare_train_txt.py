import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.join(path, '../train')
train_dirs = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
with open(os.path.join(directory, 'train.txt'), 'w') as f:
    f.write('\n'.join(train_dirs))