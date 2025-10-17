# lighting_tools/ui/maya/tools/rename_tool_ui.py

from PySide2 import QtWidgets
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
from lighting_tools.core import rename_tool
rename_tool_ui.show_rename_tool_ui()


def get_maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

def show_rename_tool_ui():
    for widget in QtWidgets.QApplication.allWidgets():
        if widget.objectName() == "RenameToolWindow":
            widget.close()

    window = QtWidgets.QWidget(parent=get_maya_main_window())
    window.setObjectName("RenameToolWindow")
    window.setWindowTitle("Rename Tool")
    window.setMinimumSize(300, 180)

    layout = QtWidgets.QVBoxLayout(window)

    # ช่อง Search for
    search_input = QtWidgets.QLineEdit()
    search_input.setPlaceholderText("Search for...")

    # ช่อง Replace with
    replace_input = QtWidgets.QLineEdit()
    replace_input.setPlaceholderText("Replace with...")

    # Radio buttons
    scope_group = QtWidgets.QButtonGroup(window)
    hierarchy_radio = QtWidgets.QRadioButton("Hierarchy")
    selected_radio = QtWidgets.QRadioButton("Selected")
    all_radio = QtWidgets.QRadioButton("All")
    all_radio.setChecked(True)

    scope_group.addButton(hierarchy_radio)
    scope_group.addButton(selected_radio)
    scope_group.addButton(all_radio)

    scope_layout = QtWidgets.QHBoxLayout()
    scope_layout.addWidget(hierarchy_radio)
    scope_layout.addWidget(selected_radio)
    scope_layout.addWidget(all_radio)

    # ปุ่ม Replace
    replace_btn = QtWidgets.QPushButton("Replace")

    # ปุ่ม Clean __pasted
    clean_btn = QtWidgets.QPushButton("Clean pasted__")

    # Layout ใส่ทุกอย่าง
    layout.addWidget(QtWidgets.QLabel("Search for:"))
    layout.addWidget(search_input)
    layout.addWidget(QtWidgets.QLabel("Replace with:"))
    layout.addWidget(replace_input)
    layout.addLayout(scope_layout)
    layout.addWidget(replace_btn)
    layout.addWidget(clean_btn)

    # --- Callback Logic ---
    def run_replace():
        search = search_input.text()
        replace = replace_input.text()
        scope = "all"
        if hierarchy_radio.isChecked():
            scope = "hierarchy"
        elif selected_radio.isChecked():
            scope = "selected"

        count = rename_tool.rename_objects(search, replace, scope)
        QtWidgets.QMessageBox.information(window, "Result", f"Renamed {count} object(s).")

    def run_clean():
        count = rename_tool.rename_objects("pasted__", "", "all")
        QtWidgets.QMessageBox.information(window, "Cleaned", f"Cleaned pasted__ from {count} object(s).")

    replace_btn.clicked.connect(run_replace)
    clean_btn.clicked.connect(run_clean)

    window.show()
    return window


