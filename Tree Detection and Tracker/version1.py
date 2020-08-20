import cv2 as cv
import numpy as np
import time

cap = cv.VideoCapture("test.MOV")
ret, frame1 = cap.read()
frame1 = cv.resize(frame1,(640,480),fx=0,fy=0, interpolation = cv.INTER_CUBIC)
prvs = cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255

pcounter = 0

time.sleep(1)

f=0
while(1):
    ret, frame2 = cap.read()
    frame2 = cv.resize(frame2,(640,480),fx=0,fy=0, interpolation = cv.INTER_CUBIC)
    if ret == False:
        break
    
     # Set trackbars
 
    
    next = cv.cvtColor(frame2,cv.COLOR_BGR2GRAY)
    f+=1
    if(f%1!=0):
         continue
    flow = cv.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 20, 3, 5, 1.2, 0)
    mag, ang = cv.cartToPolar(flow[...,0], flow[...,1])
    
    hsv[...,0] = 0
    hsv[...,2] = cv.normalize(mag,None,0,255,cv.NORM_MINMAX)
    bgr = cv.cvtColor(hsv,cv.COLOR_BGR2GRAY)
    bgrMean = bgr.mean()
    rgb_filtered = cv.inRange(bgr, bgrMean, 255)
    cutten = cv.bitwise_and(frame2, frame2, mask = rgb_filtered)
    
   
    
    lowerRange = np.array([24, 65, 61])
    upperRange = np.array([41, 255, 255])
    
    lower_white = np.array([0, 0, 212])
    upper_white = np.array([131, 255, 255])
    whiteMask = cv.inRange(cutten,lower_white, upper_white)
    
    
    greenMask = cv.inRange(cutten, lowerRange, upperRange)
    mask = (whiteMask | greenMask)
    result = cv.bitwise_and(frame2,frame2, mask=mask)
   
    # rate of optical and Hsv threshold 
    #print(np.count_nonzero(cutten>0),"\t",np.count_nonzero(result>0),"\t",np.count_nonzero(result>0)/np.count_nonzero(cutten>0))
    
    if (np.count_nonzero(result>0)/np.count_nonzero(cutten>0)) < 0.01:
        lastMask_Green = cv.inRange(frame2, lowerRange, upperRange)
        lastMask_White = cv.inRange(frame2, lower_white, upper_white)
        lastMask = (lastMask_Green | lastMask_White)
        kernel = np.ones((10,10), 'uint8')
        lastMask = cv.GaussianBlur(lastMask,(9,9),25)
        lastMask = cv.dilate(lastMask, kernel)
        lastResult = cv.bitwise_and(frame2,frame2, mask=lastMask)
        
    else:
        lastMask_Green = cv.inRange(cutten, lowerRange, upperRange)
        lastMask_White = cv.inRange(cutten, lower_white, upper_white)
        lastMask = (lastMask_Green | lastMask_White)
        kernel = np.ones((5,5), 'uint8')
        lastMask = cv.GaussianBlur(lastMask,(15,15),50)
        lastMask = cv.dilate(lastMask, kernel)
        lastResult = cv.bitwise_and(frame2,frame2, mask=lastMask)
    
    (_,contours,hierarchy) = cv.findContours(lastMask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    trees = np.zeros((0,4))

    for pic, contour in enumerate(contours):
        area = cv.contourArea(contour)
        
        if(area >1000):
            x,y,w,h = cv.boundingRect(contour)
            frame2 = cv.rectangle(frame2, (x,y), (x+w,y+h),(0,0,255),2)
            trees = np.vstack([trees, [x,y,w,h]])      # data of detected tree  for space detection 
            cv.putText(frame2, 'Tree', (x,y), cv.FONT_HERSHEY_SIMPLEX,0.7, (0,0,255))
            
        
    print("***************************")
    if len(trees)!=0:
        #print("|||||||||||||||||||||||||||||||||||||||||||||")
        meanOfHeihgt = trees[:,3].mean()
        #print(trees)
        sorted_trees = trees[np.argsort(trees[:,1])]
        #print("-------------------------------------------")
        #print(sorted_trees)
        for tree in sorted_trees:
            sameLine = sorted_trees[ ((sorted_trees[:,2]<=tree[2]) & ((sorted_trees[:,0]+(sorted_trees[:,2]/2))>tree[0]) & ((sorted_trees[:,0]+(sorted_trees[:,2]/2))<(tree[0]+tree[2]))) | ((sorted_trees[:,2]>tree[2]) & ((sorted_trees[:,0] < (tree[0]+(tree[2]/2)))) & (((sorted_trees[:,0]+sorted_trees[:,2]) > (tree[0]+(tree[2]/2)))))]
            #sameLine = sameLine[np.argsort(sameLine[:,])] Büşra için
            
            ##print(sameLine[np.where(sameLine == tree)])
            #print("Tree",tree)
            #print(sameLine)
            
            if len(sameLine[sameLine[:,1]>tree[1]])>1:
                nextTree = sameLine[sameLine[:,1]>tree[1]][0]
                nextTree = nextTree.astype(np.int64)
                tree = tree.astype(np.int64)
                if nextTree[1]-(tree[1]+tree[3]) > (meanOfHeihgt*1.5):
                    frame2 = cv.rectangle(frame2, (tree[0],(tree[1]+tree[3])), ((nextTree[0]+nextTree[2]),nextTree[1]),(0,0,15),2)
                    print("Space")
            if len(sameLine[sameLine[:,1] < tree[1]])==0:
                tree = tree.astype(np.int64)
                if tree[1]> (meanOfHeihgt*1.5):
                    frame2 = cv.rectangle(frame2, (tree[0],0), ((tree[0]+tree[2]),tree[1]),(0,0,15),2)
           
            
    cv.imshow('frame2',lastResult)
    cv.imshow('frame',frame2)
    cv.imshow('framefilt',rgb_filtered)
    cv.imshow('framecutten',cutten)
    cv.imshow('result',result)
        
    k = cv.waitKey(30) & 0xff
    if k == 27:
         break
    elif k == ord('s'):
         cv.imwrite('rapor/space{}.png'.format(pcounter),frame2)
         cv.imwrite('rapor/optical{}.png'.format(pcounter),cutten)
         pcounter +=1
    
  
    prvs = next
   
cap.release()
cv.destroyAllWindows()