from imageai.Detection import ObjectDetection
import os
from selenium import webdriver
import time

DRIVER = 'chromedriver.exe'
driver = webdriver.Chrome(DRIVER)

driver.get('https://www.earthcam.com/world/ireland/dublin/?cam=templebar')
time.sleep(32)
k = 0
driver.save_screenshot("objects.jpg")
exec_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(
	exec_path, "resnet50_coco_best_v2.0.1.h5")
)
detector.loadModel()

list = detector.detectObjectsFromImage(
	input_image=os.path.join(exec_path, "objects.jpg"),
	output_image_path=os.path.join(exec_path, "new_objects.jpg"),
	minimum_percentage_probability=30)
for eachObject in list:
	if (eachObject["name"] == "bicycle"): k += 1
print("bicycles: ", k)
driver.quit()