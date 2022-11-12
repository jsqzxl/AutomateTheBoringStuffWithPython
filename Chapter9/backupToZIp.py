# backupToZip.py copies an entire folder and its contens into
# a zip file whose filename increments
import zipfile
import os

def backupToZip(folder):

    folder = os.path.abspath(folder)  # make sure folder is absolute

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'

        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the ZIP file
    print('Createing %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    #TODO: Walk the entire folder tree and compress the files in each folder

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # add the current folder to the zip file
        backupZip.write(foldername)
    # Add all the files in this folder to the zip file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue   #don't backup the backup zip files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')


if __name__ == "__main__":

    foldername = '/home/jason/program/socketInternetProgram'
    backupToZip(foldername)
