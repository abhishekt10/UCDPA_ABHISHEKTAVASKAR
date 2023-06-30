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

# Creating data frame from Dictionary of lists
hotels_dict = {
    'hotel_name': ["The Merrion Hotel", "Glenlo Abbey Hotel", "Conrad Dublin"],
    'location': ["Dublin", "Galway", "Dublin"],
    'rating': ["9.8", "9.1", "8.5"]
}
# Convert dict into dataframe
hotels_ire = pd.DataFrame(hotels_dict)

# print the dataframe
print(hotels_ire)

# Checking if there are any nulls or missing values in the dataset
print(df.isna().any())
print(df.isnull().sum())

# Dropping columns and handling missing value columns from the dataset

df = df.drop(['agent', 'company'], axis=1)

# Listing unique values in each column using for loop
for u in df.columns:
    print(df[u].unique(), "Column_name:", u)

df['country'].fillna('XXX', inplace=True)

df['children'].fillna('0', inplace=True)

# Check to see if there are any nulls or missing value in the dataset
print(df.isnull().sum())

# Drop the duplicates from the dataset and reset the index
df = df.drop_duplicates().reset_index(drop=True)
print(df)
print(df['hotel'].value_counts())
Max_lead_time = df['lead_time'].max()
# check the max lead time bookings have
print(Max_lead_time)

# Indexed and Sorted
sort_df = df.loc[:, ("hotel", "arrival_date_week_number")]
sort_df = sort_df.sort_values('arrival_date_week_number', ascending=False)
print(sort_df)

# grouped by hotel
grouped_df = df.groupby('hotel')[['is_canceled']].sum()
print(grouped_df)

# Importing data using API https://apipheny.io/free-api/

url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'
api_response = requests.get(url)

print(api_response)

api_data = api_response.json()

print(api_data)

for k, v in api_data.items():
    print(k + ':', v)

# Access and process the data as needed
for item in api_data['data']:
    nation = item['Nation']
    population = item['Population']
    year = item['Year']
    print(nation, population, year)


# Group by hotel and arrival year and calculate total guests
print(df.columns)
print(df.dtypes)
df['total_guests'] = df['adults']+df['babies']
print(df[['total_guests', 'hotel']])
total_hotel_guests = df.groupby(['arrival_date_year', 'hotel'])['total_guests'].sum()
print(total_hotel_guests)

# Filtered data for non cancelled bookings and grouped by arrival week with calc of total guests
data = df.loc[(df['is_canceled'] == 0)]
sorted_data = data.groupby('arrival_date_week_number', as_index=False)['total_guests'].sum()\
    .sort_values(by='total_guests', ascending=False)
print(sorted_data)
sns.barplot(data=sorted_data, x='arrival_date_week_number', y='total_guests', order=sorted_data
            .sort_values('total_guests', ascending=False).arrival_date_week_number)
plt.show()
# custom function to convert date to datetime


def dateformat(column):
    return max(pd.to_datetime(column))


print(dateformat(df['reservation_status_date']))

# get min max mean median using np function
hotel_lead_time = df.groupby('hotel')['lead_time'].agg([min, max, np.mean, np.median])
print(hotel_lead_time)
# get count based on reservation status
print(df.reservation_status.value_counts())

# Visualize using bar chart whether booking was cancelled or not and its count
a = df['deposit_type'].value_counts().plot(kind='bar')
plt.show()

# Merge sample hotel data generated
sample1 = {
    'booking_id': ['1', '2', '3', '4'],
    'hotel': ['hotel 1', 'hotel 2', 'hotel 3', 'hotel 4'],
    'Location': ['India', 'New york', 'Dublin', 'Lisbon']
}
df1 = pd.DataFrame(sample1)
print(df1)

sample2 = {
    'booking_id': ['1', '2', '3', '4'],
    'prices': ['250', '500', '300', '200'],
    'Room_type': ['Single', 'penthouse', 'double', 'double'],
    'Location': ['India', 'New york', 'Dublin', 'Lisbon']
    }
df2 = pd.DataFrame(sample2)
print(df2)

merged_data = pd.merge(df1, df2, how='inner', on='booking_id', suffixes=('_df1', '_df2'))
print(merged_data)
print(df1.merge(df2, on='booking_id'))  # give similar output

# Analyze hotel bookings made every month
hotel_bookings = df.groupby('arrival_date_month', sort=True)['hotel'].count()
hotel_bookings.plot(kind='bar', x='Month', y='Number of reservations', title='Hotel Bookings by Month')
plt.show()

# Analyze booking distribution channel

distribution_channel = df.groupby('distribution_channel')['hotel'].count()
distribution_channel.plot(kind='pie', title='Booking Distribution channel')
plt.show()


# Analyze hotel booking cancellations overall

booking_cancellation = df.groupby('is_canceled')['hotel'].count()
sns.barplot(x=booking_cancellation.index, y=booking_cancellation.values)
plt.xlabel('Booking Cancellations yes(1) or No(0)')
plt.ylabel('Count of bookings')
plt.title('Hotel Booking Cancellations')
plt.show()

# Analyze length in stay
df['total_length_of_stay'] = df['stays_in_weekend_nights']+df['stays_in_week_nights']
plt.hist(df['total_length_of_stay'], bins=20)
plt.xlabel('Total_Length_stay')
plt.ylabel('Bookings')
plt.title('Length of Stay in Hotels')
plt.show()

# Analyze mean rate for hotel bookings
adr = df.groupby('hotel')['adr'].mean()
print(adr)
adr.plot(kind='bar')
plt.show()
