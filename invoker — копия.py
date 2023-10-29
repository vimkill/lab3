import itertools as it
s="Account_Balance;Duration_of_Credit_monthly;Payment_Status_of_Previous_Credit;Purpose;Credit_Amount;Value_Savings_Stocks;Length_of_current_employment;Instalment_per_cent;Sex_Marital_Status;Guarantors;Duration_in_Current_address;Most_valuable_available_asset;Age_years;Concurrent_Credits;Type_of_apartment;No_of_Credits_at_this_Bank;Occupation;No_of_dependents;Telephone;Foreign_Worker"
z = s.split(";")
W=[]
for _ in range(1, len(z) + 1):
    W.extend(list(it.combinations(z,_)))
print(list(W[-1]))
