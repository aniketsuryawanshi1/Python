class Patient:
    def __init__(self, **kwargs):
        self.__allowed_fields = [
        'email', 'name', 'gender', 'phone_no', 'age', 'address', 'insurance', 'medical_history', 'doc_name', 'role'
        ]
        for key in self.__allowed_fields:
            setattr(self, f"__{key}", kwargs.get(key)) # Use name mangling for encapsulation.

    def get_fields(self, field_name):
        """ Universal gatter for any private field. """
        if field_name in self.__allowed_fields:
            return getattr(self, f"__{field_name}")
        else:
            raise AttributeError(f"'{field_name}' is not a valid field." )

    def get_info(self):
        """ Return a directionary of all private fields. """
        return {key: self.get_fields(key) for key in self.__allowed_fields}

