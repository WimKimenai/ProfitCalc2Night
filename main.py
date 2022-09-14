import pandas as pd
import numpy as np
from datetime import date
import datetime
import requests

# df = Data Frame
df = pd.read_csv('order_export_2022-08-30-04-50-36.csv')

c = list(df.columns)

# print(c)

# Ignore this
# df2 = pd.read_csv('Revenue streams.csv')
# con_df = pd.concat([df, df2])

# In case you need to reference
# refs = pd.read_csv('refs.csv')

# print(df.head())

# c = list(df.columns)
# print(c)

# All headers
data_cols = ['order_id',
             'order_number',
             'order_date',
             'paid_date',
             'status',
             'shipping_total',
             'shipping_tax_total',
             'fee_total',
             'fee_tax_total',
             'tax_total',
             'cart_discount',
             'order_discount',
             'discount_total',
             'order_total',
             'order_key',
             'order_currency',
             'payment_method',
             'payment_method_title',
             'transaction_id',
             'customer_ip_address',
             'customer_user_agent',
             'shipping_method',
             'customer_id',
             'customer_user',
             'customer_email',
             'billing_first_name',
             'billing_last_name',
             'billing_company',
             'billing_email',
             'billing_phone',
             'billing_address_1',
             'billing_address_2',
             'billing_postcode',
             'billing_city',
             'billing_state',
             'billing_country',
             'shipping_first_name',
             'shipping_last_name',
             'shipping_company',
             'shipping_phone',
             'shipping_address_1',
             'shipping_address_2',
             'shipping_postcode',
             'shipping_city',
             'shipping_state',
             'shipping_country',
             'customer_note',
             'shipping_items',
             'fee_items',
             'tax_items',
             'coupon_items',
             'refund_items',
             'order_notes',
             'meta:_wcpdf_invoice_number',
             'meta:_wcpdf_invoice_date',
             'meta:_wcpdf_invoice_number_data',
             'meta:_wcpdf_invoice_date_formatted',
             'line_item_1',
             'line_item_2',
             'line_item_3',
             'line_item_4',
             'line_item_5']

# Headers to use
data_cola = ['order_number',
             'order_date',
             'shipping_total',
             'order_total',
             'order_currency',
             'shipping_first_name',
             'shipping_last_name',
             'shipping_country',
             'line_item_1',
             'line_item_2',
             'line_item_3',
             'line_item_4',
             'line_item_5']

# Create new dataframe
new_df = df[data_cola]

# Convert USD to EUR - not finished yet
usd_total = new_df[['order_total']]
final_usd_total = usd_total.remove()
# print(usd_total)

# usd_total = new_df['order_total'].values
# usd_total = data_cola.index('order_total')
convert_amount = float(final_usd_total)
from_currency = str("USD")
to_currency = str("EUR")

eur_total = requests.get(
    f"https://api.frankfurter.app/latest?amount={convert_amount}&from={from_currency}&to={to_currency}")

# new_df.append("order_total_eur", eur_total)

print(eur_total.text)

# new_df.append(shipping_costs_dhl)

# Shipping cost DHL + cost per product = Expenses per order
# Shipping amount + item_price = Total income client
# Total income client - Expenses per order = profit

# DHL Shipping Cost
us = 20
eu = 19
south_america = 30
asia = 30
canada = 45
australia = 45

# MATRODA
# Black & White T-Shirt = 14.35
# Hoodie = 15.95
# Long Sleeve Black & White =

# Blue Clair
# Black & White T-Shirt = 14.35
# Sand T-Shirt = 14.85
# Shoulder Bag = 5.95
# Crew Neck = 12.50
# Hoodie = 15.95


# Remove currency
# new_df['order_total'] = new_df['order_total'].str.replace(r'€', '').astype(float)

# print(new_df)

# Get time and date for file output
current_date = date.today()
current_date2 = current_date.strftime('%m-%d-%Y')

current_time = datetime.datetime.now()
current_time2 = ("%s-%s-%s" % (current_time.hour, current_time.minute, current_time.second))

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('2NightMerchOrders ' + current_date2 + " " + current_time2 + '.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
new_df.to_excel(writer, sheet_name='Blue Clair Merch', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
