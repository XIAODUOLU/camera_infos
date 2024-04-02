import cv2
import os

width_normalize = 300

def normalize_imgs(src_dir, dst_dir):
    filenames = os.listdir(src_dir)
    for filename in filenames:
        img = cv2.imread(os.path.join(src_dir, filename))
        Ssize = img.shape
        new_img = cv2.resize(img, dsize=None, fx=width_normalize/Ssize[1], fy=width_normalize/Ssize[1])
        cv2.imwrite(os.path.join(dst_dir, filename), new_img)

if __name__ == "__main__":
    normalize_imgs("./ori_imgs", "./相机攻略/imgs")
