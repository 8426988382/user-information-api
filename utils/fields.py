personal_info = [
    "firstName",
    "lastName",
    "mother_name",
    "father_name",
    "dob",
    "gender",
    "bg",
    "marital_status",
    "unmarried",
    "occupation",
    "nationality"
]

contact_info = [
    "mobile_number1",
    "mobile_number2",
    "landline",
    "personal_email",
    "company_email",
    "permanent_address",
    "current_address",
    "work_address",
    "emergency_contact1",
    "emergency_contact1"
]

educational_info = [
    "senior_school_name",
    "senior_school_board",
    "senior_school_percentage",
    "senior_school_passing_year",
    "senior_sec_school_name",
    "senior_sec_school_board",
    "senior_sec_school_percentage",
    "senior_sec_school_passing_year",
    "grad_university_name",
    "grad_percentage",
    "grad_passing_year"
]


def check_for_values(values, check_parameter):
    try:
        check_parameter = check_parameter + '_info'

        if check_parameter == 'personal_info':
            check_parameter = personal_info
        if check_parameter == 'contact_info':
            check_parameter = contact_info
        if check_parameter == 'educational_info':
            check_parameter = educational_info
        print(check_parameter)
        for value in values:
            if value not in check_parameter:
                return -1

        return 1
    except:
        return 0
