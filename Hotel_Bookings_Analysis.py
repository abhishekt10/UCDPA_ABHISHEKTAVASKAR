# Variables in Dataset:
# hotel : Displays either it's a Resort or City type hotel
# is_canceled : indicates if the booking was cancelled or not
# lead_time : number of days passed between entering date of booking into the PMS and the arrival date
# arrival_date_year : arrival year
# arrival_date_month : arrival month
# arrival_date_day : arrival day
# stays_in_weekend_nights : number of weekend days stayed or booking made
# stays_in_week_nights : number of week days stayed or booking made
# adults : number of adults
# children : number of children
# babies : number pf babies
# meal : type of meal booked
# country : country of origin categories are represented in the ISO 3155–3:2013 format
# market_segment : Market segment designation. In categories, the term “TA” means “Travel Agents”
#                  and “TO” means “Tour Operators”
# distribution_channel :Booking distribution channel.The term “TA” means “Travel Agents” and “TO” means “Tour Operators”
# is_repeated_guest : Value indicating if the booking name was from a repeated guest (1) or not (0)
# previous_cancellations : Number of previous bookings that were cancelled by the customer prior to the current booking
# previous_bookings_not_canceled :Number of previous bookings not cancelled by the customer prior to the current booking
# reserved_room_type : Code of room type reserved. Code is presented instead of designation for anonymity reasons.
# assigned_room_type : Code for the type of room assigned to the booking. Sometimes the assigned room type differs \
#                       from the reserved room type due
# booking_changes : Number of changes/amendments made to the booking from the moment the booking was entered on the PMS
# deposit_type : Indication on if the customer made a deposit to guarantee the booking.\
#                This variable can assume three categories: No
# agent : ID of the travel agency that made the booking
# company : ID of the company/entity that made the booking or responsible for paying the booking. \
#           ID is presented instead of designation for
# days_in_waiting_list : Number of days the booking was in the waiting list before it was confirmed to the customer
# customer_type : Type of booking, assuming one of four categories: Contract - when the booking has an allotment \
#                or other type of
# adr : Average Daily Rate as defined by dividing the sum of all lodging transactions by the total number of stay nights
# required_car_parking_spaces : Number of car parking spaces required by the customer
# total_of_special_request : Number of special requests made by the customer (e.g. twin bed or high floor)
# reservation_status : Reservation last status, assuming one of three categories: Canceled – \
#                      booking was canceled by the customer; Check-Out
# reservation_status_date : Date at which the last status was set. This variable can be used in conjunction \
#                           with the ReservationStatus to


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests

# Import and Load the Hotel Bookings dataset csv file
df = pd.read_csv("/Users/Public/UCDPA_ABHISHEKTAVASKAR/hotel_bookings.csv")

# Exploring the dataset
# Displaying first few rows from the data frame
print(df.head())

# Understand the shape of the dataset explaining number of rows and columns in the dataset
print(df.shape)

# Info of hotel bookings data frame
print(df.info())

# Generating the statistics of the hotel booking dataset
print(df.describe())
print(df.describe().T)  # Transposed the dataset
