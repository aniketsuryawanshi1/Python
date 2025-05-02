class Doctor:
	def __init__(self, **kwargs):
		self.__allowed_fields = [
		'email', 'name', 'email', 'gender', 'phone_no', 'qualification', 'experience', 'department', 'role'
		]

		for key in self.__allowed_fields:
			setattr(self,f"__{key}", kwargs.get(key))

	def get_field(self, fields_name):
		if fields_name in self.__allowed_fields:
			return getattr(self, f"__{fields_name}")
		else:
			raise AttributeError(f"'{fields_name}' is not valid field.")

	def get_info(self):
		""" Return a dictionary of all private fields. """
		return {key:self.get_field(key) for key in self.__allowed_fields}

