from datetime import datetime


def path_to_upload(instance, filename) -> str:
    date_ = datetime.now()
    date_str = date_.strftime("%Y%m%d_%H%M%S")
    file_name, ext = filename.split(".")
    upload_filename = f"{file_name}_{date_str}.{ext}"
    upload_path = "profile_pictures/{0}/{1}/{2}/{3}".format(date_.year,
                                                            date_.month,
                                                            date_.day,
                                                            upload_filename,)
    return upload_path
