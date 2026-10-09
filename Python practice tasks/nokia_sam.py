def phone_book():
	 print("""
--- Phone Book ---
1. Search
2. Service Nos
3. Add name
4. Erase
5. Edit
6. Copy
7. Assign tone
8. Send b'card
9. Options
10. Speed dials
11. Voice tags
00. Home
0. Back""")

            phone_book_choice = input("\nEnter your choice: ")
		match phone_book_choice:

			case 1: print("\nSearch") break
			case 2: print("\nService Nos") break
			case 3: print("\nAdd name") break
			case 4: print("\nErase") break
			case 5: pprint("\nEdit") break
			case 6: print("\nCopy") break 
			case 7: print("\nAssign tone") break
			case 8: print("\nSend b'card") break
			case 9:  options_open = True
main_menu_open = True
going_home = False


def go_home():
    print("\nGoing back to Main Menu...")
    return True


while main_menu_open:

    going_home = False

    print("""
==============================
       NOKIA 5510
==============================
1. Phone Book
2. Messages
3. Chat
4. Call Register
5. Tones
6. Settings
7. Call Divert
8. Music
9. Games
10. Calculator
11. Reminders
12. Clock
13. Profiles
14. Services
15. SIM Services""")

    main_choice = input("\nEnter your choice: ")

    if main_choice == "1":

        phone_book_open = True

        while phone_book_open and not going_home:
           phone_book()



               

                while options_open and not going_home:
                    print("""
--- Options ---
1. Memory in use
2. Type of view
3. Memory status
00. Home
0. Back""")

                    options_choice = input("\nEnter your choice: ")

			match options_choice:

			case 1: print("\nMemory in use") break
			case 2: print("\nType of view") break
			case 3: print("\nMemory status") break
			case 4: print("\nErase") break
			case 5: pprint("\nEdit") break
			case 6: print("\nCopy") break 
			case 7: print("\nAssign tone") break
			case 8: print("\nSend b'card") break
			case 9:  options_open = True


                    if options_choice == "1": print("\nMemory in use")
                    elif options_choice == "2": print("\nType of view")
                    elif options_choice == "3": print("\nMemory status")
                    elif options_choice == "00": going_home = go_home()
                    elif options_choice == "0":
                        options_open = False
                        print("\nGoing back to Phone Book...")
                    else: print("\nInvalid choice")

            elif phone_book_choice == "10": print("\nSpeed dials")
            elif phone_book_choice == "11": print("\nVoice tags")
            elif phone_book_choice == "00": going_home = go_home()
            elif phone_book_choice == "0":
                phone_book_open = False
                print("\nGoing back to Main Menu...")
            else: print("\nInvalid choice")

    elif main_choice == "2":

        messages_open = True

        while messages_open and not going_home:
            print("""
--- Messages ---
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info Service
9. Voice mailbox number
10. Service command editor
00. Home
0. Back""")

            messages_choice = input("\nEnter your choice: ")

		match messages_choice:

			case 1: print("\nWrite messages") break
			case 2: print("\nInbox") break
			case 3: print("\nOutbox") break
			case 4: print("\nPicture messages") break
			case 5: print("\nTemplates") break
			case 6: print("\nSmileys") break 
			case 7: options_open = True




            if messages_choice == "1": print("\nWrite messages")
            elif messages_choice == "2": print("\nInbox")
            elif messages_choice == "3": print("\nOutbox")
            elif messages_choice == "4": print("\nPicture messages")
            elif messages_choice == "5": print("\nTemplates")
            elif messages_choice == "6": print("\nSmileys")

            elif messages_choice == "7":

                message_settings_open = True

                while message_settings_open and not going_home:
                    print("""
--- Message Settings ---
1. Set
2. Common
00. Home
0. Back""")

                    message_settings_choice = input("\nEnter your choice: ")

                    if message_settings_choice == "1":

                        set_open = True

                        while set_open and not going_home:
                            print("""
--- Set ---
1. Message centre number
2. Messages sent as
3. Messages validity
00. Home
0. Back""")

                            set_choice = input("\nEnter your choice: ")

				

                            if set_choice == "1": print("\nMessage centre number")
                            elif set_choice == "2": print("\nMessages sent as")
                            elif set_choice == "3": print("\nMessages validity")
                            elif set_choice == "00": going_home = go_home()
                            elif set_choice == "0":
                                set_open = False
                                print("\nGoing back to Message Settings...")
                            else: print("\nInvalid choice")

                    elif message_settings_choice == "2":

                        common_open = True

                        while common_open and not going_home:
                            print("""
--- Common ---
1. Delivery reports
2. Reply via same centre
3. Character support
00. Home
0. Back""")

                            common_choice = input("\nEnter your choice: ")

                            if common_choice == "1": print("\nDelivery reports")
                            elif common_choice == "2": print("\nReply via same centre")
                            elif common_choice == "3": print("\nCharacter support")
                            elif common_choice == "00": going_home = go_home()
                            elif common_choice == "0":
                                common_open = False
                                print("\nGoing back to Message Settings...")
                            else: print("\nInvalid choice")

                    elif message_settings_choice == "00": going_home = go_home()
                    elif message_settings_choice == "0":
                        message_settings_open = False
                        print("\nGoing back to Messages...")
                    else: print("\nInvalid choice")

            elif messages_choice == "8": print("\nInfo Service")
            elif messages_choice == "9": print("\nVoice mailbox number")
            elif messages_choice == "10": print("\nService command editor")
            elif messages_choice == "00": going_home = go_home()
            elif messages_choice == "0":
                messages_open = False
                print("\nGoing back to Main Menu...")
            else: print("\nInvalid choice")

    elif main_choice == "3": print("\nChat")
    elif main_choice == "4": print("\nCall Register")
    elif main_choice == "5": print("\nTones")

    elif main_choice == "6":

        settings_open = True

        while settings_open and not going_home:
            print("""
--- Settings ---
1. Call Settings
2. Phone Settings
3. Security settings
4. Restore factory setting
00. Home
0. Back""")

            settings_choice = input("\nEnter your choice: ")

            if settings_choice == "1":

                call_settings_open = True

                while call_settings_open and not going_home:
                    print("""
--- Call Settings ---
1. Automatic redial
2. Speed dialing
3. Call waiting options
4. Own number sending
5. Phone line in
6. Automatic answer
00. Home
0. Back""")

                    call_settings_choice = input("\nEnter your choice: ")

                    if call_settings_choice == "1": print("\nAutomatic redial")
                    elif call_settings_choice == "2": print("\nSpeed dialing")
                    elif call_settings_choice == "3": print("\nCall waiting options")
                    elif call_settings_choice == "4": print("\nOwn number sending")
                    elif call_settings_choice == "5": print("\nPhone line in")
                    elif call_settings_choice == "6": print("\nAutomatic answer")
                    elif call_settings_choice == "00": going_home = go_home()
                    elif call_settings_choice == "0":
                        call_settings_open = False
                        print("\nGoing back to Settings...")
                    else: print("\nInvalid choice")

            elif settings_choice == "2":

                phone_settings_open = True

                while phone_settings_open and not going_home:
                    print("""
--- Phone Settings ---
1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Confirm SIM service actions
00. Home
0. Back""")

                    phone_settings_choice = input("\nEnter your choice: ")

                    if phone_settings_choice == "1": print("\nLanguage")
                    elif phone_settings_choice == "2": print("\nCell info display")
                    elif phone_settings_choice == "3": print("\nWelcome note")
                    elif phone_settings_choice == "4": print("\nNetwork selection")
                    elif phone_settings_choice == "5": print("\nConfirm SIM service actions")
                    elif phone_settings_choice == "00": going_home = go_home()
                    elif phone_settings_choice == "0":
                        phone_settings_open = False
                        print("\nGoing back to Settings...")
                    else: print("\nInvalid choice")

            elif settings_choice == "3":

                security_open = True

                while security_open and not going_home:
                    print("""
--- Security Settings ---
1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Security level
6. Change access codes
00. Home
0. Back""")

                    security_choice = input("\nEnter your choice: ")

                    if security_choice == "1": print("\nPIN code request")
                    elif security_choice == "2": print("\nCall barring service")
                    elif security_choice == "3": print("\nFixed dialling")
                    elif security_choice == "4": print("\nClosed user group")
                    elif security_choice == "5": print("\nSecurity level")
                    elif security_choice == "6": print("\nChange access codes")
                    elif security_choice == "00": going_home = go_home()
                    elif security_choice == "0":
                        security_open = False
                        print("\nGoing back to Settings...")
                    else: print("\nInvalid choice")

            elif settings_choice == "4": print("\nRestore factory setting")
            elif settings_choice == "00": going_home = go_home()
            elif settings_choice == "0":
                settings_open = False
                print("\nGoing back to Main Menu...")
            else: print("\nInvalid choice")

    elif main_choice == "7": print("\nCall Divert")

    elif main_choice == "8":

        music_open = True

        while music_open and not going_home:
            print("""
--- Music ---
1. Music player
2. Radio
3. Recorder
4. Tracklist
00. Home
0. Back""")

            music_choice = input("\nEnter your choice: ")

            if music_choice == "1": print("\nMusic player")
            elif music_choice == "2": print("\nRadio")
            elif music_choice == "3": print("\nRecorder")
            elif music_choice == "4": print("\nTracklist")
            elif music_choice == "00": going_home = go_home()
            elif music_choice == "0":
                music_open = False
                print("\nGoing back to Main Menu...")
            else: print("\nInvalid choice")

    elif main_choice == "9": print("\nGames")
    elif main_choice == "10": print("\nCalculator")
    elif main_choice == "11": print("\nReminders")

    elif main_choice == "12":

        clock_open = True

        while clock_open and not going_home:
            print("""
--- Clock ---
1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update date and time
00. Home
0. Back""")

            clock_choice = input("\nEnter your choice: ")

            if clock_choice == "1": print("\nAlarm clock")
            elif clock_choice == "2": print("\nClock settings")
            elif clock_choice == "3": print("\nDate setting")
            elif clock_choice == "4": print("\nStopwatch")
            elif clock_choice == "5": print("\nCountdown timer")
            elif clock_choice == "6": print("\nAuto update date and time")
            elif clock_choice == "00": going_home = go_home()
            elif clock_choice == "0":
                clock_open = False
                print("\nGoing back to Main Menu...")
            else: print("\nInvalid choice")

    elif main_choice == "13": print("\nProfiles")
    elif main_choice == "14": print("\nServices")
    elif main_choice == "15": print("\nSIM Services")

    else:
        print("\nInvalid choice")