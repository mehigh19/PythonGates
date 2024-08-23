import shutil
import os

class MoveFile():
    @staticmethod
    def check_txt(txt_file):
        source_path = f'HW\\PythonGates\\intrari\\{txt_file}'
        destination_path = f'HW\\PythonGates\\backup_intrari\\{txt_file}'
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
    def check_csv(csv_file):
        source_path = f'HW\\PythonGates\\intrari\\{csv_file}'
        destination_path = f'HW\\PythonGates\\backup_intrari\\{csv_file}'
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
    def get_txt_files(directory=r'HW\PythonGates\intrari'):
        return [f for f in os.listdir(directory) if f.endswith('.txt')]

    @staticmethod
    def get_csv_files(directory=r'HW\PythonGates\intrari'):
        return [f for f in os.listdir(directory) if f.endswith('.csv')]