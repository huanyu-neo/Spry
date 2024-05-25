class ResourceResolver:
    def __init__(self, base_path):
        self.base_path = base_path

    def resolve(self, resource_name):
        try:
            with open(f"{self.base_path}/{resource_name}", "r") as file:
                return file.read()
        except FileNotFoundError:
            return None