def calculate_bill(units):
    slab_rates = {
        1: 13.48,
        2: 18.95,
        3: 22.14,
        4: 25.53,
        5: 27.74,
        6: 29.16,
        7: 30.30,
        8: 35.22,
    }
    cost_of_electricity = units * slab_rates[min(units, 8)]
    gst = 0.21 * cost_of_electricity
    neelum_jhelum_surcharge = 0.05 * cost_of_electricity
    electricity_duty = 0.0015 * cost_of_electricity
    tv_fee = 35
    fc_surcharge = 1703.72 * (units / 17000)
    total_charges = cost_of_electricity + gst + neelum_jhelum_surcharge + electricity_duty + tv_fee + fc_surcharge
    return total_charges

if __name__ == "__main__":
    units = int(input("Enter the number of units consumed: "))
    total_charges = calculate_bill(units)
    print("Total charges:", total_charges)
