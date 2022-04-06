from classic.app.errors import AppError

class WrongObjType(AppError):
    msg_template = "'{obj_type}' is wrong"
    code = 'issue.wrong_obj_type'
