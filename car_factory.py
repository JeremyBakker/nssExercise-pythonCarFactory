import sys

makes = list()
models = list()

class Car_Factory():

	def read_car_makes():
		'''Reads the car-makes.log file'''
		with open('car_makes.log', 'r') as car_makes:
			for make in car_makes:
				make = make.replace('\n', '')
				makes.append(make)

	def read_car_models():
		'''Reads the car-models.log file'''
		with open('car_models.log', 'r') as car_models:
			for model in car_models:
				model = model.replace('\n', '')
				models.append(model)

	def create_car_dictionary():
		'''Creates a dictionary with data from the car-makes and car-models files'''
		Car_Factory.read_car_makes()
		Car_Factory.read_car_models()
		car_dictionary=dict()
		for make in makes:
			car_dictionary[make] = list()
			for model in models:
				if make[0] == model[0]:
					car_dictionary[make].append(model[2:])
		print(car_dictionary)

if __name__ == '__main__':
	Car_Factory.create_car_dictionary()
	


