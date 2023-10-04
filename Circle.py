import cv2
import numpy as np

# อ่านภาพจากไฟล์
image = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)

# ค้นหาวงกลมที่เหมาะสม
circles = cv2.HoughCircles(
    image,
    cv2.HOUGH_GRADIENT,
    dp=1,  # ความละเอียดของการหาวงกลม (1 = ความละเอียดสูง)
    minDist=20,  # ระยะห่างระหว่างวงกลมที่ต่างกัน
    param1=50,  # ความสามารถในการตรวจจับของวงกลม
    param2=30,  # ค่าสูงสุดของระยะทางระหว่างจุดศูนย์กลางวงกลมและเส้นของขอบวงกลม
    minRadius=0,  # ขนาดของวงกลมขั้นต่ำ
    maxRadius=0   # ขนาดของวงกลมสูงสุด
)

# หากพบวงกลม
if circles is not None:
    circles = np.uint16(np.around(circles))
    
    for circle in circles[0, :]:
        center = (circle[0], circle[1])
        radius = circle[2]
        
        # วาดวงกลมบนภาพ
        cv2.circle(image, center, radius, (0, 0, 255), 2)

    # แสดงผลลัพธ์
    cv2.imshow('Detected Circles', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No circles found in the image.")