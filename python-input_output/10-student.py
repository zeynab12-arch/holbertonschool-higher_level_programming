class Student:
	def __init__(self, first_name, last_name, age):
	self.first_name = first_name
	self.last_name = last_name
	self.age = age
	def to json(self,atrs) 
	obj_dict = self.__dict__

        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {key: obj_dict[key] for key in attrs if key in obj_dict}

        return obj_dict
