class Profile:
    """ The Profile class """

    def __init__(self, full_name, date_of_birth, occupation):
        """ Initial the instance with the full name, date of birth: str, and occupation """
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.occupation = occupation

    def get_user_profile(self):
        """ returns a dict of the user profile in full_name, date_of_birth and occupation order """
        return {
            "full_name": self.full_name,
            "date_of_birth": self.date_of_birth,
            "occupation": self.occupation
        }

    def clear_user_profile(self):
        """ unsets all the parameters to empty strings and returns 1 on success """
        self.full_name = ''
        self.date_of_birth = ''
        self.occupation = ''
        return 1

    def get_full_name(self):
        """ returns the full_name """
        return self.full_name

    def set_full_name(self, full_name):
        """ sets the full_name """
        self.full_name = full_name

    def get_date_of_birth(self):
        """ returns the date_of_birth """
        return self.date_of_birth

    def set_date_of_birth(self, date_of_birth):
        """ sets the date_of_birth """
        self.date_of_birth = date_of_birth

    def get_occupation(self):
        """ gets the occupation """
        return self.occupation

    def set_occupation(self, occupation):
        """ sets the occupationI """
        self.occupation = occupation


if __name__ == "__main__":
    import sys

    full_name = sys.argv[1]
    date_of_birth = sys.argv[2]
    occupation = sys.argv[3]

    print(Profile(full_name, date_of_birth, occupation).get_user_profile())
