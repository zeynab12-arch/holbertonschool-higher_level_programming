class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        student_dict = self.__dict__

        if isinstance(attrs, list):
            new_dict = {}
            for key in attrs:
                if key in student_dict:
                    new_dict[key] = student_dict[key]
            return new_dict

        return student_dict
