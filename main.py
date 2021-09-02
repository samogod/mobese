import cv2
import mobese
import imutils
import numpy as np
import random
from colorama import Fore, Back, Style, init
import colorama, colorsys
colorama.init(autoreset=False)

mobese = mobese.secim()
yolo_config = "model/yolov4-tiny.cfg"
yolo_weights = "model/yolov4-tiny.weights"
yolo_races = cv2.dnn.readNetFromDarknet(yolo_config, yolo_weights)
confidence_races = ''
frame_width = 1200
red = Fore.RED
bos = "\033[1;37m"

#size = (1920, 1080)
with open("model/coco.names","r", encoding="UTF-8") as f:
    labels = f.read().strip().split("\n")
    
def random_colors(size):
    for i in range(0,size-1):
        h,s,l = random.random(), 0.5 + random.random()/2.0, 0.4 + random.random()/5.0
        r,g,b = [int(256*i) for i in colorsys.hls_to_rgb(h,l,s)]
        yield (r,g,b)

def mobese_track(yolo_races, mobese, confidence_races, overlapping_threshold, labels = None, frame_resize_width=None):
    try:
        colors = list(random_colors(len(labels)))
        ln = yolo_races.getLayerNames()
        ln = [ln[i[0] - 1] for i in yolo_races.getUnconnectedOutLayers()]
        cap = cv2.VideoCapture(mobese)
        '''result = cv2.VideoWriter('filename.mp4',
                            cv2.VideoWriter_fourcc(*'mp4v'),
                            23, size)''' #for save preview video or something.
        try:
            if not cap.isOpened():
                return print(f"{red}[ - ]{bos} Mobese görüntüsüne erişilemedi.\n{red}[ - ]{bos} Farklı bir kamerayı açmayı deneyin.\n{red}[ - ]{bos} Sorun devam ederse >> https://github.com/samet-g/mobese\n{red}[ - ]{bos} Güncellemeleri kontrol edin.")
            
            yolo_width_height = (320, 320)
            max_count = 0

            while True:
                (_, frame) = cap.read()            
                if frame_resize_width:
                    frame = imutils.resize(frame, width=frame_resize_width)
                (H, W) = frame.shape[:2]
                blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, yolo_width_height, swapRB=True, crop=False)
                yolo_races.setInput(blob)
                layerOutputs = yolo_races.forward(ln)
                boxes = []
                confidences = []
                classIDs = []
                for output in layerOutputs:
                    for detection in output:
                        scores = detection[5:]
                        classID = np.argmax(scores)
                        confidence = scores[classID]
                        if confidence > confidence_races:
                            box = detection[0:4] * np.array([W, H, W, H])
                            (centerX, centerY, width, height) = box.astype("int")
                            x = int(centerX - (width / 2))
                            y = int(centerY - (height / 2))
                            boxes.append([x, y, int(width), int(height)])
                            confidences.append(float(confidence))
                            classIDs.append(classID)

                bboxes = cv2.dnn.NMSBoxes(
                    boxes, confidences, confidence_races, overlapping_threshold)
                if len(bboxes) > 0:
                    for i in bboxes.flatten():
                        (x, y) = (boxes[i][0], boxes[i][1])
                        (w, h) = (boxes[i][2], boxes[i][3])
                        color = [int(c) for c in colors[classIDs[i]]]
                        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                        text = "{}".format(labels[classIDs[i]])
                        
                        text_offset_x = x
                        text_offset_y = y
                        text_color = (255, 255, 255)
                        (text_width, text_height) = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, thickness=1)[0]
                        box_coords = ((text_offset_x, text_offset_y), (text_offset_x + text_width - 80, text_offset_y - text_height + 4))
                        cv2.rectangle(frame, box_coords[0], box_coords[1], color, cv2.FILLED)
                        cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1)
                #result.write(frame)
                cv2.imshow("https://github.com/samet-g/mobese", frame)
                key = cv2.waitKey(1) & 0xFF
                
                if key == ord("q"):
                    break
        finally:
            cap.release()
            #result.release()
            cv2.destroyAllWindows()
    except cv2.error:
        print(f"{red}[ - ]{bos} Modül kaynaklı bir hata oluştu.\n{red}[ - ]{bos} Farklı bir kamerayı açmayı deneyin.\n{red}[ - ]{bos} Sorun devam ederse >> https://github.com/samet-g/mobese\n{red}[ - ]{bos} Güncellemeleri kontrol edin.")
        
if __name__ == '__main__':
    mobese_track(yolo_races, mobese, 0.6, 0.1, labels,frame_width)