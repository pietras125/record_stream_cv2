#Buferless video cpature

Made by Pietras125 (me) from:  
-https://stackoverflow.com/a/54755738/20133132  
-https://www.learningaboutelectronics.com/Articles/How-to-record-video-Python-OpenCV.php  
    
Ready to import in your project.    
    
Example of use (paste this into your code):  
'''  
import record_stream_cv2  
import threading  
    
if __name__ == "__main__":  
    #record 5 second video from webcam and close  
    cap = VideoCapture(0)  
    x = threading.Thread(target=cap.start_recording)  
    x.start()  
    time.sleep(5)  
    cap.stop_recording()  
'''