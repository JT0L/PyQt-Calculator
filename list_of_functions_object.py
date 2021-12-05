class Functions:
    def __init__(self):
        self.list_of_functions = []

    def check_if_functions_exists(self, function):
        for func in self.list_of_functions:
            if func.type == function.type:
                if func == function:
                    return True
        return False

    def add_function(self, function):
        if not self.check_if_functions_exists(function):
            self.list_of_functions.append(function)

    def remove_function_by_index(self, index):
        if index < len(self.list_of_functions):
            del self.list_of_functions[index]

    def prepare_html(self):
        html = '<ol style="font-size:15px">'
        for f in self.list_of_functions:
            html = html + '<li>' + f.formula() + '</li>'
        html += '</ol>'
        return html
