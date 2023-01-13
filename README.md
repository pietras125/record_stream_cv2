#Buferless video cpature

Made by Pietras125 (me) from:  
-https://stackoverflow.com/a/54755738/20133132  
-https://www.learningaboutelectronics.com/Articles/How-to-record-video-Python-OpenCV.php  
    
Ready to import in your project.    
    
Example of use:  
``` 
import record_stream_cv2  
import threading  
import time  
    
if __name__ == "__main__":  
    #record 5 second video from webcam and close  
    cap = VideoCapture(0)  
    x = threading.Thread(target=cap.start_recording)  
    x.start()  
    time.sleep(5)  
    cap.stop_recording()  
```

This will record 5 second video from your webcam. It is about 5 seconds, depending on your camera startup time.
