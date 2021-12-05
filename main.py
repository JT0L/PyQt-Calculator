import sys
from abc import abstractmethod

from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

import functions
import list_of_functions_object
import graph

list_of_functions = list_of_functions_object.Functions()
graph_of_functions = graph.Graph(list_of_functions)


FROM_LEFT = 600
FROM_TOP = 200

WINDOW_X = 600
WINDOW_Y = 600

NUMBER_OF_BUTTONS = 5


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.button_lenght = int(WINDOW_X / 2.5)
        self.button_height = int(WINDOW_Y / 10)
        self.button_from_left = int((WINDOW_X - self.button_lenght) / 2)
        self.setupUi()

    @pyqtSlot()
    def add_function_button_1_clicked(self):
        self.cams = AddFunctionWindow()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def remove_function_button_2_clicked(self):
        self.cams = RemoveFunctionWindow()
        self.cams.show()
        self.close()

    def display_graph_button_3_clicked(self):
        graph_of_functions.plot()
        graph_of_functions.show_plot()

    @pyqtSlot()
    def set_graph_parameters_button_4_clicked(self):
        self.cams = SetParametersWindow()
        self.cams.show()
        self.close()

    @staticmethod
    def quit_button_5_clicked():
        quit()

    def calculate_button_y_position(self, button_number):
        distance_between_buttons = (WINDOW_Y - NUMBER_OF_BUTTONS * self.button_height) // (NUMBER_OF_BUTTONS + 1)
        return int((button_number - 1) * self.button_height + button_number * distance_between_buttons)

    def setupUi(self):
        self.setGeometry(FROM_LEFT, FROM_TOP, WINDOW_X, WINDOW_Y)
        self.setWindowTitle('Graphing calculator')

        self.add_function_button_1 = QPushButton(self)
        self.add_function_button_1.setText('Add function')
        self.add_function_button_1.clicked.connect(self.add_function_button_1_clicked)
        self.add_function_button_1.setGeometry(self.button_from_left, self.calculate_button_y_position(1), self.button_lenght, self.button_height)

        self.remove_function_button_2 = QPushButton(self)
        self.remove_function_button_2.setText('Remove function')
        self.remove_function_button_2.clicked.connect(self.remove_function_button_2_clicked)
        self.remove_function_button_2.setGeometry(self.button_from_left, self.calculate_button_y_position(2), self.button_lenght, self.button_height)

        self.display_graph_button_3 = QPushButton(self)
        self.display_graph_button_3.setText('Show graph')
        self.display_graph_button_3.clicked.connect(self.display_graph_button_3_clicked)
        self.display_graph_button_3.setGeometry(self.button_from_left, self.calculate_button_y_position(3), self.button_lenght, self.button_height)

        self.set_graph_parameters_button_4 = QPushButton(self)
        self.set_graph_parameters_button_4.setText('Set graph parameters')
        self.set_graph_parameters_button_4.clicked.connect(self.set_graph_parameters_button_4_clicked)
        self.set_graph_parameters_button_4.setGeometry(self.button_from_left, self.calculate_button_y_position(4), self.button_lenght, self.button_height)

        self.quit_button_5 = QPushButton(self)
        self.quit_button_5.setText('Quit')
        self.quit_button_5.clicked.connect(self.quit_button_5_clicked)
        self.quit_button_5.setGeometry(self.button_from_left, self.calculate_button_y_position(5), self.button_lenght, self.button_height)

#------------------------------------------------------------

class SubWindow(QDialog):
    def __init__(self):
        super(SubWindow, self).__init__()
        self.setupUi()

    @abstractmethod
    def setupUi(self):
        self.setGeometry(250, 250, 700, 700)
        self.setWindowTitle('SubWindow')

    @staticmethod
    def getInput(text):
        if text == '':
            return 0
        return float(text)

    def showListOfFunction(self):
        self.list_of_functions_label.setText(graph_of_functions.functions.prepare_html())

    def returnToMainWindow(self):
        self.cams = MainWindow()
        self.cams.show()
        self.close()


#------------------------------------------------------------

