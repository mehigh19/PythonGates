import shutil
import os

class MoveFile:
    @staticmethod
    def check_txt():
        source_path = r'HW\PythonGates\intrari\Poarta1.txt'
        destination_path = r'HW\PythonGates\backup_intrari\Poarta1.txt'
        try:
            shutil.move(source_path, destination_path)
            print(f"Successfully moved {source_path} to {destination_path}")
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")
        except PermissionError as e:
            print(f"PermissionError: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    @staticmethod
    def check_csv():
        source_path = r'HW\PythonGates\intrari\Poarta2.csv'
        destination_path = r'HW\PythonGates\backup_intrari\Poarta2.csv'
        try:
            shutil.move(source_path, destination_path)
            print(f"Successfully moved {source_path} to {destination_path}")
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")
        except PermissionError as e:
            print(f"PermissionError: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")