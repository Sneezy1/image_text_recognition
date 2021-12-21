import pandas as pd
import keras_ocr

ocr_model = keras_ocr.pipeline.Pipeline()

def make_recognition(image_path):
	image = keras_ocr.tools.read(image_path)
	prediction_groups = ocr_model.recognize([image])
	strings_list = []
	for i in prediction_groups:
		for y in i:
			strings_list.append(y[0])
	result = ' '.join([item for item in strings_list])
	
	return result
