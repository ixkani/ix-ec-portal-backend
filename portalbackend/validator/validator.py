from django.http import JsonResponse

from portalbackend.validator.errormapping import ErrorMessage,ErrorFields


def custom404(request):
    return JsonResponse({
        'status_code': 404,
        'error': 'Invalid URL'
    })

def custom500(request):
    return JsonResponse({
        'status_code': 500,
        'error': 'Internal Server Error'
    })

def init_validator_rules(fields):
    validators = {}
    for field in fields:
        errors = {}
        errors["error_messages"] = {}
        errors["error_messages"]["required"] = ErrorMessage.MISSING_PARAMETERS
        errors["error_messages"]["blank"] = ErrorMessage.REQUIRED_VALID_DATA
        errors["error_messages"]["invalid"] = invalid_message(field)
        errors["error_messages"]["min_length"] = min_length_message(field)
        errors["error_messages"]["null"] = ErrorMessage.SKIP_NULL_VALUE
        errors["error_messages"]["invalid_choice"] = ErrorMessage.INVALID_CHOICE
        errors["error_messages"]["does_not_exist"] = ErrorMessage.DATA_NOT_FOUND
        errors["error_messages"]["incorrect_type"] = ErrorMessage.INVALID_PARAMETERS
        validators[field] = errors
    return validators

def min_length_message(field):
    if field in "website":
        message = ErrorMessage.MINIMUM_LENGTH_4
    elif field in "auth_key" or field in "secret_key":
        message = ErrorMessage.MINIMUM_LENGTH_10
    else:
        message = ErrorMessage.MINIMUM_LENGTH_3
    return message



def invalid_message(field):
    if field in ErrorFields.DATE_FIELDS:
        message = ErrorMessage.INVALID_DATE_FORMAT
    elif field in ErrorFields.PHONE_FIELDS:
        message = ErrorMessage.INVALID_PHONE_NUMBER
    else:
        message = ErrorMessage.REQUIRED_INVALID_DATA
    return message


