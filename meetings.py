import datetime


def add_meetings(meetings_dict, meeting_name, meeting_date):
    meetings_dict.update({meeting_name: meeting_date})
    return meetings_dict


def delete_meeting(meetings_dict, meeting):
    meetings_dict.pop(meeting)
    return meetings_dict


def change_meeting_date(meetings_dict, changing_key, changed_value):
    meetings_dict[changing_key] = changed_value
    return meetings_dict


def change_meeting_name(meetings_dict, changing_key, changed_key):
    meetings_dict[changed_key] = meetings_dict.pop(changing_key)
    return meetings_dict


def write_meetings(meeting_dict):
    file = open("meeting_file.txt", "w")
    for meeting in meeting_dict.items():
        file.write("{} {}\r\n".format(meeting[0], meeting[1]))


if __name__ == "__main__":
    meeting_dict = {}
    while True:
        task = input(
            """What do you want?
    1 - add meeting
    2 - delete meeting
    3 - change meeting date
    4 - change meeting name
    5 - print all meetings
    6 - write meeting on computer
    7 - show nearest meetings
    0 - exit\n"""
                     )
        if task == "1":
            meeting_name = input("Type meeting name\n")
            meeting_date = input(
                "Type meeting date in format Jun 1 2005 1:33PM\n"
            )
            try:
                convert_to_datetime = datetime.datetime.strptime(
                    meeting_date,
                    '%b %d %Y %I:%M%p'
                )
            except ValueError:
                print("Wrong Date Format")
                continue
            if datetime.datetime.now() > convert_to_datetime:
                print("Date is passed")
                continue
            add_meetings(meeting_dict, meeting_name, convert_to_datetime)
        if task == "2":
            meeting_name = input("Type deleted meeting\n")
            delete_meeting(meeting_dict, meeting_name)
        if task == "3":
            meeting_name == input("Type meeting name\n")
            new_date = input("Type new date of meeting\n")
            convert_to_datetime = datetime.datetime.strptime(
                new_date,
                '%b %d %Y %I:%M%p'
            )
            change_meeting_date(
                meeting_dict,
                meeting_name,
                convert_to_datetime
            )
        if task == "4":
            meeting_name = input("Type changing meeting\n")
            new_meeting_name = input("Type new meeting name\n")
            change_meeting_name(meeting_dict, meeting_name, new_meeting_name)
        if task == "5":
            for meeting in meeting_dict.items():
                print(meeting[0], meeting[1])
        if task == "6":
            write_meetings(meeting_dict)
        if task == "7":
            nearest_meeting = int(input(
                "Type number of hours to find nearest meeting\n"
            ))
            for date in meeting_dict.values():
                deltatime = abs(date - datetime.datetime.now()).total_seconds()
                if deltatime/3600 < nearest_meeting:
                    print("Nearest date is {}".format(date))
        if task == "0":
            exit("Exit!")