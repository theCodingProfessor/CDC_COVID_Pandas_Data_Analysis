# Clinton Garwood
# Using Pandas to analyze CDC Dailys Data

# Change log: Features not yet implemented; Final File Gen, New Data Ingestion

import pandas as pd
import matplotlib.pyplot as plt

def import_data():
    # Import Data from CSV
    df_cdc_all = pd.read_csv("United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv")
    # Explicitly create a data frame
    cdc_df = pd.DataFrame(df_cdc_all)
    return cdc_df

def read_df_info(cdc_df):
    # Take a look at the data
    # [44820 rows x 15 columns] - this is what is found
    print(cdc_df.info)
    return

def describe_df_info(cdc_df):
    # Get metadata about the data
    # responds with [8 rows (of data) in 10 columns
    print(cdc_df.describe())
    return

def determine_nulls(cdc_df):
    # Determine if null values exist
    # columns without null data:
    # submission_date, state, tot_cases, new_case, tot_death, created_at, new_death
    cdc_df.info()

def trim_data(cdc_df):
    """ we want columns named: submission_date, state, tot_cases, new_case, tot_death, new_death
    # this allows us to continue without dropping or altering any data
    # we effectively drop columns named; consent_deaths, consent_deaths """
    df_cdc_using = cdc_df.loc[:, ["submission_date", "state", "tot_cases", "new_case", "tot_death", "created_at", "new_death"]]
    #print("The total number of duplicate rows are: ", df_cdc_using.duplicated().sum())
    #print(df_cdc_using.head(3))
    return df_cdc_using

def determine_most_recent_date(cdc_df):
    # Grab the dates column from df_cdc_using - trimmed list
    df_just_dates = cdc_df.loc[:, ["submission_date"]]
    # Cast the date column to be datetime objects
    #df_just_dates['submission_date'] = df_just_dates['submission_date'].astype('datetime64[ns]')
    # parse out the most recent date
    #max_date = df_just_dates.max()
    cdc_df['submission_date'] = cdc_df['submission_date'].astype('datetime64[ns]')
    # Search for max date
    max_date = cdc_df['submission_date'].max()
    # pull the rows with that date
    selected_dates_df = cdc_df[cdc_df['submission_date'] == max_date]
    #dates_df = df_cdc_using[df_cdc_using['submission_date'] == max_date]
    #print(selected_dates_df.describe())
    #print(selected_dates_df.info())
    #print(selected_dates_df.head(10))
    return max_date, selected_dates_df

def generate_national(max_date, df_cdc_using):
    # National Summary (all states);
    # 1) Total Cases
    # 2) Total New Cases
    # 3) Total Deaths
    # 4) Total New Deaths
    #df_cdc_national_summary = df_cdc_all.loc[:, ["tot_cases", "new_case", "tot_death", "new_death"]]
    # This is the number we want for the most recent date
    # Parse the list to find the most recent date.
    # Next we want to 'sum()' the 'tot_cases' for each state, for that date.
    # Update the 'submission_date' row to a date object type
    print("\n Selected dates")
    # print(selected_dates_df)
    # st = selected_dates_df.loc['states']
    # print(st)
    return

def print_national_summary(max_date,selected_dates_df):
    print("\n\tNational Summary Data as of ", max_date)
    print("\t\tTotal cases reported nationally: {:,}".format(selected_dates_df["tot_cases"].sum()))
    print("\t\tTotal new cases reported: {:,}".format(selected_dates_df["new_case"].sum()))
    print("\t\tTotal deaths reported nationally: {:,}".format(selected_dates_df["tot_death"].sum()))
    print("\t\tTotal new deaths reported: {:,}".format(selected_dates_df["new_death"].sum()))
    return

def state_summary(selected_dates_df, max_date):
    # State Summary State (retrieve state level data by prompting a user to enter a two-character state code)
    # 1) Total Cases
    # 2) Total New Cases
    # 3) Total Deaths
    # 4) Total New Deaths
    # Jurisdictions may include cities or territories:
    # HI, MA, AS, GA, TX, OK, FL, NY, IA, OH, SD, GU, ME, IL, WI, AL, CA, NH, MO, MT,
    # DE, ND, NE, WA, MN, DC, RI, OR, WY, FSM, NJ, KY, NV, CT, NC, VI, IN, VT, MI, MS,
    # MD, ID, AZ, SC, VA, LA, KS, AR, MP, PW, AK, UT, CO, PR WV, NYC, RMI, TN, PA, NM
    st = selected_dates_df['state']
    st_lst = input("\n\tPlease enter the jurisdiction code (i.e., IL) ").upper()
    try:
        if (selected_dates_df['state'].str.contains(st_lst.upper(), regex=False).any() == True):
            print("\t\tJurisiction Data (i.e., States) from ", max_date)
            # #state_df = selected_dates_df.loc[selected_dates_df['state']]
            state_df = selected_dates_df[selected_dates_df['state'] == st_lst.upper()]
            #print(state_df)
            print("\t\t\tState Level Data for", st_lst.upper())
            print("\t\t\t\tTotal state cases reported: {:,}".format(state_df["tot_cases"].sum()))
            print("\t\t\t\tTotal state new cases reported: {}".format(state_df["new_case"].sum()))
            print("\t\t\t\tTotal state deaths reported: {:,}".format(state_df["tot_death"].sum()))
            print("\t\t\t\tTotal state new deaths reported: {:,}".format(state_df["new_death"].sum()))
        else:
            print("\n\tSorry, could not find data for the state you requested.")
    except:
        print("\n\tSorry, could not find data for the state you requested.")
    return

def main():
    cdc_df = import_data()
    df_cdc_using = trim_data(cdc_df)
    max_date, selected_dates_df = determine_most_recent_date(cdc_df)
    generate_national(max_date, df_cdc_using)
    print_options()
    try:
        exit_program = int(input("\n\tPlease enter an option, or zero to exit "))
    except ValueError:
        print("Invalid data submitted, please try again")
    while exit_program != 0:
        if exit_program == 1:
            print_national_summary(max_date, selected_dates_df)
        elif exit_program == 2:
            state_summary(selected_dates_df, max_date)
        elif exit_program == 3:
            read_df_info(cdc_df)
        elif exit_program == 4:
            describe_df_info(cdc_df)
        elif exit_program == 5:
            determine_nulls(cdc_df)
        elif exit_program == 6:
            print("\nNot yet implemented.")
        elif exit_program > 6:
            print("\nInvalid option please try again")
        pause = input("\nPlease press enter to continue...")
        print_options()
        try:
            exit_program = int(input("\n\tPlease enter an option, or zero to exit "))
        except ValueError:
            print("Invalid data submitted, please try again")
    return

def print_options():
    print("\n\tOption 1) To Run National Summary")
    print("\tOption 2) Run Local Summary")
    print("\tOption 3) Show Dataset Info")
    print("\tOption 4) Describe Dataset")
    print("\tOption 5) Show Null Value Summary in Dataset")
    print("\tOption 6) Query/get most recent data from CDC")
    print("\t...Enter 0 to exit")
    return

main()