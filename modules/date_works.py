import adbs
def eng2nepali_date(year, month, day): #characterised DATE
    required_dictionary = adbs.ad_to_bs(f'{year}/{month}/{day}')['en']
    # Saturday, 13 April 2019
    required_data = f"{required_dictionary['str_day_of_week']}, {required_dictionary['day']} {required_dictionary['str_month']} {required_dictionary['year']}"
    
    return required_data

def convert(year, month, day):
    required_dictionary = adbs.bs_to_ad(f'{year}/{month}/{day}')
    print(required_dictionary)
    # Saturday, 13 April 2019
    eng_date = f"{required_dictionary['str_day_of_week']}, {required_dictionary['day']} {required_dictionary['str_month']} {required_dictionary['year']}"
    nep_date = eng2nepali_date(required_dictionary['year'], required_dictionary['month'], required_dictionary['day'])
    required_data = {
        'en':eng_date,
        'np' : nep_date
        }
    return required_data

