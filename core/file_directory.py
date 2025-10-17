import os
import maya.cmds as cmds

# ประกาศฟังก์ชั่นชื่อ open_current_scene_folder
def open_current_scene_folder():
    
    # ประกาศตัวแปรที่มี value เป็นfull pathไฟล์Maya
    scene_path = cmds.file(query=True, sceneName=True)

    # รีเช็คว่าไฟล์เซฟยัง
    if not scene_path:
        cmds.warning("กรุณากด Save ก่อน")
        return

    # ในกรณีที่ไฟล์หายไปจาก folder ไฟล์ที่ถูกเซฟ
    if not os.path.exists(scene_path):
        cmds.warning("ไม่พบไฟล์ Maya บน disk")
        return

    # เอาเฉพาะ directory (ไม่รวมชื่อไฟล์)
    folder_path = os.path.dirname(scene_path)

    # เปิด File Explorer ใน Windows
    if os.path.exists(folder_path):
        try:
            os.startfile(folder_path)
        except Exception as e:
            cmds.warning(f"เปิดโฟลเดอร์ไม่สำเร็จ")
    else:
        cmds.warning("ไม่พบโฟลเดอร์ที่ไฟล์ Maya อยู่")