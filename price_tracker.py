

choice=int(input(print("1.)For Amazon product.\n2.)For Flipkart product\n3.)To Exit")).strip())

while(choice!=3):
    if choice==1:
        import Amazon
        Amazon.check()

    elif choice==2:
        import Flipkart
        Flipkart.check_price()
    elif choice==3:
        quit()
    else :
        print('Invalid choice.Try Again!!!')

    choice=int(input(print("1.)For Amazon product.\n2.)For Flipkart product\n3.)To Exit")).strip())
