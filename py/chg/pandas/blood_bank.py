import pandas as pd
import sys

# data frame for donors.txt
data_frame_of_donors = pd.DataFrame(columns=['Donor_id','Name','Gender','Date_of_birth' ,'Blood_group', 'Wight','City','Mobile_number','Email'])

# data frame for donations.txt
data_frame_of_donations = pd.DataFrame(columns=['Donor_id', 'Donation_date', 'Packet_size'])

# data frame for packet
data_frame_of_available_packets = pd.DataFrame(columns=['Group', 'Packet_size 250', 'Packet_size 500', 'Packet_size 750', 'Packet_size 1000'])


# Append rows in Empty Dataframe by adding dictionaries
# dfObj = dfObj.append({'User_ID': 23, 'UserName': 'Riti', }, ignore_index=True)


def showMenu():
    

sys.exit()