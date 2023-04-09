class UserInteraction:
    def PrintMainMenu():
        try:
            file = open("Programming.txt", "r")
            print("Please select one of the options:")
            print("1. Create")
            print("2. Read")
            print("3. Edit")
            print("4. Delete")
            print("5. Close the Program")

            userInput = int(input())

        except:
            userInput = 0

        if userInput == 1:
            Create.Creating()

        elif userInput == 2:
            Read.Reading()

        elif userInput == 3:
            Edit.Editing()

        elif userInput == 4:
            Delete.Deleting()

        elif userInput == 5:
            file.close()

        else:
            print("Please enter a valid input (1-5).")
            UserInteraction.PrintMainMenu()

    def Run():
        UserInteraction.PrintMainMenu()

class Create:
    def Creating():
        try: 
            with open("Programming.txt", "a") as file:
                userInput1 = input("Please enter the name of the book: ")    
                print("Please enter the book's ID number: ")
                
                try:
                    userInput2 = int(input())

                except:
                    userInput2 = 0

                if userInput2 > 0:
                    file.write(("\n" + str(userInput2) + " " + userInput1))
                    print("Successfully appended to the document!")
                    print("Press 1 to return to the main menu, or anything else to close the program. ")
                    try:
                        userInput = int(input())

                    except:
                        userInput = 0

                    if userInput == 1:
                        file.close()
                        UserInteraction.PrintMainMenu()

                    else:
                        file.close()

                else:
                    print("What you entered was not valid, please try again.")
                    file.close()
                    Create.Creating()
    
        except FileNotFoundError:
            print("File not found.")

        except PermissionError:
            print("Permission denied")

        except Exception as e:
            print(f"Error: {e}")
    

class Read:
    def Reading():
        try: 
            with open("Programming.txt", "r") as file:
                search = input("Please enter either the book name or ID: ")
                
                lines = file.readlines()
                
                for line in lines:
                    if line.find(search) != -1:
                        print(line)

                print("Press 1 to return to the main menu, or anything else to close the program.")

                try:
                    userInput = int(input())

                except:
                    userInput = 0

                if userInput == 1:
                    file.close()
                    UserInteraction.PrintMainMenu()

                else:
                    file.close()

        except FileNotFoundError:
            print("File not found.")

        except PermissionError:
            print("Permission denied")

        except Exception as e:
            print(f"Error: {e}")

class Edit:
    def Editing():
        try: 
            try:
                userInput1 = input("Please enter the ID followed by the name of the book you'd like to replace: ")
                userInput2 = input("Please enter the ID followed by the name of the book you'd like to add: ")

            except:
                userInput1 = 0
            
            if userInput1 != 0:

                with open("Programming.txt","r") as file:
                    search = userInput1
                    newline=[]

                    for search in file.readlines():        
                        newline.append(search.replace(userInput1, userInput2))

                with open("Programming.txt","w") as file:
                    for line in newline:
                        file.writelines(line)
                
                print("Successfully edited!")

                print("Press 1 to return to the main menu, or anything else to close the program.")

                try:
                    userInput = int(input())

                except:
                    userInput = 0

                if userInput == 1:
                    file.close()
                    UserInteraction.PrintMainMenu()

                else:
                    file.close()

            else:
                print("What you entered is not valid.")
                file.close()
                Edit.Editing()

        except FileNotFoundError:
            print("File not found.")

        except PermissionError:
            print("Permission denied")

        except Exception as e:
            print(f"Error: {e}")

class Delete:
    def Deleting():
        try: 
            with open("Programming.txt", "r") as file:
                lines = file.readlines()
            
            try:
                userInput1 = int(input("Please enter the ID of the book you'd like to delete: "))

            except:
                userInput1 = 0

            if userInput1 == 0:
                print("What you entered is invalid.")
                file.close()
                Delete.Deleting()

            else:
                try:
                    userInput2 = input("Please enter the name of the book you'd like to delete: ")

                except:
                    userInput2 = 0

                if userInput2 == 0:
                    print("What you entered is invalid.")
                    file.close()
                    Delete.Deleting()

                else:
                    with open("Programming.txt", "w") as file:
                        for line in lines:
                            if line.strip("\n") != (str(userInput1) + " " + userInput2):
                                file.write(line)

        except FileNotFoundError:
            print("File not found.")

        except PermissionError:
            print("Permission denied")

        except Exception as e:
            print(f"Error: {e}")

UserInteraction.Run()
