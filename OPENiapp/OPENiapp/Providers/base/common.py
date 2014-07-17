defJsonRes = "Doesn't Exist"
defaultMethodResponse = "Not supported by this service"

def check_if_exists(data, check, otherwise = defJsonRes):
    """ Loop through the  """
    checkArray = check.split('.')
    ret = data
    for allChecks in checkArray:
        if hasattr(ret, allChecks):
            ret = getattr(ret, allChecks)
        elif isinstance(ret, (list, dict)) and (allChecks in ret):
            ret = ret[allChecks]
        else:
            return otherwise
    return ret

def format_generic(data, prepend = ''):
    return {
                "id": data[prepend + 'id'],
                "object_type": data[prepend + 'object_type'],
                "service": data[prepend + 'service'],
                "url": data[prepend + 'url'],
                "from": format_from(data),
                "time": format_time(data)
            }

#   region Profile objects

def format_application(data, prepend = ''):
    return {
                "title": data[prepend + 'application_title'],
                "description": data[prepend + 'application_description'],
                "version": data[prepend + 'application_version'],
                "icon": data[prepend + 'application_icon'],
                "developer": data[prepend + 'application_developer']
            }

def format_device(data, prepend = ''):
    return {
                "manufacturer": data[prepend + 'device_manufacturer'],
                "model": data[prepend + 'device_model'],
                "device_id": data[prepend + 'device_id'],
                "os_type": data[prepend + 'device_os_type'],
                "os_version": data[prepend + 'device_os_version']
            }

def format_file(data, prepend = ''):
    return {
                "title": data[prepend + 'file_title'],
                "description": data[prepend + 'file_description'],
                "format": data[prepend + 'file_format'],
                "size": data[prepend + 'file_size'],
                "icon": data[prepend + 'file_icon']
            }

def format_organization(data, prepend = ''):
    return {
                "name": data[prepend + 'organization_name'],
                "description": data[prepend + 'organization_description'],
                "founded": data[prepend + 'organization_founded'],
                "address": []
            }

def format_person(data, prepend = ''):
    return {
                "name": data[prepend + 'person_name'],
                "surname": data[prepend + 'person_surname'],
                "middlename": data[prepend + 'person_middlename'],
                "birthdate": data[prepend + 'person_birthdate'],
                "organizations": []
            }

def format_place(data, prepend = ''):
    return {
                "name": data[prepend + 'place_name'],
                "description": data[prepend + 'place_description'],
                "category": data[prepend + 'place_category'],
                "picture": data[prepend + 'place_picture'],
                "address": format_address(data, 'place_'),
                "location": format_location(data, 'place_')
            }

def format_product(data, prepend = ''):
    return {
                "name": data[prepend + 'product_name'],
                "description": data[prepend + 'product_description'],
                "category": data[prepend + 'product_category'],
                "picture": data[prepend + 'product_picture'],
                "company": format_organization(data, 'product_'),
                "year": data[prepend + 'product_year']
            }

def format_service(data, prepend = ''):
    return {
                "name": data[prepend + 'service_name'],
                "description": data[prepend + 'service_description'],
                "category": data[prepend + 'service_category'],
                "icon": data[prepend + 'service_icon'],
                "company": format_organization(data, 'service_')
            }

#   endregion Profile objects


#   region Set of Properties

def format_address(data, prepend = ''):
    return {
                "street": data[prepend + 'address_street'],
                "number": data[prepend + 'address_number'],
                "apartment": data[prepend + 'address_apartment'],
                "city": data[prepend + 'address_city'],
                "locality": data[prepend + 'address_locality'],
                "country": data[prepend + 'address_country'],
                "zip": data[prepend + 'address_zip']
            }

def format_duration(data, prepend = ''):
    return {
                "starts_time": data[prepend + 'duration_starts_time'],
                "ends_time": data[prepend + 'duration_ends_time']
            }

def format_from(data, prepend = ''):
    return {
                "id": data[prepend + 'from_id'],
                "object_type": data[prepend + 'from_object_type'],
                "url": data[prepend + 'from_url'],
                "name": data[prepend + 'from_name']
            }

def format_location(data, prepend = ''):
    return {
                "latitude": data[prepend + 'location_latitude'],
                "longtitude": data[prepend + 'location_longitude'],
                "height": data[prepend + 'location_height']
            }

def format_size(data, prepend = ''):
    return {
                "depth": data[prepend + 'size_depth'],
                "height": data[prepend + 'size_height'],
                "width": data[prepend + 'size_width']
            }

def format_tags(data, prepend = ''):
    return {
                "id": data[prepend + 'tags_id'],
                "name": data[prepend + 'tags_name'],
                "time": format_time(data, 'tags_'),
                "x-location": data[prepend + 'tags_x-location'],
                "y-location": data[prepend + 'tags_y-location']
            }

def format_time(data, prepend = ''):
    return {
                "created_time": data[prepend + 'time_created_time'],
                "edited_time": data[prepend + 'time_edited_time'],
                "deleted_time": data[prepend + 'time_deleted_time']
            }

#   endregion Set of Properties