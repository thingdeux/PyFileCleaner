from manage.log import log

class File:
    path = None
    filename = None
    extension = None

    def __init__(self, path):
        self.path = path

        # Might only work on Unix filesystems
        # Account for windows with \\ potentially
        self.filename = path.split('/')[-1:][0]
        self.extension = self.filename.split('.')[-1:][0]

    def get_size(self):
        pass

    def move(self):
        pass

    def copy(self, destination):
        pass

    def has_extension(self, extension):
        if self.extension is not None:
            if self.extension == extension:
                return True
            return False
        else:
            log("Error: File does not have an extension: {}".format(self.filename or self.path))
            raise ValueError

    def has_filter_in_name(self, filter_name):
        if self.filename is not None:
            if filter_name in self.filename:
                return True
            return False
        else:
            log("Error: File does not have a name: {}".format(self.path))
            raise ValueError