class AddFunctionWindow(SubWindow):
    def __init__(self):
        super(AddFunctionWindow, self).__init__()
        self.setupUi()
        self.showListOfFunction()

    def setupUi(self):
        font = QFont()
        font.setPointSize(15)

        self.setGeometry(300, 300, 700, WINDOW_Y)
        self.setWindowTitle('Add function')

        self.add_function_button = QPushButton(self)
        self.add_function_button.setText('Add this function')
        self.add_function_button.clicked.connect(self.addFunction)
        self.add_function_button.setGeometry(10, 10, 250, 50)

        self.return_button = QPushButton(self)
        self.return_button.setText('Return')
        self.return_button.clicked.connect(self.returnToMainWindow)
        self.return_button.setGeometry(10, 80, 250, 50)

        self.a_label = QLabel(self)
        self.a_label.setText('a value:')
        self.a_label.setGeometry(300, 10, 80, 50)

        self.b_label = QLabel(self)
        self.b_label.setText('b value:')
        self.b_label.setGeometry(420, 10, 80, 50)

        self.c_label = QLabel(self)
        self.c_label.setText('c value:')
        self.c_label.setGeometry(540, 10, 80, 50)

        self.a_input = QLineEdit(self)
        self.a_input.setFont(font)
        self.a_input.setGeometry(300, 80, 100, 50)

        self.b_input = QLineEdit(self)
        self.b_input.setFont(font)
        self.b_input.setGeometry(420, 80, 100, 50)

        self.c_input = QLineEdit(self)
        self.c_input.setFont(font)
        self.c_input.setGeometry(540, 80, 100, 50)

        self.list_of_functions_label = QLabel(self)
        self.list_of_functions_label.setGeometry(200, 135, 400, 500)

    def addFunction(self):
        a = self.getInput(self.a_input.text())
        b = self.getInput(self.b_input.text())
        c = self.getInput(self.c_input.text())

        if a:
            list_of_functions.add_function(functions.Quadratic.create_function(a=a, b=b, c=c))
        else:
            if b:
                list_of_functions.add_function(functions.Linear.create_function(a=b, b=c))
            else:
                list_of_functions.add_function(functions.Constant.create_function(a=c))

        self.showListOfFunction()

#------------------------------------------------------------


class RemoveFunctionWindow(SubWindow):
    def __init__(self):
        super(RemoveFunctionWindow, self).__init__()
        self.setupUi()
        self.showListOfFunction()

    def setupUi(self):
        font = QFont()
        font.setPointSize(15)

        self.setGeometry(FROM_LEFT, FROM_TOP, WINDOW_X, WINDOW_Y)
        self.setWindowTitle('Remove function')

        self.remove_function_button = QPushButton(self)
        self.remove_function_button.setText('Remove this function')
        self.remove_function_button.clicked.connect(self.rmFunction)
        self.remove_function_button.setGeometry(30, 10, 250, 60)

        self.return_button = QPushButton(self)
        self.return_button.setText('Return')
        self.return_button.clicked.connect(self.returnToMainWindow)
        self.return_button.setGeometry(30, 80, 250, 60)

        self.label_for_input = QLabel(self)
        self.label_for_input.setText('<p style="font-size:12px"> Enter number of function you want to remove <\p>')
        self.label_for_input.setGeometry(300, 20, 800, 50)

        self.index_to_remove = QLineEdit(self)
        self.index_to_remove.setFont(font)
        self.index_to_remove.setGeometry(400, 75, 60, 60)

        self.list_of_functions_label = QLabel(self)
        self.list_of_functions_label.setGeometry(180, 135, 400, 500)

    def rmFunction(self):
        index = int(self.getInput(self.index_to_remove.text()))
        if index != 0:
            list_of_functions.remove_function_by_index(index-1)
        self.showListOfFunction()


#------------------------------------------------------------

class SetParametersWindow(SubWindow):
    def __init__(self):
        super(SetParametersWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(300, 300, 900, 150)
        self.setWindowTitle('Set parameters')

        self.change_button = QPushButton(self)
        self.change_button.setText('Change for this')
        self.change_button.clicked.connect(self.RmFunction)
        self.change_button.setGeometry(10, 10, 250, 50)

        self.return_button = QPushButton(self)
        self.return_button.setText('Return')
        self.return_button.clicked.connect(self.returnToMainWindow)
        self.return_button.setGeometry(10, 80, 250, 50)

        font = QFont()
        font.setPointSize(15)

        self.label = QLabel(self)
        self.label.setText('x_min')
        self.label.setGeometry(335, 10, 80, 50)

        self.label = QLabel(self)
        self.label.setText('x_max')
        self.label.setGeometry(455, 10, 80, 50)

        self.label = QLabel(self)
        self.label.setText('y_min')
        self.label.setGeometry(575, 10, 80, 50)

        self.label = QLabel(self)
        self.label.setText('y_max')
        self.label.setGeometry(690, 10, 80, 50)

        self.label = QLabel(self)
        self.label.setText('step')
        self.label.setGeometry(815, 10, 80, 50)

        self.xi_input = QLineEdit(self)
        self.xi_input.setFont(font)
        self.xi_input.setGeometry(300, 80, 100, 50)

        self.xa_input = QLineEdit(self)
        self.xa_input.setFont(font)
        self.xa_input.setGeometry(420, 80, 100, 50)

        self.yi_input = QLineEdit(self)
        self.yi_input.setFont(font)
        self.yi_input.setGeometry(540, 80, 100, 50)

        self.ya_input = QLineEdit(self)
        self.ya_input.setFont(font)
        self.ya_input.setGeometry(660, 80, 100, 50)

        self.s_input = QLineEdit(self)
        self.s_input.setFont(font)
        self.s_input.setGeometry(780, 80, 100, 50)


    def RmFunction(self):
        x_min = float(self.xi_input.text())
        x_max = float(self.xa_input.text())
        y_min = float(self.yi_input.text())
        y_max = float(self.ya_input.text())
        step = float(self.s_input.text())
        graph_of_functions.set_x_range(x_min, x_max)
        graph_of_functions.set_y_range(y_min, y_max)
        graph_of_functions.set_step(step)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()