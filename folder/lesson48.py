import zipfile
import os

folder_path = '/folder'
zip_path = '/folder/test.zip'
zip_name = 'test.zip'

my_zip = zipfile.ZipFile(zip_path, 'w')

my_zip.write('c:\\Users\\User\\PycharmProjects\\TeachPythonWithCourseHunter\\folder\\file.txt', compress_type=zipfile.ZIP_DEFLATED)

my_zip.close()





