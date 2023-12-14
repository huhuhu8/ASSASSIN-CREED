<<<<<<< HEAD
import os

folder_path = "yolo-class/Annotations/"

# フォルダ内のすべてのファイルを削除
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(f"ファイル {file_path} を削除中にエラーが発生しました: {e}")

folder_path = "yolo-class/JPEGImages/"

# フォルダ内のすべてのファイルを削除
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(f"ファイル {file_path} を削除中にエラーが発生しました: {e}")
=======
import os

folder_path = "yolo-class/Annotations/"

# フォルダ内のすべてのファイルを削除
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(f"ファイル {file_path} を削除中にエラーが発生しました: {e}")

folder_path = "yolo-class/JPEGImages/"

# フォルダ内のすべてのファイルを削除
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(f"ファイル {file_path} を削除中にエラーが発生しました: {e}")
>>>>>>> ba3da11f9f1493eaaa5990301d5becac0985992f
