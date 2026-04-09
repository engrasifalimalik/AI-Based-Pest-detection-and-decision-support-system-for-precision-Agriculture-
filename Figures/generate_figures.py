
import os
import cv2
import matplotlib.pyplot as plt

dataset_path = "data/raw"  # Update with your dataset path
classes = os.listdir(dataset_path)

plt.figure(figsize=(12, 8))
count = 0

for cls in classes:
    class_path = os.path.join(dataset_path, cls)
    images = os.listdir(class_path)

    if images:
        img_path = os.path.join(class_path, images[0])
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        plt.subplot(2, 3, count + 1)
        plt.imshow(img)
        plt.title(cls)
        plt.axis("off")

        count += 1
        if count == 6:
            break

plt.tight_layout()
plt.savefig("figures/dataset/dataset_samples.png", bbox_inches="tight", dpi=300)
plt.show()
