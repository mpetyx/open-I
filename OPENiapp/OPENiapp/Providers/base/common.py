defJsonRes = "Doesn't Exist"
defaultMethodResponse = "Not supported by this service"

def format_file(file_title, file_description, file_format, file_size, file_icon):
    return {
                "title": file_title,
                "description": file_description,
                "format": file_format,
                "size": file_size,
                "icon": file_icon
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

def format_location(location_latitude, location_longtitude, location_height):
    return {
                "latitude": location_latitude,
                "longtitude": location_longtitude,
                "height": location_height
            }

def format_tags(tags_id, tags_name, tag_created_time, tag_edited_time, tag_deleted_time, tags_x_location, tags_y_location):
    return {
                "id": tags_id,
                "name": tags_name,
                "time":
                    { "created_time": tag_created_time,
                      "edited_time": tag_edited_time,
                      "deleted_time": tag_deleted_time
                    },
                "x-location": tags_x_location,
                "y-location": tags_y_location,
            }