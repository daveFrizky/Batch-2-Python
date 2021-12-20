def KelvinCelcius(suhu,tipeSuhu):
    "Function Convert temperature to kelvin or celcius depend on the input type. return converted temperature"
    if tipeSuhu=="c":
        return suhu+273.15
    elif tipeSuhu=="k":
        return suhu-273.15
    else:
        return; 

def ToFahrenheit(suhu,tipeSuhu):
    "Function Convert temperature to fahrenheit from celcius or kelvin. return temperature in fahrenheit"
    if tipeSuhu=="c":
        return (suhu*9)/5+32
    elif tipeSuhu=="k":
        return (KelvinCelcius(suhu,tipeSuhu)*9)/5+32
    else:
        return;
    
def FtoKelvinCelcius(suhu,outputSuhu):
    "Function Convert temperature from fahrenheit to celcius or kelvin. return converted temperature Celcius,Kelvin"
    if outputSuhu=="c":
        return (suhu-32)*5/9,"k"
    elif outputSuhu=="k":
        return  (suhu-32)*5/9+273.15,"k"
    else:
        return;        

def showSuhu(suhu,tipeSuhu):
    if tipeSuhu=="c":
        return "Suhu = "+str(suhu)+" Celcius"
    elif tipeSuhu=="k":
        return "Suhu = "+str(suhu)+" Kelvin"
    elif tipeSuhu=="f":
        return "Suhu = "+str(suhu)+" Fahrenheit"
    else:
        return ; 
        

tipeSuhu=input("Temperature Unit Kelvin or Fahrenheit or Celcius(K/F/C): ")
tipeSuhu=tipeSuhu.lower()    
suhu=float(input("Enter Temperature: "))
while True:
    print("\n",showSuhu(suhu,tipeSuhu))
    print(
        "0. Exit\n"+
        "1. Kelvin To Celcius\n"+
        "2. Celcius to Kelvin\n"+
        "3. to Fahrenheit\n"+
        "4. Fahrenheit to Kelvin\n"+
        "5. Fahrenheit to Celcius\n"        
        )
    menu=int(input("Menu (0-5): "))
    if menu==0:
        print("Bye-bye")
        break
    elif menu==1:
        if tipeSuhu=="k":
            suhu=KelvinCelcius(suhu,tipeSuhu)
            tipeSuhu="c"
        else:
            print("Invalid Input. should be in Kelvin")
    elif menu==2:
        if tipeSuhu=="c":
            suhu=KelvinCelcius(suhu,tipeSuhu)
            tipeSuhu="k"
        else:
            print("Invalid Input. should be in Celcius")
    elif menu==3:
        if tipeSuhu=="c" or tipeSuhu=="k":
            suhu=ToFahrenheit(suhu,tipeSuhu)
            tipeSuhu="f"
        else:
            print("Invalid Input. should be in Celcius or Kelvin")
    elif menu==4:
        if tipeSuhu=="f":
            suhu,tipeSuhu=FtoKelvinCelcius(suhu,"k")
        else:
            print("Invalid Input. should be in Fahrenheit")
    elif menu==5:
        if tipeSuhu=="f":
            suhu,tipeSuhu=FtoKelvinCelcius(suhu,"c")
        else:
            print("Invalid Input. should be in Fahrenheit")
    else:
        print("Invalid Input. should be 0-5")
        