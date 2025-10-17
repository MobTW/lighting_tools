from PySide2 import QtWidgets
from lighting_tools.core import file_directory

# เก็บหน้าต่างไว้ไม่ให้ถูก Garbage Collected
_file_directory_ui_instance = None

def show_file_directory_ui():
    global _file_directory_ui_instance

    # ปิดหน้าต่างเดิม (ถ้ามี)
    for widget in QtWidgets.QApplication.allWidgets():
        if widget.objectName() == "FileDirectoryWindow":
            widget.close()

    # สร้างหน้าต่างใหม่
    window = QtWidgets.QWidget()
    window.setObjectName("FileDirectoryWindow")
    window.setWindowTitle("Open Scene Folder")
    window.setMinimumSize(300, 100)

    # Layout และปุ่ม
    layout = QtWidgets.QVBoxLayout(window)
    open_button = QtWidgets.QPushButton("📂 เปิดโฟลเดอร์ไฟล์ Maya ปัจจุบัน")
    layout.addWidget(open_button)

    # เชื่อมปุ่มกับฟังก์ชันเปิดโฟลเดอร์
    open_button.clicked.connect(file_directory.open_current_scene_folder)

    window.show()

    # เก็บอ้างอิงไว้ ไม่ให้ถูกปิด
    _file_directory_ui_instance = window
