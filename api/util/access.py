
def administor(current_user):
    if current_user.type == 'medical_doctor':
        return {"message": "You are not authorized to access this resource."}, 401
    else:
        pass

def medical_doctor(current_user):
    if current_user.type == 'administor':
        return {"message": "You are not authorized to access this resource."}, 401
    else:
        pass