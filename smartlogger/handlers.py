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
            dir_name = os.path.dirname(self.filename)
            if dir_name:
                os.makedirs(dir_name, exist_ok=True)
            with open(self.filename, "a", encoding="utf-8"):
                pass

        def emit(self, message):
            dir_name = os.path.dirname(self.filename)
            if dir_name:
                os.makedirs(dir_name, exist_ok=True)
                
            if os.path.exists(self.filename):
                if os.path.getsize(self.filename) > self.max_size:
                    backup = self.filename + ".1"
                    if os.path.exists(backup):
                        os.remove(backup)
                    os.rename(self.filename, backup)

            with open(self.filename, "a", encoding="utf-8") as f:
                f.write(message + "\n")