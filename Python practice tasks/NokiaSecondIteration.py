
main_menu_open = True

while main_menu_open:

    print("\n==============================")
    print("       NOKIA 5510")
    print("==============================")
    print("1. Phone Book")
    print("2. Messages")
    print("3. Chat")
    print("4. Call Register")
    print("5. Tones")
    print("6. Settings")
    print("7. Call Divert")
    print("8. Music")
    print("9. Games")
    print("10. Calculator")
    print("11. Reminders")
    print("12. Clock")
    print("13. Profiles")
    print("14. Services")
    print("15. SIM Services")
    print("99. Exit")

    main_choice = int(input("\nEnter your choice: "))

    if main_choice == 1:

        phone_book_open = True

        while phone_book_open:
            print("\n--- Phone Book ---")
            print("1. Search")
            print("2. Service Nos")
            print("3. Add name")
            print("4. Erase")
            print("5. Edit")
            print("6. Copy")
            print("7. Assign tone")
            print("8. Send b'card")
            print("9. Options")
            print("10. Speed dials")
            print("11. Voice tags")
            print("0. Back")

            phone_book_choice = int(input("\nEnter your choice: "))

            if phone_book_choice == 1: print("\nSearch")
            elif phone_book_choice == 2: print("\nService Nos")
            elif phone_book_choice == 3: print("\nAdd name")
            elif phone_book_choice == 4: print("\nErase")
            elif phone_book_choice == 5: print("\nEdit")
            elif phone_book_choice == 6: print("\nCopy")
            elif phone_book_choice == 7: print("\nAssign tone")
            elif phone_book_choice == 8: print("\nSend b'card")

            elif phone_book_choice == 9:

                options_open = True

                while options_open:
                    print("\n--- Options ---")
                    print("1. Memory in use")
                    print("2. Type of view")
                    print("3. Memory status")
                    print("0. Back")

                    options_choice = int(input("\nEnter your choice: "))

                    if options_choice == 1: print("\nMemory in use")
                    elif options_choice == 2: print("\nType of view")
                    elif options_choice == 3: print("\nMemory status")
                    elif options_choice == 0:
                        options_open = False
                        print("\nGoing back to Phone Book...")
                    else: print("\nInvalid choice")

            elif phone_book_choice == 10: print("\nSpeed dials")
            elif phone_book_choice == 11: print("\nVoice tags")
            elif phone_book_choice == 0:
                phone_book_open = False
                print("\nGoing back to Main Menu...")
            else: print("\nInvalid choice")

    elif main_choice == 2:

        messages_open = True

        while messages_open:
            print("\n--- Messages ---")
            print("1. Write messages")
            print("2. Inbox")
            print("3. Outbox")
            print("4. Picture messages")
            print("5. Templates")
            print("6. Smileys")
            print("7. Message settings")
            print("8. Info Service")
            print("9. Voice mailbox number")
            print("10. Service command editor")
            print("0. Back")

            messages_choice = int(input("\nEnter your choice: "))

            if messages_choice == 1: print("\nWrite messages")
            elif messages_choice == 2: print("\nInbox")
            elif messages_choice == 3: print("\nOutbox")
            elif messages_choice == 4: print("\nPicture messages")
            elif messages_choice == 5: print("\nTemplates")
            elif messages_choice == 6: print("\nSmileys")

            elif messages_choice == 7:

                message_settings_open = True

                while message_settings_open:
                    print("\n--- Message Settings ---")
                    print("1. Set")
                    print("2. Common")
                    print("0. Back")

                    message_settings_choice = int(input("\nEnter your choice: "))

                    if message_settings_choice == 1:

                        set_open = True

                        while set_open:
                            print("\n--- Set ---")
                            print("1. Message centre number")
                            print("2. Messages sent as")
                            print("3. Messages validity")
                            print("0. Back")

                            set_choice = int(input("\nEnter your choice: "))

                            if set_choice == 1: print("\nMessage centre number")
                            elif set_choice == 2: print("\nMessages sent as")
                            elif set_choice == 3: print("\nMessages validity")
                            elif set_choice == 0:
                                set_open = False
                                print("\nGoing back to Message Settings...")
                            else: print("\nInvalid choice")

                    elif message_settings_choice == 2:

                        common_open = True

                        while common_open:
                            print("\n--- Common ---")
                            print("1. Delivery reports")
                            print("2. Reply via same centre")
                            print("3. Character support")
                            print("0. Back")

                            common_choice = int(input("\nEnter your choice: "))

                            if common_choice == 1: print("\nDelivery reports")
                            elif common_choice == 2: print("\nReply via same centre")
                            elif common_choice == 3: print("\nCharacter support")
                            elif common_choice == 0:
                                common_open = False
                                print("\nGoing back to Message Settings...")
                            else: print("\nInvalid choice")

                    elif message_settings_choice == 0:
                        message_settings_open = False
                        print("\nGoing back to Messages...")
                    else: print("\nInvalid choice")

            elif messages_choice == 8: print("\nInfo Service")
            elif messages_choice == 9: print("\nVoice mailbox number")
            elif messages_choice == 10: print("\nService command editor")
            elif messages_choice == 0:
                messages_open = False
                print("\nGoing back to Main Menu...")
            else: print("\nInvalid choice")

    elif main_choice == 3: print("\nChat")
    elif main_choice == 4: print("\nCall Register")
    elif main_choice == 5: print("\nTones")

    elif main_choice == 6:

        settings_open = True

        while settings_open:
            print("\n--- Settings ---")
            print("1. Call Settings")
            print("2. Phone Settings")
            print("3. Security settings")
            print("4. Restore factory setting")
            print("0. Back")

            settings_choice = int(input("\nEnter your choice: "))

            if settings_choice == 1:

                call_settings_open = True

                while call_settings_open:
                    print("\n--- Call Settings ---")
                    print("1. Automatic redial")
                    print("2. Speed dialing")
                    print("3. Call waiting options")
                    print("4. Own number sending")
                    print("5. Phone line in")
                    print("6. Automatic answer")
                    print("0. Back")

                    call_settings_choice = int(input("\nEnter your choice: "))

                    if call_settings_choice == 1: print("\nAutomatic redial")
                    elif call_settings_choice == 2: print("\nSpeed dialing")
                    elif call_settings_choice == 3: print("\nCall waiting options")
                    elif call_settings_choice == 4: print("\nOwn number sending")
                    elif call_settings_choice == 5: print("\nPhone line in")
                    elif call_settings_choice == 6: print("\nAutomatic answer")
                    elif call_settings_choice == 0:
                        call_settings_open = False
                        print("\nGoing back to Settings...")
                    else: print("\nInvalid choice")

            elif settings_choice == 2:

                phone_settings_open = True

                while phone_settings_open:
                    print("\n--- Phone Settings ---")
                    print("1. Language")
                    print("2. Cell info display")
                    print("3. Welcome note")
                    print("4. Network selection")
                    print("5. Confirm SIM service actions")
                    print("0. Back")

                    phone_settings_choice = int(input("\nEnter your choice: "))

                    if phone_settings_choice == 1: print("\nLanguage")
                    elif phone_settings_choice == 2: print("\nCell info display")
                    elif phone_settings_choice == 3: print("\nWelcome note")
                    elif phone_settings_choice == 4: print("\nNetwork selection")
                    elif phone_settings_choice == 5: print("\nConfirm SIM service actions")
                    elif phone_settings_choice == 0:
                        phone_settings_open = False
                        print("\nGoing back to Settings...")
                    else: print("\nInvalid choice")

            elif settings_choice == 3:

                security_open = True

                while security_open:
                    print("\n--- Security Settings ---")
                    print("1. PIN code request")
                    print("2. Call barring service")
                    print("3. Fixed dialling")
                    print("4. Closed user group")
                    print("5. Security level")
                    print("6. Change access codes")
                    print("0. Back")

                    security_choice = int(input("\nEnter your choice: "))

                    if security_choice == 1: print("\nPIN code request")
                    elif security_choice == 2: print("\nCall barring service")
                    elif security_choice == 3: print("\nFixed dialling")
                    elif security_choice == 4: print("\nClosed user group")
                    elif security_choice == 5: print("\nSecurity level")
                    elif security_choice == 6: print("\nChange access codes")
                    elif security_choice == 0:
                        security_open = False
                        print("\nGoing back to Settings...")
                    else: print("\nInvalid choice")

            elif settings_choice == 4: print("\nRestore factory setting")
            elif settings_choice == 0:
                settings_open = False
                print("\nGoing back to Main Menu...")
            else: print("\nInvalid choice")

    elif main_choice == 7: print("\nCall Divert")

    elif main_choice == 8:

        music_open = True

        while music_open:
            print("\n--- Music ---")
            print("1. Music player")
            print("2. Radio")
            print("3. Recorder")
            print("4. Tracklist")
            print("0. Back")

            music_choice = int(input("\nEnter your choice: "))

            if music_choice == 1: print("\nMusic player")
            elif music_choice == 2: print("\nRadio")
            elif music_choice == 3: print("\nRecorder")
            elif music_choice == 4: print("\nTracklist")
            elif music_choice == 0:
                music_open = False
                print("\nGoing back to Main Menu...")
            else: print("\nInvalid choice")

    elif main_choice == 9: print("\nGames")
    elif main_choice == 10: print("\nCalculator")
    elif main_choice == 11: print("\nReminders")

    elif main_choice == 12:

        clock_open = True

        while clock_open:
            print("\n--- Clock ---")
            print("1. Alarm clock")
            print("2. Clock settings")
            print("3. Date setting")
            print("4. Stopwatch")
            print("5. Countdown timer")
            print("6. Auto update date and time")
            print("0. Back")

            clock_choice = int(input("\nEnter your choice: "))

            if clock_choice == 1: print("\nAlarm clock")
            elif clock_choice == 2: print("\nClock settings")
            elif clock_choice == 3: print("\nDate setting")
            elif clock_choice == 4: print("\nStopwatch")
            elif clock_choice == 5: print("\nCountdown timer")
            elif clock_choice == 6: print("\nAuto update date and time")
            elif clock_choice == 0:
                clock_open = False
                print("\nGoing back to Main Menu...")
            else: print("\nInvalid choice")

    elif main_choice == 13: print("\nProfiles")
    elif main_choice == 14: print("\nServices")
    elif main_choice == 15: print("\nSIM Services")

    elif main_choice == 99:
        main_menu_open = False
        print("\nNokia 5510 shutting down...")

    else:
        print("\nInvalid choice")
