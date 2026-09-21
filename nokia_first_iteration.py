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


main_choice = int(input("\nEnter your choice: "))

if main_choice == 1:
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
        print("\n--- Options ---")
        print("1. Memory in use")
        print("2. Type of view")
        print("3. Memory status")

        options_choice = int(input("\nEnter your choice: "))

        if options_choice == 1: print("\nMemory in use")
        elif options_choice == 2: print("\nType of view")
        elif options_choice == 3: print("\nMemory status")
        else: print("\nInvalid choice")

    elif phone_book_choice == 10: print("\nSpeed dials")
    elif phone_book_choice == 11: print("\nVoice tags")
    else: print("\nInvalid choice")

elif main_choice == 2:
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

    messages_choice = int(input("\nEnter your choice: "))

    if messages_choice == 1: print("\nWrite messages")
    elif messages_choice == 2: print("\nInbox")
    elif messages_choice == 3: print("\nOutbox")
    elif messages_choice == 4: print("\nPicture messages")
    elif messages_choice == 5: print("\nTemplates")
    elif messages_choice == 6: print("\nSmileys")

    elif messages_choice == 7:
        print("\n--- Message Settings ---")
        print("1. Set")
        print("2. Common")

        message_settings_choice = int(input("\nEnter your choice: "))

        if message_settings_choice == 1:
            print("\n--- Set ---")
            print("1. Message centre number")
            print("2. Messages sent as")
            print("3. Messages validity")

            set_choice = int(input("\nEnter your choice: "))

            if set_choice == 1: print("\nMessage centre number")
            elif set_choice == 2: print("\nMessages sent as")
            elif set_choice == 3: print("\nMessages validity")
            else: print("\nInvalid choice")

        elif message_settings_choice == 2:
            print("\n--- Common ---")
            print("1. Delivery reports")
            print("2. Reply via same centre")
            print("3. Character support")

            common_choice = int(input("\nEnter your choice: "))

            if common_choice == 1: print("\nDelivery reports")
            elif common_choice == 2: print("\nReply via same centre")
            elif common_choice == 3: print("\nCharacter support")
            else: print("\nInvalid choice")

        else:
            print("\nInvalid choice")

    elif messages_choice == 8: print("\nInfo Service")
    elif messages_choice == 9: print("\nVoice mailbox number")
    elif messages_choice == 10: print("\nService command editor")
    else: print("\nInvalid choice")

elif main_choice == 3: print("\nChat")
elif main_choice == 4: print("\nCall Register")
elif main_choice == 5: print("\nTones")

elif main_choice == 6:
    print("\n--- Settings ---")
    print("1. Call Settings")
    print("2. Phone Settings")
    print("3. Security settings")
    print("4. Restore factory setting")

    settings_choice = int(input("\nEnter your choice: "))

    if settings_choice == 1:
        print("\n--- Call Settings ---")
        print("1. Automatic redial")
        print("2. Speed dialing")
        print("3. Call waiting options")
        print("4. Own number sending")
        print("5. Phone line in")
        print("6. Automatic answer")

        call_settings_choice = int(input("\nEnter your choice: "))

        if call_settings_choice == 1: print("\nAutomatic redial")
        elif call_settings_choice == 2: print("\nSpeed dialing")
        elif call_settings_choice == 3: print("\nCall waiting options")
        elif call_settings_choice == 4: print("\nOwn number sending")
        elif call_settings_choice == 5: print("\nPhone line in")
        elif call_settings_choice == 6: print("\nAutomatic answer")
        else: print("\nInvalid choice")

    elif settings_choice == 2:
        print("\n--- Phone Settings ---")
        print("1. Language")
        print("2. Cell info display")
        print("3. Welcome note")
        print("4. Network selection")
        print("5. Confirm SIM service actions")

        phone_settings_choice = int(input("\nEnter your choice: "))

        if phone_settings_choice == 1: print("\nLanguage")
        elif phone_settings_choice == 2: print("\nCell info display")
        elif phone_settings_choice == 3: print("\nWelcome note")
        elif phone_settings_choice == 4: print("\nNetwork selection")
        elif phone_settings_choice == 5: print("\nConfirm SIM service actions")
        else: print("\nInvalid choice")

    elif settings_choice == 3:
        print("\n--- Security Settings ---")
        print("1. PIN code request")
        print("2. Call barring service")
        print("3. Fixed dialling")
        print("4. Closed user group")
        print("5. Security level")
        print("6. Change access codes")

        security_choice = int(input("\nEnter your choice: "))

        if security_choice == 1: print("\nPIN code request")
        elif security_choice == 2: print("\nCall barring service")
        elif security_choice == 3: print("\nFixed dialling")
        elif security_choice == 4: print("\nClosed user group")
        elif security_choice == 5: print("\nSecurity level")
        elif security_choice == 6: print("\nChange access codes")
        else: print("\nInvalid choice")

    elif settings_choice == 4: print("\nRestore factory setting")
    else: print("\nInvalid choice")

elif main_choice == 7: print("\nCall Divert")

elif main_choice == 8:
    print("\n--- Music ---")
    print("1. Music player")
    print("2. Radio")
    print("3. Recorder")
    print("4. Tracklist")

    music_choice = int(input("\nEnter your choice: "))

    if music_choice == 1: print("\nMusic player")
    elif music_choice == 2: print("\nRadio")
    elif music_choice == 3: print("\nRecorder")
    elif music_choice == 4: print("\nTracklist")
    else: print("\nInvalid choice")

elif main_choice == 9: print("\nGames")
elif main_choice == 10: print("\nCalculator")
elif main_choice == 11: print("\nReminders")

elif main_choice == 12:
    print("\n--- Clock ---")
    print("1. Alarm clock")
    print("2. Clock settings")
    print("3. Date setting")
    print("4. Stopwatch")
    print("5. Countdown timer")
    print("6. Auto update date and time")

    clock_choice = int(input("\nEnter your choice: "))

    if clock_choice == 1: print("\nAlarm clock")
    elif clock_choice == 2: print("\nClock settings")
    elif clock_choice == 3: print("\nDate setting")
    elif clock_choice == 4: print("\nStopwatch")
    elif clock_choice == 5: print("\nCountdown timer")
    elif clock_choice == 6: print("\nAuto update date and time")
    else: print("\nInvalid choice")

elif main_choice == 13: print("\nProfiles")
elif main_choice == 14: print("\nServices")
elif main_choice == 15: print("\nSIM Services")

else:
    print("\nInvalid choice")