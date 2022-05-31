import dropbox
import os
import sys

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_folder(self, folder_from, folder_to):
        """upload a folder to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(folder_from, 'rb') as f:
            dbx.folders_upload(f.read(), folder_to)

def main():
    access_token = 'gjZBCdrB96gAAAAAAAAAAWBaaDUKWZJJzMKr-iZhFF_xw8oUTanO2sTuDSs_gJFo'
    transferData = TransferData(access_token)

    folder_from = input("Enter the folder name that you want to transport on cloud storage:")
    folder_to = input("enter the full path to upload to dropbox:")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_folder(folder_from, folder_to)

if __name__ == '__main__':
    main()
        # construct the full local path
        local_path = os.path.join(root, foldername)

        # construct the full Dropbox path
        relative_path = os.path.relpath(local_path, local_directory)
        dropbox_path = os.path.join(dropbox_destination, relative_path)

        # upload the file
        with open(local_path, 'rb') as f:
            client.put_file(dropbox_path, f)