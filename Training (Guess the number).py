#Variables 1
try :
    var_a = int(input("Guess my number :"))
except :
    print("I said number, not words dummy. Im outta here")
    input("Type any button to close...")
else :
    var_b = int(17)
    var_z = var_a
    if var_z != var_b :
        if var_z < var_b :
            print("WRONG! you guessed too low! it was",var_b)
            var_pass = "No"
        elif var_z > var_b :
            print("WRONG! you guessed too high! it was",var_b)
            var_pass = "No"
    else :
        print("Wow, you actually guessed it")
        var_pass = "Yes"
 
    print("Guess my number again! you have three chances")
    #Variables 2
    var_c = int(var_z + var_b)
    try :
        var_d = int(input())
    except :
        print("I said number, not words dummy. Im outta here")
        input("Type any button to close...")
    else :
        var_d = var_d

        if var_d != var_c :
            if var_d < var_c :
                print("Too low! Try again!")
                var_e = int(input())
                if var_e < var_c :
                    print("Too low! Try again!")
                    var_f = int(input())
                    if var_f < var_c :
                        print("*BEEP* Out of tries.")
                        input("Type any button to close...")
                    elif var_f > var_c :
                        print("*BEEP* Out of tries.")
                        input("Type any button to close...")
                    else :
                        print("Nice! You did it!")
                        input("Type any button to close...")
                elif var_e > var_c :
                    print("Too high! Try again!")
                    var_f = int(input())
                    if var_f < var_c :
                        print("*BEEP* Out of tries.")
                        input("Type any button to close...")
                    elif var_f > var_c :
                        print("*BEEP* Out of tries.")
                        input("Type any button to close...")
                    else :
                        print("Nice! You did it!")
                        input("Type any button to close...")
                else :
                    print("Nice! You did it!")
                    input("Type any button to close...")
            elif var_d > var_c :
                print("Too high! Try again!")
                var_e = int(input())
                if var_e < var_c :
                    print("Too low! Try again!")
                    var_f = int(input())
                    if var_f < var_c :
                        print("*BEEP* Out of tries.")
                        input("Type any button to close...")
                    elif var_f > var_c :
                        print("*BEEP* Out of tries.")
                        input("Type any button to close...")
                    else :
                        print("Nice! You did it!")
                        input("Type any button to close...")
                elif var_e > var_c :
                    print("Too high! Try again!")
                    var_f = int(input())
                    if var_f < var_c :
                        print("*BEEP* Out of tries.")
                        input("Type any button to close...")
                    elif var_f > var_c :
                        print("*BEEP* Out of tries.")
                        input("Type any button to close...")
                    else :
                        print("Nice! You did it!")
                        input("Type any button to close...")
                else :
                    print("Nice! You did it!")
                    input("Type any button to close...")
        elif var_pass == "Yes" :
            print("Unfair! You're cheating! You must be!")
            input("Type any button to close...")
        elif var_pass == "No" :
            print("Damn, guess second time's the charm, huh? Nicely done anyways")
            input("Type any button to close...")
    
        
