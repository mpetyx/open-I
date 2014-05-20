defJsonRes = "Doesn't Exist"
defaultMethodResponse = "Not supported by this service"

def format_file(file_title, file_description, file_format, file_size, file_icon):
    return {
                "file_title": file_title,
                "file_description": file_description,
                "file_format": file_format,
                "file_size": file_size,
                "file_icon": file_icon
            }

def format_person(from_id, from_name, from_surname, from_middlename, from_birthdate, from_orgs):
    return {
                "id": from_id,
                "name": from_name,
                "surname": from_surname,
                "middlename": from_middlename,
                "birthdate": from_birthdate,
                "organizations": from_orgs
            }

def format_time(created_time, edited_time, deleted_time):
    return {
                "created_time": created_time,
                "edited_time": edited_time,
                "deleted_time": deleted_time
            }