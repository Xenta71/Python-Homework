class User:
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name

    def say_fname(self):
        return(self.fname)

    def say_lname(self):
        return(self.lname)

    def get_name_info(self):
        return(f"{self.fname} {self.lname}")