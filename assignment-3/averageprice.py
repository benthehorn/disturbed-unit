import pandas as pd

#this is untested, because our data is such a mess
def find_averages(frame_path):
    housing_df = pd.read_csv(frame_path)

    cph_sales = housing_df[housing_df['zip_code'].str.contains('1050 | 1049')]
    odense_sales = housing_df[housing_df['zip_code'].str.contains('5000')]
aarhus_sales = housing_df[housing_df['zip_code'].str.contains('8000')]
aalborg_sales = housing_df[housing_df['zip_code'].str.contains('9000')]

cph_sales['sell_year'] = [int(el.split('-')[-1]) for el in cph_sales['sell_date'].values]
odense_sales['sell_year'] = [int(el.split('-')[-1]) for el in odense_sales['sell_date'].values]
aarhus_sales['sell_year'] = [int(el.split('-')[-1]) for el in aarhus_sales['sell_date'].values]
aalborg_sales['sell_year'] = [int(el.split('-')[-1]) for el in aalborg_sales['sell_date'].values]

cph_sales_1992 = cph_sales[cph_sales['zip_code'].str.contains('1050 | 1049') & (cph_sales['sell_year'] == 1992)]
odense_sales_1992 = odense_sales[
    odense_sales['zip_code'].str.contains('1050 | 1049') & (odense_sales['sell_year'] == 1992)]
aarhus_sales_1992 = aarhus_sales[
    aarhus_sales['zip_code'].str.contains('1050 | 1049') & (aarhus_sales['sell_year'] == 1992)]
aalborg_sales_1992 = aalborg_sales[
    aalborg_sales['zip_code'].str.contains('1050 | 1049') & (aalborg_sales['sell_year'] == 1992)]

cph_sales_2016 = cph_sales[cph_sales['zip_code'].str.contains('1050 | 1049') & (cph_sales['sell_year'] == 2016)]
odense_sales_2016 = odense_sales[
    odense_sales['zip_code'].str.contains('1050 | 1049') & (odense_sales['sell_year'] == 2016)]
aarhus_sales_2016 = aarhus_sales[
    aarhus_sales['zip_code'].str.contains('1050 | 1049') & (aarhus_sales['sell_year'] == 2016)]
aalborg_sales_2016 = aalborg_sales[
    aalborg_sales['zip_code'].str.contains('1050 | 1049') & (aalborg_sales['sell_year'] == 2016)]

print(cph_sales)

# here we need to write some code that will take all the price_per_sq_m data, and turn it from strings to floats, so that we can
# do the sums to get our average prices, but again, our data is a mess, so it doesn't get this far without finding too many errors
# to fix..



