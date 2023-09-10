# # Booking System
# # Design a booking system where users specify a start datetime, end datetime, and timezone. Implement a function that checks whether a specified time slot is available.
# # if timeslot is available then store the start_date and end_date in the list of objects i.e
# """
# booking_storage = [
#   {
#     "car_model": "", # corolla, civic

#     "start_date": "",
#     "end_date": ""
#   }
# ]
# """
# # hint 1: store dates in booking_storage in UTC format i.e pytz.utc
# # hint 2: use for loop, the loop should run 5 times. ask user input inside the loop

# # instruction to test your program:
# # first iteration of loop
# # give input "2023-08-26 18:00:00" as start_date and "2023-08-26 19:00:00" as end_date and "Asia/Karachi" as timezone and car_model 

# # second iteration of loop
# # give input "2023-08-26 16:00:00" as start_date and "2023-08-26 17:00:00" as end_date and "Asia/Riyadh" as timezone  and car_model 
# # above program should not accept this booking as the slot is already booked by the first iteration

# You must write the following functions

# add_tz() # this should convert naive date to tz_awre
# convert_tz() # this should convert date from one tz to another
# is_slot_available() # this should return True or False
# book_the_car() # this should add the detail in booking_storage

# I didn't mention what info you need to pass to the above functions. Its part of your assigment to pass info to the function and return the value from function.


from datetime import datetime
import pytz
# Cars List
booking_storage = []
cars = ['swift','civic','corolla','sportage','alto']

# Get Time Zone Function
def time_zone_work(from_user):
    all_tz = pytz.all_timezones
    from_user = datetime.now(tz=pytz.timezone('Asia/'+from_user))
    print(from_user)
    return from_user



# Bookin Function
def booking_car():
    
    # Show Available cars name
    print(cars)
    
    # select car name
    select_car = input('Select your Car: ')

    # Info user living
    print('Where are you from.')
    where_from = input('Please Type karachi/Riyadh:  ')
    time_zone_work(where_from)

    # Booking start Date
    print('Enter date where start your car booking.')
    from_date = input('please type date in this format>>> year-month-date: ')
    st_date = datetime.fromisoformat(from_date)
    # book_start_date = st_date.date()

    # Booking end Date
    print('Enter date where end your car booking.')
    end_date = input('please type date in this format>>> year-month-date: ')
    en_date = datetime.fromisoformat(end_date)
    # book_end_date = en_date.date()

    # Check is Car available or not 
    for check_available_car in cars:
        if select_car == check_available_car:
            booking_storage.append({
                'car_model': select_car,
                'start_date': st_date.date(),
                'end_date': en_date.date(),
                'time_zone': where_from,
            })
            print('Your Car Booking has Successfully')
            print('Your Booking Details is.')
            print(booking_storage)
            cars.remove(select_car)
            break
        else:
            continue
    else:
        print('SORRY... This cars is not available yet....!')
        print('Try After some time')
        print(booking_storage)


                     
    



booking_car()