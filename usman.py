def calculate_bill():
    # Constants for tax rates and charges
    GST_RATE = 0.17  # 17% GST
    NJ_SURCHARGE_RATE = 0.05  # 5% Neelum Jhelum Surcharge

    # Take input from the user for units consumed
    units = float(input("Enter the units consumed: "))

    # Calculate the cost of electricity consumption
    cost = units * 38.5  # Assuming a unit cost of 15.5 (change this as per actual rates)

    # Calculate the taxes and charges
    gst_amount = cost * GST_RATE
    nj_surcharge_amount = cost * NJ_SURCHARGE_RATE

    # Calculate the total bill amount
    total_amount = cost + gst_amount + nj_surcharge_amount

    # Print the bill details
    print("Electricity Bill Calculation")
    print("---------------------------")
    print("Units Consumed: ", units)
    print("Cost of Electricity: ", cost)
    print("GST (17%): ", gst_amount)
    print("Neelum Jhelum Surcharge (5%): ", nj_surcharge_amount)
    print("Total Bill Amount: ", total_amount)

# Call the function to calculate the bill
calculate_bill()


