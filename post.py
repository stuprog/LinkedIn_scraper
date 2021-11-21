class Post:
    def __init__(self):
        pass

    def set_values(self, owner, time, content, views, interaction, type_of_content, text_content):
        self.owner = owner
        self.time = time
        self.content = content
        self.views = views
        self.interaction = interaction
        self.type_of_content = type_of_content
        self.text_content = text_content

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
