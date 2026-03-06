import os
class ConsoleHandler:

    def emit(self, message):
        print(message)
class FileHandler:

        # def __init__(self, filename):
        #     self.filename = filename
        # def emit(self, message):
        #     with open(self.filename, "a") as f:
        #         f.write(message + "\n")
        def __init__(self, filename, max_size=5000):
            self.filename = filename
            self.max_size = max_size

        def emit(self, message):
            if os.path.exists(self.filename):
                if os.path.getsize(self.filename) > self.max_size:
                    backup = self.filename + ".1"
                    if os.path.exists(backup):
                        os.remove(backup)
                    os.rename(self.filename, backup)

            with open(self.filename, "a") as f:
                f.write(message + "\n")