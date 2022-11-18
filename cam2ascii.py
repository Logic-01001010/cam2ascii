import cv2
import numpy as np
import time

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()

    
    frame = cv2.resize(frame, dsize=(200, 200), interpolation=cv2.INTER_AREA)
    frame = np.array( frame )

    for y in range(frame.shape[0]):
        for x in range(frame.shape[1]):
                # print(f'\033[38;2;{frame[y][x][2]};{frame[y][x][1]};{frame[y][x][0]}mo\033[0m',end='')

                if( frame[y][x][0] <= 50 ):
                    print(f'\033[38;2;{frame[y][x][2]};{frame[y][x][1]};{frame[y][x][0]}m' + '.' + '\033[0m',end='')
                elif( 50 < frame[y][x][0] <= 100 ):
                    print(f'\033[38;2;{frame[y][x][2]};{frame[y][x][1]};{frame[y][x][0]}m' + ',' + '\033[0m',end='')
                elif ( 100 < frame[y][x][0] <= 150 ):
                    print(f'\033[38;2;{frame[y][x][2]};{frame[y][x][1]};{frame[y][x][0]}m' + '&' + '\033[0m',end='')
                elif ( 150 < frame[y][x][0] <= 200 ):
                    print(f'\033[38;2;{frame[y][x][2]};{frame[y][x][1]};{frame[y][x][0]}m' + '%' + '\033[0m',end='')
                elif ( 200 < frame[y][x][0] ):
                    print(f'\033[38;2;{frame[y][x][2]};{frame[y][x][1]};{frame[y][x][0]}m' + '@' + '\033[0m',end='')
        print()
    time.sleep(1)
    input('')
    # cv2.imshow("VideoFrame", frame)    



capture.release()
cv2.destroyAllWindows()