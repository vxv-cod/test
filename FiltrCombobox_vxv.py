'''https://stackoverflow.com/questions/4827207/how-do-i-filter-the-pyqt-qcombobox-items-based-on-the-text-input'''

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtWidgets import QCompleter

# on selection of an item from the completer, select the corresponding item from combobox 
def on_completer_activated(combo, text):
    if text:
        index = combo.findText(text)
        combo.setCurrentIndex(index)
        combo.activated[str].emit(combo.itemText(index))

# on model change, update the models of the filter and completer as well 
def setModel(combo, model):
    # super(ExtendedComboBox, combo).setModel(model)
    combo.pFilterModel.setSourceModel(model)
    combo.completer.setModel(combo.pFilterModel)


# on model column change, update the model column of the filter and completer as well
def setModelColumn(combo, column):
    combo.completer.setCompletionColumn(column)
    combo.pFilterModel.setFilterKeyColumn(column)
    # super(ExtendedComboBox, combo).setModelColumn(column)    


def GO(combo, string_list=None):
    # either fill the standard model of the combobox
    # заполните стандартную модель выпадающего списка
    if string_list != None: combo.addItems(string_list)
    # Настроки
    combo.setFocusPolicy(Qt.StrongFocus)
    combo.setEditable(True)
    # add a filter model to filter matching items
    # добавьте модель фильтра для фильтрации соответствующих элементов
    combo.pFilterModel = QSortFilterProxyModel(combo)
    combo.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
    combo.pFilterModel.setSourceModel(combo.model())
    # add a completer, which uses the filter model
    # добавьте полный, который использует модель фильтра
    combo.completer = QCompleter(combo.pFilterModel, combo)
    # always show all (filtered) completions
    # всегда показывать все (отфильтрованные) завершения
    combo.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
    combo.setCompleter(combo.completer)
    # connect signals
    # сигналы подключения
    combo.lineEdit().textEdited.connect(combo.pFilterModel.setFilterFixedString)
    combo.completer.activated.connect(on_completer_activated)


if __name__ == "__main__":
    from filtrTest_ui import Ui_Form
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    # Определяем comboBox
    combo = ui.comboBox
    # Добавляем еси надо список значений
    string_list = ['hola muchachos1', 'adios amigos', 'hello world', 'good bye']
    
    GO(combo, string_list)

    sys.exit(app.exec_())
    