def total_expenditure(exp):
    total = 0
    for cost in exp:
        total=total+cost
    return total

    total_cost_tanjim=[1000,2000,3000]
    total_cost_alif=[2500,3000,2200]


    tanjim_cost=total_expenditure(total_cost_tanjim)
    alif_cost=total_expenditure(total_cost_alif)
    print("tanjim_cost")
    Print("alif_cost")
