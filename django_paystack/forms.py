'''
amount	String	Amount should be in kobo if currency is NGN and pesewas for GHS
email	String	Customer's email address
currency String The transaction currency (NGN, GHS or USD). Defaults to your integration currency.
reference String Unique transaction reference. Only -, ., = and alphanumeric characters allowed.
callback_url String Fully qualified url, e.g. https://example.com/ . Use this to override the callback url provided on the dashboard for this transaction
plan String If transaction is to create a subscription to a predefined plan, provide plan code here. This would invalidate the value provided in amount
invoice_limit Integer Number of times to charge customer during subscription to plan
metadata String Stringified JSON object. Add a custom_fields attribute which has an array of objects if you would like the fields to be added to your transaction when displayed on the dashboard. Sample: {"custom_fields":[{"display_name":"Cart ID","variable_name": "cart_id","value": "8393"}]}
channels Array An array of payment channels to control what channels you want to make available to the user to make a payment with. Available channels include: ['card', 'bank', 'ussd', 'qr', 'mobile_money', 'bank_transfer']
split_code String The split code of the transaction split. e.g. SPL_98WF13Eb3w
subaccount String The code for the subaccount that owns the payment. e.g. ACCT_8f4s1eq7ml6rlzj
transaction_charge Integer A flat fee to charge the subaccount for this transaction, in kobo if currency is NGN and pesewas if currency is GHS. This overrides the split percentage set when the subaccount was created. Ideally, you will need to use this if you are splitting in flat rates (since subaccount creation only allows for percentage split). e.g. 7000 for a 70 naira flat fee.
bearer String Who bears Paystack charges? account or subaccount (defaults to account).
'''
# from django import forms

# class PaymentForm(forms.Form):

#     amount = forms.CharField(max_length=100)
#     email = forms.EmailField(max_length=50)
    
    