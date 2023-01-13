"""

    ===Buferless video cpature===
    made by Pietras125 from:
    -https://stackoverflow.com/a/54755738/20133132
    -https://www.learningaboutelectronics.com/Articles/How-to-record-video-Python-OpenCV.php

    Example of use:
    ##########################################
    import this_class
    import threading

    if __name__ == "__main__":
        #record 5 second video from webcam and close
        cap = VideoCapture(0)
        x = threading.Thread(target=cap.start_recording)
        x.start()
        time.sleep(5)
        cap.stop_recording()
    ##########################################

"""

import cv2
import queue
import threading 
import datetime

class VideoCapture:
    def __init__(self, name):
        self.source_name = str(name)
        self.cap = cv2.VideoCapture(name)
        self.width= int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height= int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))

        self.q = queue.Queue()
        t = threading.Thread(target=self._reader)
        t.daemon = True
        t.start()

    # read frames as soon as they are available, keeping only most recent one
    def _reader(self):
        print(self.current_datetime()+ " Frame reader for source " + self.source_name + " started")
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            if not self.q.empty():
                try:
                    self.q.get_nowait()   # discard previous (unprocessed) frame
                except queue.Empty:
                    pass
            self.q.put(frame)

    def start_recording(self):
        self.output_name = self.source_name + "-" + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".mp4"
        print(self.current_datetime() + " Recording of source " + self.source_name + " started " + self.output_name)
        self.recording = True
        writer = cv2.VideoWriter(self.output_name, cv2.VideoWriter_fourcc(*'mp4v'), self.fps, (self.width,self.height))
        while True:
            frame = self.q.get()
            cv2.putText(frame,self.current_datetime(),(10,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1,2)
            cv2.putText(frame,str(self.fps),(10,200),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1,2)
            cv2.imshow("frame", frame)
            writer.write(frame)
            if self.recording == False:
                break
        self.cap.release()
        print(self.current_datetime()+ " Frame reader for source " + self.source_name + " stopped")
        writer.release()
        print(self.current_datetime()+ " Recording of source " + self.source_name + " stopped")
        cv2.destroyAllWindows()

    def stop_recording(self):
        self.recording = False

    def current_datetime(self):
        current_dt = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")
        return current_dt
    
