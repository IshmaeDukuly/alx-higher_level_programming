#!/usr/python3
"""

Contains class student
this initialize public instance attributes first_name, last_name, and age, and also, has public metod to_json that returns dictionary representation
"""


class Student():
    """
    Publice Atrributes:
    first_name
    last_name
    age

    public Methods:
        to_json: Retrieves its dictionary representation
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes student with a full name and age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self, attrs=None):
            """
            Returns:
                to dictionary description width simple data structure
                (list, dictionary, dictionay, string)
                for JSON serialisation of object

            Return:
                Only return the ict of attrs given
                Return the entire dict if not atrrs is given
            """

            if attrs is None:
                return self.__dict__
            else:
                dic = {}
                for att in attrs:
                    if att in self.__dict__.keys():
                        dict[att] = self.__dict__[att]
                return dic
