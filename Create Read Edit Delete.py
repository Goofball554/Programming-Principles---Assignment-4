#This class handles the main menu interaction with the user
class UserInteraction:
    def PrintMainMenu():
        try:
            #Prints the main menu and options for the user
            print("Please select one of the options:")
            print("1. Create")
            print("2. Read")
            print("3. Edit")
            print("4. Delete")
            print("5. Close the Program")

            #Asks the user for input
            userInput = int(input())

        #User does not input / inputs something valid
        except:
            userInput = 0

        #Takes the user to the Create menu
        if userInput == 1:
            Create.Creating()

        #Takes the user to the Read (Search) menu
        elif userInput == 2:
            Read.Reading()

        #Takes the user to the Edit menu
        elif userInput == 3:
            Edit.Editing()

        #Takes the user to the Delete menu
        elif userInput == 4:
            Delete.Deleting()

        #Ends the program
        elif userInput == 5:
            pass

        #The user did not enter a valid input, reprints the main menu
        else:
            print("Please enter a valid input (1-5).")
            UserInteraction.PrintMainMenu()

    #Runs the program
    def Run():
        UserInteraction.PrintMainMenu()

#This class handles the creating functionality
class Create:
    def Creating():
        try: 
            #Opens the file in apend mode
            with open("Programming.txt", "a") as file:
                
                #Asks the user for input
                userInput1 = input("Please enter the name of the book: ")    
                print("Please enter the book's ID number: ")
                
                #Checking for valid input
                try:
                    userInput2 = int(input())

                except:
                    userInput2 = 0

                if userInput2 > 0:
                    #Appends the information to the file
                    file.write(("\n" + str(userInput2) + " " + userInput1))
                    print("Successfully appended to the document!")

                    #Prompts the user to either return to the main menu or close the program
                    print("Press 1 to return to the main menu, or anything else to close the program. ")
                    
                    #Checking for valid input
                    try:
                        userInput = int(input())

                    except:
                        userInput = 0

                    if userInput == 1:
                        file.close()
                        UserInteraction.PrintMainMenu()

                    else:
                        file.close()

                #Prompts the user that what they entered is not valid
                else:
                    print("What you entered was not valid, please try again.")
                    file.close()
                    Create.Creating()
    
        #Handling the various possible errors
        except FileNotFoundError:
            print("File not found.")

        except PermissionError:
            print("Permission denied")

        except Exception as e:
            print(f"Error: {e}")
    
#This class handles the reading (searching) functionality
class Read:
    def Reading():
        try: 
            #Opens the file in read mode
            with open("Programming.txt", "r") as file:

                #Promps the user to input their search terms
                search = input("Please enter either the book name or ID: ")
                
                lines = file.readlines()
                
                #Searchs for the key terms in the file and prints if found
                for line in lines:
                    if line.find(search) != -1:
                        print(line)

                #Prompts the user to either return to the main menu or close the program
                print("Press 1 to return to the main menu, or anything else to close the program.")

                #Checking for valid input
                try:
                    userInput = int(input())

                except:
                    userInput = 0

                if userInput == 1:
                    file.close()
                    UserInteraction.PrintMainMenu()

                else:
                    file.close()

        #Handling the various possible errors
        except FileNotFoundError:
            print("File not found.")

        except PermissionError:
            print("Permission denied")

        except Exception as e:
            print(f"Error: {e}")

#This class handles the editing functionality
class Edit:
    def Editing():
        try: 
            try:
                #Promps the user for the ID and book name they want to replace and what to replace it with
                userInput1 = int(input("Please enter the ID the book you'd like to replace: "))
                userInput2 = input("Please enter the name of the book you'd like to replace: ")
                userInput3 = input("Please enter the name of the book you'd like to add: ")

            except:
                userInput1 = 0
            
            if userInput1 > 0:
                
                #Opens the file in read mode
                with open("Programming.txt","r") as file:
                    search = userInput1
                    newline=[]

                    #Copies the contents of the file, swapping the two inputs
                    for search in file.readlines():        
                        newline.append(search.replace(userInput2, userInput3))

                #Opens the file in write mode
                with open("Programming.txt","w") as file:

                    #Rewrites the new text into the file
                    for line in newline:
                        file.writelines(line)
                
                print("Successfully edited!")

                #Prompts the user to either return to the main menu or close the program
                print("Press 1 to return to the main menu, or anything else to close the program.")

                #Checking for valid input
                try:
                    userInput = int(input())

                except:
                    userInput = 0

                if userInput == 1:
                    file.close()
                    UserInteraction.PrintMainMenu()

                else:
                    file.close()

            #Promps the user that what they entered is not valid
            else:
                print("What you entered is not valid.")
                file.close()
                Edit.Editing()

        #Handling the various possible errors
        except FileNotFoundError:
            print("File not found.")

        except PermissionError:
            print("Permission denied")

        except Exception as e:
            print(f"Error: {e}")

#This class handles the deleting functionality
class Delete:
    def Deleting():
        try: 
            #Opens the program in read mode
            with open("Programming.txt", "r") as file:
                lines = file.readlines()
            
            try:
                #Asks the user for the ID of the book they'd like to delete
                userInput1 = int(input("Please enter the ID of the book you'd like to delete: "))

            except:
                userInput1 = 0

            #Promps the user that what they entered is invalid
            if userInput1 == 0:
                print("What you entered is invalid.")
                file.close()
                Delete.Deleting()

            else:
                try:
                    #Asks the user for the name of the book they'd like to delete
                    userInput2 = input("Please enter the name of the book you'd like to delete: ")

                except:
                    userInput2 = 0

                #Opens the file in write mode
                with open("Programming.txt", "w") as file:
                    for line in lines:
                        
                        #Removes the inputed text from the file
                        if line.strip("\n") != (str(userInput1) + " " + userInput2):
                            file.write(line)

        #Handling the various possible errors
        except FileNotFoundError:
            print("File not found.")

        except PermissionError:
            print("Permission denied")

        except Exception as e:
            print(f"Error: {e}")

#Runs the program upon starting
UserInteraction.Run()
