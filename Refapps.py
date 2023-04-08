def computeRefund():  # Function that compute the refund owns for bottles
    bottleSize, numBottle = (), ()
    OneLtrNless, moreThan1ltr = 0.10, 0.25  # Refund value for 1 ltr or 2 ltrs bottles
    totalRef, refundSmall, refundLrge = 0, 0, 0  # Initializing variables

    count = 1
    while count <= 2:  # Loop breaking condition
        numBottle = input("Number of bottle: ")  # User input
        bottleSize = input("Bottle size (1 or 2 Ltr): ")  # User input

        if int(bottleSize) == 1:
            refundSmall = int(numBottle) * OneLtrNless  # Formula to calculate the refund value
            print(f'You get ${refundSmall:.2f} for the small bottles')  # Display the value to receive
            totalRef += refundSmall  # Increment the total refund to Keep track
            print("--------------------------------------")

        elif int(bottleSize) == 2:
            refundLrge = int(numBottle) * moreThan1ltr  # Formula to calculate the refund value
            print(f'You get ${refundLrge:.2f} for the large bottles')  # Display the value to receive
            totalRef += refundLrge  # Increment the total refund to Keep track
            print("---------------------------------------")
        elif int(bottleSize) > 2:
            print('Error Dude, relaunch the program again!')  # Flag error if the above conditions are not met
            break

        count += 1  # Keep track of the count by incrementing at each loop
    result = print(f'Your total refund is ${totalRef:.2f}')  # Display the total refund amount to be paid
    print("---------------------------------------")
    return result


computeRefund()