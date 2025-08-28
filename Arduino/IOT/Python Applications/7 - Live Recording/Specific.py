def Recording():
    import numpy as np
    import cv2
    import time
# Define the duration (in seconds) of the video capture here
    capture_duration = 10

    cap1 = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out1 = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

    start_time = time.time()
    while( int(time.time() - start_time) < capture_duration ):
        ret, frame = cap1.read()
        if ret==True:
            frame = cv2.flip(frame,90)

            # write the flipped frame
            out1.write(frame)

            cv2.imshow('frame',frame)
            #if cv2.waitKey(1) & 0xFF == ord('q'):
            #    break
        else:
            break

# Release everything if job is finished
    cap1.release()
    out1.release()
    cv2.destroyAllWindows()


