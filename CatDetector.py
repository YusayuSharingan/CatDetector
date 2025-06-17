from torchvision.models.detection import ssd300_vgg16
from PIL import Image
import numpy as np
import os

import matplotlib.pyplot as plt
import matplotlib.patches as patches


class CatDetector:
    __classes = ["background", "tiger", "leopard"]

    def __init__(self, path="best_ssd.pth"):
        self.__model = ssd300_vgg16(weights=path)

    def detect(self, path):
        img = Image(path)
        img = np.array(img)
        preds = self.__model(img)

        img = img.permute(1, 2, 0)
        _, ax = plt.subplots(1)
        ax.imshow(img)        

        for p in preds:
            filter = p["scores"] > 0.2
            for box, cls in zip(p["boxes"][filter], p["labels"][filter]):
                xmin, ymin, xmax, ymax = box
                rect = patches.Rectangle(
                    (xmin, ymin), xmax - xmin, ymax - ymin,
                    linewidth=2, edgecolor='r', facecolor='none'
                )
                ax.add_patch(rect)
                if self.__classes != None:
                    ax.text(
                        xmin, ymin-5, self.__classes[cls],
                        color='yellow', fontsize=12, 
                        weight='bold'
                    )
        plt.axis('off')

        os.makedirs("output", exist_ok=True)
        file = os.path.splitext(path)

        plt.savefig(f"output/{file[0]}_detected{file[1]}")


if __name__ == "__main__"():
    detector = CatDetector()
    detector.detect(input())
            
