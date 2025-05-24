"""
70% das imagens para train(treinar o modelo)
15% para val(validação)
15% test(para testar apos o modelo estiver treinado)
"""
import os
import random
import shutil

PATH = "data"

class_labels = ['amarela', 'biscoita', 'bugi', 'frankie', 'pikichita', 'milei',
                 'preta-cristina', 'pulga', 'quenga', 'quilla', 'rosita']

def collect_all_imgs_for_each_class():
    all_images = []
    for dirpath, dirnames, filenames in os.walk(PATH):
        for file in filenames:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_path = os.path.join(dirpath, file)
                all_images.append(full_path)
    return all_images

def image_count(class_name: str):
    count = 0
    img_collection = collect_all_imgs_for_each_class()
    for img_path in img_collection:
        if class_name in img_path:
            count = count + 1
    return count

def total_imgs():
    total=0
    for class_name in class_labels:
        count=image_count(class_name)
        print(f"{class_name}={count}")
        total = total + count
    return total

def split_data():
    random.seed(42)
    
    for split in ['train', 'val', 'test']:
        for label in class_labels:
            os.makedirs(os.path.join(PATH, split, label), exist_ok=True)
            print(PATH, split, label)
            
    for label in class_labels:
        class_path = os.path.join(PATH, label)
        print("class_path: ", class_path)
        if not os.path.exists(class_path):
            raise FileNotFoundError(f"path does not exists: {class_path}")
        
        images = [img for img in os.listdir(class_path)
                  if img.lower().endswith(('.png', '.jpg', '.jpeg'))]
         
        total = len(images)
        if total == 0: raise Exception(f"No image for class '{label}'.")
        
        random.shuffle(images)
        
        train_len = int(total * 0.7)
        val_len = int(total * 0.15)
        test_len = total - train_len - val_len
        
        split_sets = {
            'train': images[:train_len],
            'val': images[train_len:train_len+val_len],
            'test': images[train_len+val_len:]
        }
        
        for split, imgs in split_sets.items():
            for img in imgs:
                src = os.path.join(class_path, img)
                print("src: ", src)
                dst = os.path.join(PATH, split, label, img)
                print("dst: ", dst)
                shutil.copy(src, dst)
                
        print(f"{label}: {train_len} train, {val_len} val, {test_len} test")
        
if __name__ == '__main__':
    split_data()