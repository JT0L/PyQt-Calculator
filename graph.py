import matplotlib.pyplot as plt


class Graph:
    def __init__(self, functions):
        self.functions = functions
        self.__x_min = -10
        self.__x_max = 10
        self.__y_min = -4
        self.__y_max = 20
        self.__step = 0.0001

    def set_x_range(self, min, max):
        self.__x_min = min
        self.__x_max = max

    def set_y_range(self, min, max):
        self.__y_min = min
        self.__y_max = max

    def set_step(self, step):
        self.__step = step

    def evaluate_functions(self):
        for func in self.functions.list_of_functions:
            func.set_x_range(self.__x_min, self.__x_max)
            func.set_step(self.__step)
            func.evaluate()

    def add_functions_to_plot(self):
        for func in self.functions.list_of_functions:
            plt.plot(func.x, func.y, label=func.formula())

    @staticmethod
    def set_labels():
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Plot of all the functions')

    def set_axes(self):
        axes = plt.gca()
        axes.set_xlim([self.__x_min, self.__x_max])
        axes.set_ylim([self.__y_min, self.__y_max])

    @staticmethod
    def set_layout():
        plt.tight_layout()

    def add_legend(self):
        legend_list = []
        for func in self.functions.list_of_functions:
            legend_list.append(func.formula() + ', roots: ' + str(func.calc_roots()))

        plt.legend(legend_list)

    @staticmethod
    def show_plot():
        plt.show()

    def plot(self):
        self.evaluate_functions()
        self.add_functions_to_plot()
        self.set_labels()
        self.set_axes()
        self.set_layout()
        self.add_legend()
        self.show_plot()