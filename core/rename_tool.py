# lighting_tools/core/rename_tool.py

import maya.cmds as cmds

def rename_objects(search, replace, scope="all"):
    if not search:
        cmds.warning("ต้องใส่คำค้นหา (search)")
        return 0

    # ดึง objects ตาม scope
    if scope == "selected":
        objects = cmds.ls(selection=True, long=True)
    elif scope == "hierarchy":
        selected = cmds.ls(selection=True, long=True)
        objects = []
        for obj in selected:
            children = cmds.listRelatives(obj, allDescendents=True, fullPath=True) or []
            objects.extend(children)
        objects = list(set(objects))  # remove duplicates
    else:  # all
        objects = cmds.ls(dag=True, long=True)

    if not objects:
        cmds.warning("ไม่พบ object ตาม scope ที่เลือก")
        return 0

    renamed_count = 0

    for obj in objects:
        name = obj.split("|")[-1]  # ชื่อเฉพาะตัว ไม่รวม path
        if search in name:
            new_name = name.replace(search, replace)
            try:
                cmds.rename(obj, new_name)
                renamed_count += 1
            except Exception as e:
                print(f"⚠️ Rename failed: {obj} -> {new_name} ({e})")

    return renamed_count
