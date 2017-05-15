import picamera

def createData(movement,index=0):
    
    camera = picamera.PiCamera()
    camera.resolution = (128, 128)

    try:
        index = str(index)
        if movement[0] == 1:
            y_label = 'links'
        elif movement[1] == 1:
            y_label = 'vorne'
        elif movement[2] == 1:
            y_label = 'rechts'
        f = open('/Desktop/Self-Driving-Car/TrainingData/mydataset.txt','a')
        f.write('/Desktop/Self-Driving-Car/TrainingData/img{}.jpeg {}\n'.format(index,y_label))
        camera.capture('/Desktop/Self-Driving-Car/TrainingData/img{}.jpeg'.format(index),format='jpeg')
    finally:
        camera.close()
