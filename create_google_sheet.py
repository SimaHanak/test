from hanak_config_appka import *

def create_google_sheet_in_folder(folder_id, sheet_name):
    try:
        # Create a new Google Sheet
        sheet = gc.create(sheet_name)
        print(f"Google Sheet created with ID: {sheet.id}")
        # Move the Google Sheet to the specified folder
        drive_service.files().update(
            fileId=sheet.id,
            addParents=folder_id,
            removeParents="root",
            fields="id, parents"
        ).execute()

        return sheet
    except HttpError as error:
        print(f"An error occurred: {error}")
        print(error.resp)
        print(error.content)
        return None

# Update with your folder ID and sheet name
folder_id = "1m8CLTK42OrtG6sl1-bz01HsRBQMTtDCW"
sheet_name = "Database"
# Create the sheet and move it to the folder
sheet = create_google_sheet_in_folder(folder_id, sheet_name)