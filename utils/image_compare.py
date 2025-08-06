import cv2

def compare_images(img1_path, img2_path, threshold=0.95):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)
    if img1.shape != img2.shape:
        return False

    result = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)
    return max_val >= threshold
