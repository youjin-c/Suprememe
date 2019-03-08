from PIL import Image, ImageFilter, ImageDraw, ImageFont
from imageai.Detection import ObjectDetection
import os, random
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'# Just disables the warning, doesn't enable AVX/FMA
import time
from glob import glob
import subprocess
from datetime import datetime


def boxlogo(): 
	now = datetime.now()
	isTshirt = False 
	isBoxLogo = False
	files = []
	for file in glob('img/*.jpg'):
		files.append(file)
	# industrialObject=random.choice(files)
	industrialObject = max(files, key=os.path.getctime)
	# show_img = Image.open(industrialObject)
	# show_img.show()

	tshrits = []
	for file in glob('tshirts/*.jpg'):
		tshrits.append(file)
	# Tshirt=random.choice(tshrits)
	Tshirt = max(tshrits, key=os.path.getctime)
	# show_img = Image.open(Tshirt)
	# show_img.show()

	prints = []
	for printimg in glob('insta/*.jpg'):
		prints.append(printimg)
	# selPrint = random.choice(prints)
	selPrint = max(prints, key=os.path.getctime)
	# print(selPrint)
	# show_img = Image.open(selPrint)
	# show_img.show()
	
	execution_path = os.getcwd()
	detector = ObjectDetection()
	detector.setModelTypeAsRetinaNet()
	detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
	detector.loadModel()
	detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , industrialObject), output_image_path=os.path.join(execution_path , "imagenew.jpg"))
	#detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , industrialObject))
	show_img = Image.open("imagenew.jpg")
	show_img.show()

	if int(len(detections)):
		baby = Image.open(industrialObject)
		chosenObject=random.choice(detections)
		isTshirt = False
		isBoxLogo = True
		
		
	else:
		# detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , Tshirt))
		detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , Tshirt), output_image_path=os.path.join(execution_path , "imagenew.jpg"))
		show_img = Image.open("imagenew.jpg")
		show_img.show()
		chosenObject=random.choice(detections)
		baby = Image.open(Tshirt)
		isTshirt = True
		if(random.randint(0,1)):
			isBoxLogo = True
		

	# print("chosen",chosenObject["name"]," : ", chosenObject["box_points"])
	objectX,objectY,objectW,objectH=(chosenObject["box_points"][0],chosenObject["box_points"][1],chosenObject["box_points"][2]-chosenObject["box_points"][0],chosenObject["box_points"][3]-chosenObject["box_points"][1])

	if not isTshirt:
		before  = baby.size
		degree = random.randint(-45,45) #rotation degree
		baby=baby.rotate(degree, expand=1)
		after = baby.size
		baby.show()
		# print('size difference : ', after[0]-before[0]," , " ,after[1]-before[1])
		x = objectX+random.uniform(objectW*0.05,objectW*0.15)+after[0]-before[0]
		y = objectY+random.uniform(objectH*0.15,objectH*0.25)+after[1]-before[1]
		f = int(random.uniform(objectW*0.1,objectW*0.15))
	else: #Put the Box Logo or a square Img
		f = int(random.uniform(objectW*0.02,objectW*0.15))
		x = objectX+random.uniform(objectW*13/f,objectW*17/f)
		y = objectY+random.uniform(objectH*18/f,objectH*23/f)
	print(x-objectX,y-objectY,f)
	
	if isBoxLogo:
		print("IS BOX LOGO")
		canvas = ImageDraw.Draw(baby)
		# canvas.rectangle([objectX,objectY,objectW,objectH],outline=(255,255,255))
		canvas.rectangle([x,y,x+5*f,y+1.4*f], fill = (random.randint(0,1)*255,0,0))
		font = ImageFont.truetype('/Library/Fonts/Futura Std Heavy Oblique',f)
		canvas.text((x+0.5*f,y+f/6),"Supreme", font=font, fill=(255,255,255))
	else:
		print("IS PRINT")
		x =-1*(objectX+random.uniform(objectW*0.2,objectW*0.4))
		y =-1*(objectY+random.uniform(objectH*0.3,objectH*0.35))
		size = int(random.uniform(objectW*0.3,objectW*0.4))
		print("x,y,",x,y,"SIZE :",size)
		subprocess.call(['magick',selPrint,'-resize',str(size)+'x'+str(size),selPrint])
		if(random.randint(0,1)):
			subprocess.call(['convert', selPrint, '-colorspace', 'Gray', selPrint])
		
		temp = 'upload/'+'print'+'.jpg' 
		subprocess.call(['composite','-compose', 'atop', '-geometry', 
			'-'+str(x)+'-'+str(y),
			selPrint,
			Tshirt,
			temp])
		baby = Image.open(temp)
		baby.show()
		# os.remove(temp)

	if not isTshirt:
		baby=baby.rotate(360-degree, expand=1)
		baby.show()
	if random.randint(0,1):
		# map the inputs to the function blocks
		options = {0 : GaussianBlur,
				1 : BoxBlur,
				2 : UnsharpMask,
				3 : MinFilter,
				4 : MaxFilter,
				5 : ModeFilter,
				6 : MedianFilter
		}
		optionSel= random.randint(0,6)
		baby = options[optionSel](baby)
		baby.show()
		return baby.save('upload/'+now.strftime("%m%d%Y_%H%M%S")+chosenObject["name"]+str(optionSel)+'.jpg')

	# os.remove(industrialObject)
	# os.remove(Tshirt)
	# os.remove(selPrint)
	baby.show()
	return baby.save('upload/'+now.strftime("%m%d%Y_%H%M%S")+chosenObject["name"]+'.jpg')

# define the function blocks
def GaussianBlur(img):
    return img.filter(ImageFilter.GaussianBlur(random.randint(0,2)))

def BoxBlur(img):
    return img.filter(ImageFilter.BoxBlur(random.randint(0,9)))

def UnsharpMask(img):
    return img.filter(ImageFilter.UnsharpMask(random.randint(0,2), random.randint(80,250), random.randint(0,5)))#random.randint(0,9)))

def MinFilter(img):
    return img.filter(ImageFilter.MinFilter(random.randrange(3,5,2)))

def MaxFilter(img):
    return img.filter(ImageFilter.MaxFilter(random.randrange(3,5,2)))

def ModeFilter(img):
    return img.filter(ImageFilter.ModeFilter(random.randrange(3,5,2)))

def MedianFilter(img):
    return img.filter(ImageFilter.MedianFilter(random.randrange(3,5,2)))


boxlogo()