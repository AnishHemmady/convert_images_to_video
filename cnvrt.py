import cv2
import os
#print(cv2.getBuildInformation())


cv2.namedWindow("camCapture", cv2.WINDOW_AUTOSIZE)
cap = cv2.VideoCapture()
video_stream="stream_link_here"

if not cap.open(video_stream):
    print ("Not open")
cnt=1
while (True):
	err,img = cap.read()
	#print(img.shape)
	ans="{}.png".format(cnt)
	cv2.imwrite("images/"+ans,img)
	#new_img=cv2.imread("img1.jpg",1)
	#cv2.imshow("camCapture",new_img)
	cnt+=1
	
		
		
def convert_to_video():
	images=[]
	
	dir_path="images/"
	for f in os.listdir(dir_path):
		if f.endswith(".png"):
			images.append(f)
	new_img_loctn=[None]*len(images)
	print(len(images))
	for i in images:
		k=i.split('.')
		k1=int(k[0])
		new_img_loctn[k1-1]=i
	img_path=os.path.join(dir_path,new_img_loctn[0])
	frame=cv2.imread(img_path)
	#cv2.imshow('video',frame)
	height, width, channels = frame.shape
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	print(new_img_loctn)
	out = cv2.VideoWriter("output.avi", fourcc, 30.0, (width, height))
	for image in new_img_loctn:

		image_path = os.path.join(dir_path, image)
		frame = cv2.imread(image_path)
		#print(image_path)
		out.write(frame) # Write out frame to video

		cv2.imshow('video',frame)
		if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
			break

	# Release everything if job is finished
	out.release()
	cv2.destroyAllWindows()
	
convert_to_video()
		
