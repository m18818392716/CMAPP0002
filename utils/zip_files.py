import os
import zipfile

z = zipfile.ZipFile('../allure_report.zip', 'w', zipfile.ZIP_DEFLATED)
startdir = "../allure-report"

def zip_file():
    for dirpath, dirnames, filenames in os.walk(startdir):
        for filename in filenames:
            z.write(os.path.join(dirpath, filename))
    z.close()