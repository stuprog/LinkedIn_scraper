class User:
    def __init__(self):
        pass

    def set_values(self, name, title, position, connections, exp, emp_duration, company_name, location, profile_views,profile_url):
        self.exp = exp
        self.name = name
        self.title = title
        self.position = position
        self.connections = connections
        self.emp_duration = emp_duration
        self.company_name = company_name
        self.location = location
        self.profile_views = profile_views
        self.profile_url= profile_url

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
