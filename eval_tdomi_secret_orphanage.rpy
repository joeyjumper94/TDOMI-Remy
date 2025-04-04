#You're proably wondering: Why does this exist? Why did Eval just copy paste the other orphanage minigame into a new file?
#In short, it would take WAY to many if/else statements to keep both games in the same file, since a ton of dialogue changes take place.
#For code clarity and to make my life 100x easier, I made them different files.

#It is very possible that I add an item tracker somewhere down the line. Sounds like a good idea to me

#This is where all of the orphanage stuff will take place to keep the main block of code from being *too* long
#Basic ideas:
    #Remy basically becomes your servant while you fix up an orphanage. Simple enough, right?
    #Don't make it as annoying as the ECK Anna paper writing game. I'm sorry, but that was not fun

    #The amount you can do at the orphanage is determined by the time you spend on certain activities. Each activity will have ~3 possible activites
    #Each task can be done at any time, and have a set solution
    #Some tasks have red herrings. There will be clues as to what are things you must do.
    #You need to send Remy off to do tasks to complete certain solutions to issues and must wait for him to return
    
    #How many total activities? Let's see how much more I can take of this random branching stuff. I already did SO much for the katsu game...

    #First order of business - Fix the lights. You have 3 options. Replace the bulbs, reset the circuit breaker, or fix the lightswitch
        #For the bulbs, you must send Remy off to the storage room to grab more bulbs
    #Then you need to fix the broken desk. You have options. Apply DWD-40 (Dragon Water Displacement-40), fix the legs of the desk

#Organized List of Items:
#    Supply Closet:
#        Lightbulbs - 1 action
#        Replacement Switch - 2 Actions
#        DWD-40 (Dragon Water Displacement-40) - 1 action
#    Shed:
#        Tools - 1 action
#        Small Spare Parts - 2 actions
#        Large Spare Parts - 3 actions
#        Ladder - 1 action
#    Main Office:
#        Children's folders - 1 action
#        Circuit Breaker - 2 actions
#        Cleaning Spray - 1 action
#
#All possible actions and outcomes:
#    Lights:
#        Replace bulbs - Requires lightbulbs and ladder. Progress + 1
#        Reset circuit breaker - Requires circuit breaker. Progress + 1
#        Replace light switch - Requires light switch. No progress
#    Desk:
#        Apply DWD-40 - Requires DWD-40. Progress + 1
#        Fix desk leg - Requires small spare parts and tools. Progress + 1
#        Fix desk seat - Requires large spare parts and tools. No progress
#    Organize books:
#        Pick up books - No requirements. Progress + 1
#        Fix crumpled pages - No requirements. Progress + 1
#        Sort books - No requirements. Progress + 1
#    Sort through papers:
#        Sort the hatchlings' drawings - Need children's files. Progress + 1
#        Go through paperwork - Need Remy present. Progress + 1
#        Fold newspaper - No requirements. Progress + 1
#    Do some cleaning:
#        Clean the walls - Requires cleaning spray. Progress + 1
#        Clean the desks - Requires cleaning spray. Progress + 1
#        Clean the whiteboard - Requires cleaning spray. Progress + 1

#Maybe use config.menu_include_disabled for this minigame. Just make sure to disable it again later

#Variables and display stuff - COUNT MINUTES BY 15!!!! - It's possible I want to make these more specific to the orphanage
#if I make another mod

#By the way self. The issue is that for everything excpet the lights, the completion condition has to come before the remy returning
#code since that is skipping the completion sequence. The reason it works for lights is because the completion sequence is located within the main game
label eval_secret_orphanage_game_init:
    $ evalVaraGone = False
    $ evalRemyAsksAboutVara = False
    $ evalVaraSnack = False
    $ evalRemyGoneWhileSnack = False
    $ evalCrackersConsumed = 0
    $ evalVaraHasSnack = False

    #Show ECK's extra info display
    show screen evalextrainfo
    $ evalextradisplay = 3

    jump eval_secret_orphanage_game

#And... game time!
label eval_secret_orphanage_game:
    #Complete the game if the player has done all 5 tasks
    if evalTasksComplete == 5:
        m "I took one last look around the room."
        m "It looks like we had finished just about everything we could."
        if evalRemyOnMission:
            c "I think we're all finished, Vara!"
            m "I brought my palm close to Vara."
            c "High five?"
            m "She looked at my hand curiously before pushing her head into it."
            m "I rubbed her head."
            c "I appreciate the effort, but for a high five, you have to open your claw and slap mine."
            c "Open up your claw, I'll show you."
            Vr smnone "..."
            play sound "fx/lighthighfive.mp3"
            m "Vara tentatively stretched her claw in my direction. I lightly hit it with my palm."
            show vara smsmile with dissolvemed
            m "She recoiled on impact, but after a moment of consideration, smiled."
            Vr smnormal "My turn."
            play sound "fx/goodhighfive.mp3"
            m "I stretched my palm and Vara hit my palm. Her claws made it a bit painful, but nothing intolerable."
            c "As high fives go, that was quite impressive."
            show remy normal behind vara
            show amely smnormal
            with easeinright
            Ry "We're back!"
            c "Oh hey, Remy. We just finished up."
            Vr "I learned a high five!"
            Ry look "What's a high five?"
            c "You really don't know?"
            show remy normal behind vara with dissolvemed
            m "I led Remy through the process of a high five."
            play sound "fx/goodhighfive.mp3"
            m "By the end, Remy had become a master at high fiving."
            Ry look "No wonder I didn't understand what a high five was."
            Ry normal "I don't have five claws."
            c "You know, I didn't even think about that."
            Ry smile "We might have to rename it if we start doing this more often."
            Am "Me next!"
            show remy normal behind vara with dissolvemed
            play sound "fx/goodhighfive.mp3"
            m "Quickly running through the process again, Amely was also a great high fiver."
            Am "Fun!"
        else:
            c "I think we're all finished! High five, guys!"
            show remy look with dissolvemed
            $ renpy.pause (1.5)
            Ry "High five?"
            c "You don't know what that is?"
            Ry "Can't say I do."
            c "Well, in simple terms, we hit our palms, or claws, together to make a slapping noise."
            c "Put your claw out, I'll show you."
            play sound "fx/goodhighfive.mp3"
            m "Remy outstretched his claw, and I gave it a clean hit with my palm."
            Ry normal "Interesting. Why do people high five?"
            c "It's a little congratulatory celebration for good collaboration."
            Ry "And why is it a high {i}five{/i}?"
            c "Well, it's named after the fact that humans have five fingers. But since dragon species have varying amounts of digits, we might need to consider renaming it."
            Ry "I see."
            Am "I try?"
            c "Sure, Amely."
            play sound "fx/goodhighfive.mp3"
            m "I stretched out my arm, and the little dragon gave it a nice slap with her claw."
            c "Nice!"
            Am "Yay!"
            Vr smnone "Me?"
            play sound "fx/lighthighfive.mp3"
            m "I reached out to Vara with an outstretched palm. She tentatively gave my hand a light hit."
            c "You can do it harder, Vara. It doesn't hurt me, I promise."
            Vr "Okay."
            play sound "fx/goodhighfive.mp3"
            m "Vara tried again with more force, generating a nice slap."
            c "Wow! That was a great high five, Vara!"
            Vr smnormal "Thanks."
        m "Remy glanced at the room."
        $ evalOrphanageScore = 2
        jump eval_secret_orphanage_end
    
    #Complete the game if the player runs out of time
    elif evalRemainingMinutes <= 0:
        $ evalDisplayVar1 = 0
        if evalRemyOnMission:
            show remy normal behind vara
            show amely smnormal
            with easeinright
            if evalMinutesRemyIsGone > 0:
                Ry "I came back early as soon as I noticed the time. Adine should be here any minute, [player_name]."
            else:
                Ry "Adine should be here any minute, [player_name]."
        else:
            Ry "Adine should be here any minute, [player_name]."
        c "But we aren't done!"
        if evalTasksComplete > 3:
            Ry smile "We still did quite a lot in one day. Don't worry, Adine and I can finish the rest in the next few days."
            $ evalOrphanageScore = 1
        else:
            Ry look "Don't worry, Adine and I can finish the rest in the next few days."
            $ evalOrphanageScore = 0
        jump eval_secret_orphanage_end
    
    #Update the display
    $ evalDisplayVar1name = "Remaining Time:"
    $ evalDisplayVar1 = evalRemainingMinutes
    $ evalDisplayVar1unit = " mins"

    if evalMinutesRemyIsGone > 0:
        $ evalDisplayVar2name = "Remy returns in"
        $ evalDisplayVar2 = evalMinutesRemyIsGone
        $ evalDisplayVar2unit = " mins"
    else:
        $ evalDisplayVar2name = "Remy is here!"
        $ evalDisplayVar2 = ""
        $ evalDisplayVar2unit = ""

    $ evalDisplayVar3name = "Tasks Completed:"
    $ evalDisplayVar3 = evalTasksComplete
    $ evalDisplayVar3unit = ""

    #Show Remy when he returns and give the player their item
    if evalRemyOnMission and evalMinutesRemyIsGone <= 0:
        show amely smnormal with easeinright
        if evalVaraGone:
            show remy normal behind amely with easeinright
        else:
            show remy normal behind vara with easeinright
        if evalRemyItem != "circuit breaker":
            Ry "We're back with the [evalRemyItem], [player_name]!"
            if evalLightsOnWithoutRemy: #Remy acknowledges that the lights have come back on if he was gone
                Ry "Oh hey! You got the lights working! Nice job, [player_name]!"
                Am "Lights!"
                $ evalLightsOnWithoutRemy = False
        else: #Handles special case where task isn't completed with an item
            Ry "We reset the circuit breaker, [player_name]!"
            $ evalResetBreaker = True
            $ evalRemyOnMission = False
            if evalReplaceBulbs and evalResetBreaker:
                $ evalTasksComplete += 1
                $ evalDisplayVar3 = evalTasksComplete
                play sound "fx/lightswitch.mp3"
                $ renpy.pause (1.5)
                scene evalorphlight
                if not evalRemyOnMission:
                    show remy normal behind vara
                    if not evalVaraGone:
                        show vara smnormal behind amely
                    show amely smnormal
                else:
                    if not evalVaraGone:
                        show vara smnormal
                    $ evalLightsOnWithoutRemy = True
                c "Let there be light!"
                if not evalRemyOnMission:
                    Ry smile "Nice job, [player_name]! Now we can see!"
                    Am "Light!"
        c "Thanks, Remy!"
        if evalVaraGone and not evalRemyAsksAboutVara:
            Ry look "Wait, where's Vara?"
            c "She said she would be back. She's making us something."
            Ry normal "Oh, well now I'm excited. I wonder what she's going to do."
            $ evalRemyAsksAboutVara = True
        $ evalGatheredItems.append(evalRemyItem)
        $ evalRemyOnMission = False
    #Remy warning if he is idling
    elif evalMinutesRemyIsGone <= 0: #This probably deserves a bit of variation
        if not evalJustAteCracker:
            Ry normal "Amely and I are here if you need anything, [player_name]."

#Stuff for Vara's snack
    if evalRemainingMinutes <= 205 and not evalVaraGone and not evalVaraHasSnack:
        if evalRemyOnMission:
            $ evalRemyAsksAboutVara = True
            Vr smsmile "Stay here, I will make a surprise."
            c "Okay, Vara."
            show vara smsmile flip with dissolvemed
            hide vara with easeoutright
            m "Vara left the room and went into the back of the orphanage."
            m "I wonder what the surprise is going to be."
        else:
            Vr smsmile "I will go make a surprise."
            Ry "A surprise?"
            Vr "Yes."
            Ry "Well, go ahead, Vara."
            show vara smsmile flip with dissolvemed
            hide vara with easeoutright
            Ry smile "I guess you've lost your little helper for a while."
            c "I'll make do."
            $ evalRemyAsksAboutVara = True #This just makes sure he doesn't ask where Vara is later
        $ evalVaraHasSnack = True
        $ evalVaraGone = True
    
    if evalRemainingMinutes <= 175 and evalVaraGone:
        $ evalVaraGone = False
        $ evalVaraSnack = True
        Vr "I'm back!"
        show vara smnormal behind amely with easeinright
        m "Vara walked into the room balancing a large helping of cheese, crackers, and jam on her head."
        c "Oh! Let me help you with that, Vara."
        m "I lifted the plate off her head and set it on a nearby desk."
        if evalRemyOnMission:
            $ evalRemyGoneWhileSnack = True
            c "This looks delicious, Vara!"
            Vr "For all of us!"
            m "She took a knife off the plate and used it to cut a small chunk of cheese and place it on a cracker."
            c "(Oh my goodness, the little dragon has a knife again.)"
            m "She then took a small spoonful of the jam and rested it on the cheese."
            play sound "fx/pizzabite2.ogg"
            m "She put the whole cracker in her mouth and bit down."
            Vr "Yum!"
            Vr "You can have too!"
            c "Thank you, Vara!"
        else:
            c "This looks delicious, Vara!"
            Vr "For all of us!"
            m "She took a knife off the plate and used it to cut a small chunk of cheese and place it on a cracker."
            c "(Oh my goodness, the little dragon has a knife again.)"
            m "She then took a small spoonful of the jam and rested it on the cheese."
            play sound "fx/pizzabite2.ogg"
            m "She put the whole cracker in her mouth and bit down."
            Vr "Yum!"
            Vr "You can have too!"
            Ry "I think I'll take you up on that offer, Vara."
            m "Remy repeated the process, but this time with extra cheese."
            play sound "fx/pizzabite2.ogg"
            $ renpy.pause (1.0)
            Ry smile "This is exactly what I needed, Vara. I didn't even notice how hungry I was."
            Am "Hungry too!"
            Ry normal "Let me get you some, Amely."
            Vr "No, I will."
            m "Vara made another cracker and handed it to Amely."
            play sound "fx/pizzabite.ogg"
            $ renpy.pause (1.0)
            Am "Good!"
        Vr "You have some, [player_name]?"
        c "Maybe I will."
        

    #What the player should ask in the menu
    if evalRemainingMinutes == 15:
        $ evalWhatNextText = "(What should we work on first?)"
    elif evalRemainingMinutes > 5:
        $ evalWhatNextText = "(What should we work on next?)"
    else:
        $ evalWhatNextText = "(We're running out of time. What should we work on next?)"
    
    #Deciding whether the player should ask Remy to fetch an item or work on a task
    menu:
        c "(What should I try to do?)"

        "Ask Remy to get something." if not evalRemyOnMission:
            jump eval_secret_orphanage_remy_item_gather
        
        "Work on tasks.":
            pass
        
        "Eat Vara's snack." if evalVaraSnack:
            $ evalCrackersConsumed += 1
            if evalCrackersConsumed == 1:
                m "I made myself a cracker and put it into my mouth."
            else:
                m "I made myself another cracker and put it into my mouth."
            play sound "fx/pizzabite.ogg"
            $ renpy.pause (1.0)
            if evalCrackersConsumed == 30:
                m "My body would not let me swallow it. I was forced to spit it out on the floor."
                Vr smshocked "..."
                stop music fadeout 2.0
                hide screen evalextrainfo
                scene black with dissolvemed
                m "Then, everything went black."
                play sound "fx/impact3.ogg"
                jump eval_too_many_crackers
            elif evalCrackersConsumed >= 27:
                m "I could fell a raging turmoil in my stomach, I could just manage to swallow the cracker."
            elif evalCrackersConsumed >= 18:
                m "I was starting to feel sick, I should have stopped eating a while ago."
            elif evalCrackersConsumed >= 12:
                m "I was starting to get full. Maybe I should stop."
            elif evalCrackersConsumed > 1:
                m "It still tasted great, and my stomach was feeling less empty."
            else:
                m "It was amazing. I didn't realize just how hungry I was."
                c "Wow, Vara! This is wonderful."
                Vr "Thank you!"

            $ evalRemainingMinutes -= 5
            if evalRemyOnMission:
                $ evalMinutesRemyIsGone -= 5
            $ evalJustAteCracker = True
            jump eval_secret_orphanage_game

        "Wait.":
            if evalRemyOnMission:
                c "(I should wait for Remy to get back.)"
            else:
                c "(I should take a quick break.)"
            $ evalRemainingMinutes -= 15
            if evalRemyOnMission:
                $ evalMinutesRemyIsGone -= 15
            jump eval_secret_orphanage_game

    #Deciding which task to work on
    $ evalJumpFromMain = True
    menu:
        c "[evalWhatNextText]"
        
        "Fix the lights." if not evalReplaceBulbs or not evalResetBreaker:
            jump eval_secret_orphanage_fix_lights
        
        "Fix the desk." if not evalApplyDWD or not evalFixLeg:
            jump eval_secret_orphanage_fix_desk
        
        "Organize the books." if not evalPickUpBooks or not evalUncrumplePages or not evalSortBooks: #Add conditionals here
            jump eval_secret_orphanage_organize_books
        
        "Sort through papers." if not evalHatchlingArt or not evalPaperwork or not evalFoldNewspaper: #Add conditionals here
            jump eval_secret_orphanage_sort_papers
        
        "Do some cleaning." if not evalCleanWalls or not evalCleanDesks or not evalCleanWhiteboard: #Add conditionals here
            jump eval_secret_orphanage_clean
        
        "[[Go back]":
            jump eval_secret_orphanage_game

label eval_secret_orphanage_remy_item_gather:
    c "Could you grab something for me, Remy?"
    Ry "Sure! Where from?"

    label eval_secret_orphanage_reselect_gather_area:
        menu:
            "Supply Closet." if "lightbulbs" not in evalGatheredItems or "lightswitch" not in evalGatheredItems or "DWD-40" not in evalGatheredItems:

                menu:
                    "Lightbulbs." if "lightbulbs" not in evalGatheredItems:
                        $ evalRemyItem = "lightbulbs"
                        $ evalMinutesRemyIsGone = 15
                        $ evalRemyOnMission = True
                        c "I think we should get some lightbulbs to replace the broken lights."
                        Ry "Sounds like a good idea. Let's go, Amely!"
                        Am "Light!"
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                        Ry "Whoah! Wait for me, Amely!"
                        show remy normal flip behind vara with dissolvemed
                        hide remy with easeoutright

                    "Replacement Lightswitch." if "lightswitch" not in evalGatheredItems:
                        $ evalRemyItem = "lightswitch"
                        $ evalMinutesRemyIsGone = 30
                        $ evalRemyOnMission = True
                        c "We should try replacing the lightswitch with a new one."
                        Ry "Good idea, [player_name]! I didn't think of that possibility."
                        show remy normal flip behind vara with dissolvemed
                        hide remy with easeoutright
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                    
                    "DWD-40." if "DWD-40" not in evalGatheredItems:
                        $ evalRemyItem = "DWD-40"
                        $ evalMinutesRemyIsGone = 15
                        $ evalRemyOnMission = True
                        c "We should grab some WD-40. That stuff always comes in handy."
                        Ry look "Do you mean DWD-40?"
                        c "What does that even stand for?"
                        Ry normal "Dragon Water Displacement 40, obviously."
                        c "(I guess that's what the WD stands for.)"
                        show remy normal flip behind vara with dissolvemed
                        hide remy with easeoutright
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                    
                    "[[Go Back]":
                        jump eval_secret_orphanage_reselect_gather_area
                
                jump eval_secret_orphanage_game

            "Shed." if "tools" not in evalGatheredItems or "small spare parts" not in evalGatheredItems or "large spare parts" not in evalGatheredItems or "ladder" not in evalGatheredItems:

                menu:
                    "Tools." if "tools" not in evalGatheredItems:
                        $ evalRemyItem = "tools"
                        $ evalMinutesRemyIsGone = 15
                        $ evalRemyOnMission = True
                        c "Would you mind getting some tools? That sounds like it'll come in handy."
                        Ry "Sure thing! Come on Amely!"
                        show remy normal flip behind vara with dissolvemed
                        hide remy with easeoutright
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                    
                    "Small Spare Parts." if "small spare parts" not in evalGatheredItems:
                        $ evalRemyItem = "small spare parts"
                        $ evalMinutesRemyIsGone = 30
                        $ evalRemyOnMission = True
                        c "I think we should grab some small spare parts."
                        Ry "Good idea! We're on it, right Amely?"
                        Am "Yes!"
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                        show remy normal flip behind vara with dissolvemed
                        hide remy with easeoutright
                    
                    "Large Spare Parts." if "large spare parts" not in evalGatheredItems:
                        $ evalRemyItem = "large spare parts"
                        $ evalMinutesRemyIsGone = 45
                        $ evalRemyOnMission = True
                        c "We should probably get a few large parts to replace any odds or ends."
                        Ry "This might take a second, those parts are heavy!"
                        show remy normal flip behind vara with dissolvemed
                        hide remy with easeoutright
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                    
                    "Ladder." if "ladder" not in evalGatheredItems:
                        $ evalRemyItem = "ladder"
                        $ evalMinutesRemyIsGone = 15
                        $ evalRemyOnMission = True
                        c "I think a ladder would be beneficial."
                        Ry "One ladder coming right {i}up{/i}!"
                        c "I see what you did there..."
                        Ry smile "There's a lot more where that came from."
                        c "Oh no."
                        show remy normal flip behind vara with dissolvemed
                        hide remy with easeoutright
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                    
                    "[[Go Back]":
                        jump eval_secret_orphanage_reselect_gather_area
                
                jump eval_secret_orphanage_game
            
            "Main Office." if "folders" not in evalGatheredItems or "circuit breaker" not in evalGatheredItems or "cleaning spray" not in evalGatheredItems:

                menu:
                    "Hatchlings' folders" if "folders" not in evalGatheredItems:
                        $ evalRemyItem = "folders"
                        $ evalMinutesRemyIsGone = 15
                        $ evalRemyOnMission = True
                        c "Why don't we sort through the hatchlings' things?"
                        Ry "Sounds good to me, let me grab their folders for you."
                        show remy normal flip behind vara with dissolvemed
                        hide remy with easeoutright
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                    
                    "Circuit breaker." if "circuit breaker" not in evalGatheredItems:
                        $ evalRemyItem = "circuit breaker"
                        $ evalMinutesRemyIsGone = 30
                        $ evalRemyOnMission = True
                        c "Actually, instead of grabbing something, could you try resetting the circuit breaker?"
                        Ry "Good idea! I didn't think about that."
                        show remy normal flip behind vara with dissolvemed
                        hide remy with easeoutright
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                    
                    "Cleaning spray." if "cleaning spray" not in evalGatheredItems:
                        $ evalRemyItem = "cleaning spray"
                        $ evalMinutesRemyIsGone = 15
                        $ evalRemyOnMission = True
                        c "Let's grab some cleaning spray so we can work on cleaning the walls."
                        Ry look "A lot of those scribbles have been there for years."
                        Ry normal "It'll be nice to finally clean them off."
                        show remy normal flip behind vara with dissolvemed
                        hide remy with easeoutright
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                    
                    "[[Go Back]":
                        jump eval_secret_orphanage_reselect_gather_area
                    
                jump eval_secret_orphanage_game

            "[[Go back]":
                jump eval_secret_orphanage_game
            
                                        
label eval_secret_orphanage_fix_lights:
    #A bunch of code to increase continuity and kill bugs
    if evalRemyOnMission and evalMinutesRemyIsGone == 0:
        if evalReplaceBulbs and evalResetBreaker:
            $ evalTasksComplete += 1
            $ evalDisplayVar3 = evalTasksComplete
            $ renpy.pause (1.5)
            play sound "fx/lightswitch.mp3"
            scene evalorphlight
            show vara smnormal
            if not evalRemyOnMission:
                show remy normal behind vara
                show vara smnormal behind amely
                show amely smnormal
            else:
                $ evalLightsOnWithoutRemy = True
            c "Let there be light!"
            if not evalRemyOnMission:
                Ry smile "Nice job, [player_name]! Now we can see!"
                Am "Light!"
        jump eval_secret_orphanage_game
    elif evalMinutesRemyIsGone > 0:
        $ evalDisplayVar2name = "Remy returns in"
        $ evalDisplayVar2 = evalMinutesRemyIsGone
        $ evalDisplayVar2unit = " mins"

    $ evalDisplayVar1 = evalRemainingMinutes

    if evalJumpFromMain:
        m "I walked over to the lightswitch."
        $ evalJumpFromMain = False
    else:
        m "I walked back over to the lightswitch."

    #Handle completion of the lights
    if evalReplaceBulbs and evalResetBreaker:
        $ evalTasksComplete += 1
        $ evalDisplayVar3 = evalTasksComplete
        $ renpy.pause (1.5)
        play sound "fx/lightswitch.mp3"
        scene evalorphlight
        show vara smnormal
        if not evalRemyOnMission:
            show remy normal behind vara
            show vara smnormal behind amely
            show amely smnormal
        else:
            $ evalLightsOnWithoutRemy = True
            if evalVaraGone:
                c "Let there be light!"
            else:
                c "We got the lights on, Vara. Nice job."
                Vr "..."
        if not evalRemyOnMission:
            Ry smile "Nice job, [player_name]! Now we can see!"
            if not evalVaraGone:
                Vr "And me!"
                Ry smile "Yes, and you too, Vara."
            Am "Light!"
        jump eval_secret_orphanage_game

    play sound "fx/lightswitch.mp3"
    $ renpy.pause (1.0)
    m "The lights are busted, but the switch seems intact."
    
    menu:
        c "(What should I try fixing?)"

        "Replace the lightbulbs." if not evalReplaceBulbs:
            if "lightbulbs" in evalGatheredItems and "ladder" in evalGatheredItems:
                $ evalRemainingMinutes -= 15
                if evalRemyOnMission:
                    $ evalMinutesRemyIsGone -= 15
                $ evalReplaceBulbs = True
                play sound "fx/lightscrewunscrew.mp3"
                m "One by one, I walked up to each bulb, placed down the ladder, and reinstalled the lightbulbs."
                if not evalVaraGone:
                    Vr smnone "Safe?"
                    c "Don't worry, Vara, this ladder is very safe."
                    m "Seemingly worried, she rested her front claws on the bottom to support it."
                    c "Thanks, Vara. Better safe than sorry."
                    show vara smnormal with dissolvemed
                $ renpy.pause (1.0)
                play sound "fx/lightswitch.mp3"
                jump eval_secret_orphanage_fix_lights
            elif "lightbulbs" in evalGatheredItems and "ladder" not in evalGatheredItems:
                m "I need a ladder to reach the lights."
                jump eval_secret_orphanage_game
            elif "lightbulbs" not in evalGatheredItems and "ladder" in evalGatheredItems:
                m "I can reach the lights, but I have nothing to replace them with."
                jump eval_secret_orphanage_game
            else:
                m "I need some way to reach the lights and something to replace them with."
                jump eval_secret_orphanage_game
        
        "Reset the circuit breaker." if not evalResetBreaker:
            m "It would be a good idea to reset the circuit breaker, but I have no idea where it is."
            if not evalVaraGone:
                c "Vara, do you know where the circuit breaker is?"
                m "Vara shook her head."
            if evalRemyOnMission:
                m "Maybe Remy could do that for me."
            else:
                if evalVaraGone:
                    m "I should ask Remy to do that for me."
                else:
                    Ry "I know where it is, [player_name]. Is there something you would like to do with it?"
            jump eval_secret_orphanage_game
        
        "Replace the lightswitch." if not evalReplaceSwitch:
            if "lightswitch" in evalGatheredItems:
                $ evalRemainingMinutes -= 15
                if evalRemyOnMission:
                    $ evalMinutesRemyIsGone -= 15
                $ evalReplaceSwitch = True
                play sound "fx/rummage.wav"
                m "I quickly replaced the lightswitch with the one Remy had given me."
                play sound "fx/lightswitch.mp3"
                m "Doesn't look like it did anything."
                jump eval_secret_orphanage_fix_lights
            else:
                m "I need a new lightswitch if I'm going to replace the old one."
                jump eval_secret_orphanage_game
        
        "[[Go Back]":
            jump eval_secret_orphanage_game

label eval_secret_orphanage_fix_desk:
    #Handle completion of the desk
    if evalApplyDWD and evalFixLeg:
        if evalVaraGone:
            m "I sat back down at the desk Remy said was broken."
        else:
            c "Vara why don't you try the desk out now?"
            m "Vara sat at the desk Remy said was broken."
        m "It seemed perfectly fine now. It no longer made hideous squeaking noises and didn't rock when she moved around."
        $ evalTasksComplete += 1
        $ evalDisplayVar3 = evalTasksComplete
        jump eval_secret_orphanage_game
        if not evalRemyOnMission:
            if evalVaraGone:
                Ry "Now I won't be tormented by those horrible squeaks. Nice going, [player_name]."
            else:
                Ry "Now I won't be tormented by those horrible squeaks. Nice going, you two."
            c "Thanks!"
        jump eval_secret_orphanage_game
    
    #A bunch of code to increase continuity and kill bugs
    if evalRemyOnMission and evalMinutesRemyIsGone == 0:
        jump eval_secret_orphanage_game
    elif evalMinutesRemyIsGone > 0:
        $ evalDisplayVar2name = "Remy returns in"
        $ evalDisplayVar2 = evalMinutesRemyIsGone
        $ evalDisplayVar2unit = " mins"
    
    $ evalDisplayVar1 = evalRemainingMinutes

    if evalJumpFromMain:
        m "I sat down at the desk Remy said was broken."
        $ evalJumpFromMain = False
    else:
        m "I sat back down at the desk Remy said was broken."

    #Handle hints as to what is wrong with the desk
    if not evalApplyDWD and not evalFixLeg:  
        play sound "fx/chairsqueak.mp3"
        $ renpy.pause (1.0)
        m "The desk rocked so violently that I almost fell off."
        if not evalVaraGone:
            Vr smshocked "..."
            c "Don't worry, Vara. I'm fine."
            show vara smnormal with dissolvemed
        m "Like Remy said, one of the legs had been partially dissolved."
    elif not evalApplyDWD and evalFixLeg:
        play sound "fx/chairsqueak.mp3"
        $ renpy.pause (1.0)
        if evalVaraGone:
            m "That sounds horrible."
        else:
            Vr smnone "Ow! My ears."
            c "That does sound quite awful, doesn't it."
            Vr smnormal "We will fix."
    elif evalApplyDWD and not evalFixLeg:
        m "The desk rocked so violently that I almost fell off."
        m "Like Remy said, one of the legs had been partially dissolved."
        if not evalVaraGone:
            Vr smshocked "..."
            c "Don't worry, Vara. I'm fine."
            show vara smnormal with dissolvemed
    
    #Handle player fix options
    menu:
        c "(What should I try fixing?)"

        "Apply lubricant." if not evalApplyDWD:
            if "DWD-40" in evalGatheredItems:
                $ evalRemainingMinutes -= 15
                if evalRemyOnMission:
                    $ evalMinutesRemyIsGone -= 15
                $ evalApplyDWD = True
                play sound "fx/DWDspray.mp3"
                m "I gave the desk a quick coat of DWD-40."
                if not evalVaraGone:
                    Vr "I try?"
                    c "Sure, why not?"
                    m "I handed the can of DWD-40 to Vara."
                    play sound "fx/DWDspray.mp3"
                    m "She awkwardly positioned the can in her claws and gave a small spot on the desk a very healthy coating of the spray."
                    Vr "Fixed!"
                jump eval_secret_orphanage_fix_desk
            else:
                m "I need some sort of lubricant to stop the squeaking."
                jump eval_secret_orphanage_game
        
        "Fix the desk leg." if not evalFixLeg:
            if "small spare parts" in evalGatheredItems and "tools" in evalGatheredItems:
                $ evalRemainingMinutes -= 15
                if evalRemyOnMission:
                    $ evalMinutesRemyIsGone -= 15
                $ evalFixLeg = True
                if not evalVaraGone:
                    c "Vara, do you see a new desk leg anywhere in that pile of parts?"
                    Vr "Yes!"
                    show vara smnormal flip with dissolvemed
                    hide vara with easeoutright
                    m "She grabbed a long metal desk leg from the pile and returned to me."
                    if evalRemyOnMission:
                        show vara smnormal with easeinright
                    else:
                        show vara smnormal behind amely with easeinright
                    Vr "Here."
                    c "Thank you, Vara."
                play sound "fx/screwin.mp3"
                m "I quickly replaced the melted desk leg with a new one."
                jump eval_secret_orphanage_fix_desk
            elif "small spare parts" in evalGatheredItems and "tools" not in evalGatheredItems:
                m "I have the new desk leg, but I need tools to install it."
                jump eval_secret_orphanage_game
            elif "small spare parts" not in evalGatheredItems and "tools" in evalGatheredItems:
                m "I have some tools, but I also need a replacement desk leg. I think it's pretty small as well."
                jump eval_secret_orphanage_game
            else:
                m "I need tools and a replacement desk leg to fix this. The legs look quite small."
                jump eval_secret_orphanage_game
        
        "Fix the desk seat." if not evalFixSeat:
            if "large spare parts" in evalGatheredItems and "tools" in evalGatheredItems:
                $ evalRemainingMinutes -= 15
                if evalRemyOnMission:
                    $ evalMinutesRemyIsGone -= 15
                $ evalFixSeat = True
                if not evalVaraGone:
                    m "I went to get a desk seat from the pile of extra pieces, but I couldn't find one."
                    c "Vara, did you happen to see an extra seat lying around here somewhere?"
                    Vr "Maybe..."
                    c "Where?"
                    m "I looked over to Vara, who was happily sitting on the extra seat."
                    c "Could I get that, Vara?"
                    Vr "It's comfortable."
                    c "Please?"
                    Vr "Fine."
                play sound "fx/screwin.mp3"
                m "I replaced the desk seat with a new one."
                m "I'm not too sure that accomplished much."
                jump eval_secret_orphanage_fix_desk
            elif "large spare parts" in evalGatheredItems and "tools" not in evalGatheredItems:
                m "I have a seat to replace the old one, but I also need tools to install it."
                jump eval_secret_orphanage_game
            elif "large spare parts" not in evalGatheredItems and "tools" in evalGatheredItems:
                m "I have tools, but I need a replacement seat for the desk. I's quite a large piece."
                jump eval_secret_orphanage_game
            else:
                m "I need tools and a replacement for the desk seat. The desk seat is decently large."
                jump eval_secret_orphanage_game
        
        "[[Go Back]":
            jump eval_secret_orphanage_game

label eval_secret_orphanage_organize_books:
    #Handle completion of book organization
    if evalPickUpBooks and evalUncrumplePages and evalSortBooks: #yyy
        if evalVaraGone:
            m "I walked a few steps back and admired my work."
        else:
            m "I walked a few steps back and admired our work."
        $ evalTasksComplete += 1
        $ evalDisplayVar3 = evalTasksComplete
        $ renpy.pause (2.0)
        m "Everything looked perfect. The books were neatly stacked on the shelves."
        if not evalRemyOnMission:
            Ry smile "You did a great job organizing those books, [player_name]!"
            if persistent.c1booksort:
                c "Well, I've already had plenty of practice in the library."
                Ry normal "I almost forgot about that!" #This is a bit ugly might want to change later
        jump eval_secret_orphanage_game

    #A bunch of code to increase continuity and kill bugs
    if evalRemyOnMission and evalMinutesRemyIsGone == 0:
        jump eval_secret_orphanage_game
    elif evalMinutesRemyIsGone > 0:
        $ evalDisplayVar2name = "Remy returns in"
        $ evalDisplayVar2 = evalMinutesRemyIsGone
        $ evalDisplayVar2unit = " mins"
    
    $ evalDisplayVar1 = evalRemainingMinutes

    if evalJumpFromMain:
        m "I looked at the bookshelf at the back of the room." #Might want to dumb this down to maintain coherence when jumping back to this label
        $ evalJumpFromMain = False
    else:
        if evalVaraGone:
            m "I walked a few steps back and admired my work."
        else:
            m "I walked a few steps back and admired our work."

    #Really fun if/elif/else chain to portray how the books look
    if not evalPickUpBooks and not evalUncrumplePages and not evalSortBooks: #nnn
        m "The books were strewn across the floor, their pages wrinkled."
    elif not evalPickUpBooks and not evalUncrumplePages and evalSortBooks: #nny
        m "The books were neatly sorted on the ground, their pages somewhat wrinkled."
    elif not evalPickUpBooks and evalUncrumplePages and evalSortBooks: #nyy
        m "The books were neatly sorted on the ground, with only faint wrinkles showing on their pages."
    elif evalPickUpBooks and not evalUncrumplePages and not evalSortBooks: #ynn
        m "The books rested on the shelves in no particular order and had wrinkled pages."
    elif evalPickUpBooks and evalUncrumplePages and not evalSortBooks: #yyn
        m "The books rested on the shelves in no particular order."
    elif evalPickUpBooks and not evalUncrumplePages and evalSortBooks: #yny
        m "The books were neatly sorted on the shelves. However, their pages still looked wrinkled."
    elif not evalPickUpBooks and evalUncrumplePages and not evalSortBooks: #nyn
        m "The books lay strewn across the floor, their pages freshly unwrinkled."
    
    menu:
        c "(What should I do with the books?)"

        "Pick up the books." if not evalPickUpBooks:
            $ evalRemainingMinutes -= 15
            if evalRemyOnMission:
                $ evalMinutesRemyIsGone -= 15
            $ evalPickUpBooks = True
            play sound "fx/rummage3.ogg"
            m "I started picking up the books and rested them on the shelves."
            if not evalVaraGone:
                m "Vara contributed as well. While she couldn't reach the upper shelves, she filed books into the lower ones."
            jump eval_secret_orphanage_organize_books
        
        "Fix crumpled pages." if not evalUncrumplePages:
            $ evalRemainingMinutes -= 15
            if evalRemyOnMission:
                $ evalMinutesRemyIsGone -= 15
            $ evalUncrumpleProgress += 1
            if evalUncrumpleProgress == 2:
                play sound "fx/paper2.ogg"
                m "I finished uncrumpling the pages of the last few books."
                $ evalUncrumplePages = True
            else:
                play sound "fx/paper2.ogg"
                m "I started removing the wrinkles from the books' pages."
                play sound "fx/paper2.ogg"
                m "This was going to take longer than I expected."
            jump eval_secret_orphanage_organize_books
        
        "Sort the books." if not evalSortBooks:
            $ evalRemainingMinutes -= 15
            if evalRemyOnMission:
                $ evalMinutesRemyIsGone -= 15
            $ evalSortBooks = True
            play sound "fx/placebook.mp3"
            if persistent.c1booksort:
                if evalPickUpBooks:
                    m "Just like I had at the library, I organized the books on the shelf."
                else:
                    m "Just like I had at the library, I organized the books on the floor."
            else:
                if evalPickUpBooks:
                    m "I organized the books on the shelf in alphabetical order."
                else:
                    m "I organized the books on the floor in alphabetical order."
                c "(Not sure if this is how I should do it, but it should be fine.)"
            if not evalVaraGone:
                m "Vara laid down next to me with a disinterested expression."
            jump eval_secret_orphanage_organize_books
        
        "[[Go Back]":
            jump eval_secret_orphanage_game

label eval_secret_orphanage_sort_papers:
    #Handle completion of paper sorting.
    if evalHatchlingArt and evalPaperwork and evalFoldNewspaper:
        if evalVaraGone:
            m "I stood back and took a look at my work."
        else:
            m "I stood back and took a look at our work."
        $ evalTasksComplete += 1
        $ evalDisplayVar3 = evalTasksComplete
        m "All of the papers were properly sorted, and the hatchlings' artwork was safe in their respective folders."
        m "The newspaper was also folded and ready for another art project."
        if not evalRemyOnMission:
            $ evalAmelyPicture = False
            Ry smile "I can't remember the last time this desk ever looked this clean!"
            c "Oh, Remy. Look what I found!"
            m "I showed him Amely's drawing."
            m "Amely must have seen it as well."
            Am "Give Remy."
            Ry "A gift for me, Amely? Thanks!"
            m "Remy took the drawing and looked at it for a long time before slipping it under his wing."
            Ry "Wow, Amely, this looks really good!"
            Am "Thanks!"
            #Is it possible I actually draw something for this? Maybe :) Or ask the creator of the Remy Hatchlings mod
        jump eval_secret_orphanage_game

    #A bunch of code to increase continuity and kill bugs
    if evalRemyOnMission and evalMinutesRemyIsGone == 0:
        jump eval_secret_orphanage_game
    elif evalMinutesRemyIsGone > 0:
        $ evalDisplayVar2name = "Remy returns in"
        $ evalDisplayVar2 = evalMinutesRemyIsGone
        $ evalDisplayVar2unit = " mins"

    $ evalDisplayVar1 = evalRemainingMinutes

    if evalJumpFromMain:
        m "I glanced at the papers on the large desk at the front of the room."
        $ evalJumpFromMain = False
    else:
        if evalVaraGone:
            m "I stood back and took a look at my work."
        else:
            m "I stood back and took a look at our work."
    
    #Portraying how the papers look. Once again, this will not be fun
    if not evalHatchlingArt and not evalPaperwork and not evalFoldNewspaper:
        m "The desk was littered with papers of all sorts, ranging from important documents to crayon drawings."
        m "There was also newspaper crammed into one of the lower drawers. Probably for art projects."
    elif not evalHatchlingArt and not evalPaperwork and evalFoldNewspaper:
        m "The desk was covered in papers ranging from important documents to crayon drawings."
        m "However, the newspaper was folded neatly in the bottom drawer."
    elif not evalHatchlingArt and evalPaperwork and evalFoldNewspaper:
        m "I had managed to sort through all of the important documents and pile them neatly."
        m "The newspapers were also neatly folded in the desk drawer."
        m "However, the hatchlings' artwork still lay haphazardly on the table."
    elif evalHatchlingArt and not evalPaperwork and not evalFoldNewspaper:
        m "The artwork that had littered the table was now correctly sorted into the hatchlings' folders."
        m "However, the documents and newspaper still lay untouched."
    elif evalHatchlingArt and evalPaperwork and not evalFoldNewspaper:
        m "The papers on the top of the desk were completely organized."
        m "However, the newspaper in the lower drawer still lay crumpled."
    elif evalHatchlingArt and not evalPaperwork and evalFoldNewspaper:
        m "The hatchlings' artwork was properly sorted and the newspaper in the bottom drawer was folded nicely."
        m "However, I still had to go through the many important documents."
    elif not evalHatchlingArt and evalPaperwork and not evalFoldNewspaper:
        m "The important documents were neatly stacked and sorted on the desk."
        m "However, the hatchlings' artwork lay untouched, and the newspaper was still crammed tightly in a lower drawer."
    
    menu:
        c "(What should I do with the papers?)"

        "Sort the hatchlings' drawings." if not evalHatchlingArt:
            if "folders" in evalGatheredItems:
                $ evalRemainingMinutes -= 15
                if evalRemyOnMission:
                    $ evalMinutesRemyIsGone -= 15
                $ evalHatchlingArt = True
                play sound "fx/pages.ogg"
                m "It was quite simple sorting through the hatchlings' art."
                m "Some of the art was also quite impressive."
                m "Wait, what's this? A drawing of Remy by Amely? I should keep this."
                $ evalAmelyPicture = True
                m "Finishing up, I noticed that Vara's folder was completely empty."
                if evalVaraGone:
                    m "She must not like drawing."
                else:
                    c "Where is your art, Vara?"
                    Vr "Drawing is boring. I cook."
                jump eval_secret_orphanage_sort_papers
            else:
                m "I need something to organize this artwork in."
                m "Maybe there's some folders the hatchlings keep their art in?"
                jump eval_secret_orphanage_game
        
        "Sort the important documents." if not evalPaperwork:
            $ evalRemainingMinutes -= 15
            if evalRemyOnMission:
                $ evalMinutesRemyIsGone -= 15
            $ evalPaperwork = True
            play sound "fx/pages.ogg"
            m "I sorted through the important documents at a reasonable pace."
            m "Not sure how exactly to organize them, I based my assumptions off of brief glances at the content."
            m "There's a surprising lack of adoption forms here. How sad."
            jump eval_secret_orphanage_sort_papers
        
        "Fold the newspaper." if not evalFoldNewspaper:
            $ evalRemainingMinutes -= 15
            if evalRemyOnMission:
                $ evalMinutesRemyIsGone -= 15
            $ evalFoldNewspaper = True
            play sound "fx/pages.ogg"
            if evalVaraGone:
                m "I quickly smoothed out the newspaper and folded it nicely."
            else:
                m "I quickly smoothed out the newspaper and folded it nicely on a desk."
                Vr "They go here."
                m "Vara took some of the newspaper in her mouth and put it in a drawer at the front of the room."
                Vr smnone "Ew, paper tastes gross."
            m "Once finished, the paper was neatly organized in the drawer."
            show vara smnormal with dissolvemed
            jump eval_secret_orphanage_sort_papers
        
        "[[Go Back]":
            jump eval_secret_orphanage_game

label eval_secret_orphanage_clean:
    #Handle completion of the room cleaning
    if evalCleanWalls and evalCleanDesks and evalCleanWhiteboard:
        if evalVaraGone:
            m "I looked back at what I had just cleaned."
        else:
            m "I looked back at what we had just cleaned."
        $ evalTasksComplete += 1
        $ evalDisplayVar3 = evalTasksComplete
        m "Everything was spotless. The walls no longer bore the mark of the hatchlings and the desks shined."
        if not evalRemyOnMission:
            Ry "Wow, [player_name]! This looks wonderful!"
            c "How long do you think it'll stay like this?"
            Ry smile "Give the hatchlings a week. It'll be destroyed again by then."
        jump eval_secret_orphanage_game

    #A bunch of code to increase continuity and kill bugs
    if evalRemyOnMission and evalMinutesRemyIsGone == 0:
        jump eval_secret_orphanage_game
    elif evalMinutesRemyIsGone > 0:
        $ evalDisplayVar2name = "Remy returns in"
        $ evalDisplayVar2 = evalMinutesRemyIsGone
        $ evalDisplayVar2unit = " mins"

    $ evalDisplayVar1 = evalRemainingMinutes

    if evalJumpFromMain:
        m "I looked around the room."
        $ evalJumpFromMain = False
    else:
        m "I looked back at what we had just cleaned."
    
    #Handle how the room looks. WHY DO I DO THIS TO MYSELF
    if not evalCleanWalls and not evalCleanDesks and not evalCleanWhiteboard:
        m "The walls, desks, and whiteboard were a complete mess."
    elif not evalCleanWalls and not evalCleanDesks and evalCleanWhiteboard:
        m "The walls and desks still bore the scars of countless crayons and markers."
        m "The whiteboard, on the other hand, sparkled like new."
    elif not evalCleanWalls and evalCleanDesks and evalCleanWhiteboard:
        m "The desks and the whiteboard shone like new."
        m "The walls, however, were still covered in crayon."
    elif evalCleanWalls and not evalCleanDesks and not evalCleanWhiteboard:
        m "The room looked much nicer without the crayon scribbles on the wall."
        m "However, the desks and whiteboard were still dirty."
    elif evalCleanWalls and evalCleanDesks and not evalCleanWhiteboard:
        m "The walls and desk were devoid of crayon and marker scribbles."
        m "The whiteboard, on the other hand, still needed a good cleaning."
    elif evalCleanWalls and not evalCleanDesks and not evalCleanWhiteboard:
        m "The walls and whiteboard looked brand new."
        m "The desks, however, still bore the scars of a thousand markers."
    elif not evalCleanWalls and evalCleanDesks and not evalCleanWhiteboard:
        m "The desks looked like they were almost brand new."
        m "However, the whiteboard and walls were still a mess."
    
    menu:
        c "(What do I clean?)"

        "Clean the walls" if not evalCleanWalls:
            if "cleaning spray" in evalGatheredItems:
                $ evalRemainingMinutes -= 15
                if evalRemyOnMission:
                    $ evalMinutesRemyIsGone -= 15
                $ evalCleanWalls = True
                play sound "fx/spraybottle.mp3"
                m "Using the cleaning spray, I wiped the crayon markings off the wall."
                jump eval_secret_orphanage_clean
            else:
                m "I need some cleaning spray if I'm going to get these crayon markings off the wall."
                jump eval_secret_orphanage_game
        
        "Clean the desks." if not evalCleanDesks:
            if "cleaning spray" in evalGatheredItems:
                $ evalRemainingMinutes -= 15
                if evalRemyOnMission:
                    $ evalMinutesRemyIsGone -= 15
                $ evalCleanDesks = True
                play sound "fx/spraybottle.mp3"
                m "Using the cleaning spray, I wiped down the desks."
                m "The crayon and marker stains seemed to lift right off of the wood."
                jump eval_secret_orphanage_clean
            else:
                m "I need some cleaning spray if I'm going to clean off these desks."
                jump eval_secret_orphanage_game
        
        "Clean the whiteboard." if not evalCleanWhiteboard:
            if "cleaning spray" in evalGatheredItems:
                $ evalRemainingMinutes -= 15
                if evalRemyOnMission:
                    $ evalMinutesRemyIsGone -= 15
                $ evalCleanWhiteboard = True
                play sound "fx/spraybottle.mp3"
                m "Using the cleaning spray, I wiped the marker residue off of the whiteboard."
                jump eval_secret_orphanage_clean
            else:
                m "I need some cleaning spray if I'm going to clean the whiteboard."
                jump eval_secret_orphanage_game
        
        "[[Go Back]":
            jump eval_secret_orphanage_game

label eval_secret_orphanage_end: #Change the music
    hide screen evalextrainfo
    stop music fadeout 2.0
    $ renpy.pause (3.0)
    if evalOrphanageScore == 2:
        play music "mx/comfy.mp3"
        Ry smile "Wow, [player_name]! This place hasn't looked this good in years!"
        Ry "It was definitely worthy of a couple high fives."
        Ry look "We really need to think about changing the name of that, though."
        c "Couldn't have done it without you and our two little helpers."
        Am "Yay! I help!"
        m "Vara gave an embarrassed smile."
        Ry normal "Well. It looks like we still have a bit of time to kill."
        Ry "Is there anything else you would like to do?"
        c "That was exhausting, I think I'm too tired to do anything else."
        if evalRemainingMinutes > 30:
            Ry look "I forgot that you aren't as strong as you usually are."
            Ry normal "How about you three take a nap together. The hatchlings look like they could use some sleep as well."
            Am smsad "No!"
            Vr smgrowl "Not tired!"
            m "Amely then let out a huge yawn."
            m "In response, Vara herself also yawned."
            Am smnormal "Maybe..."
            Vr smnormal "Fine..."
            c "Where should we sleep? On the floor?"
            Ry "You guys can sleep on me if you like."
            c "Oh boy, my very own full sized dragon pillow equipped with a built-in heater!"
            Ry smile "I'm the latest model."
            m "I carefully propped myself up against Remy's side. I could feel his body rising and falling with each breath."
            m "Amely then crawled up next to me and laid her head on my shoulder."
            Am smnormal "Goodnight."
            m "In an instant, the little dragon was fast asleep."
            c "Wow! I wish I could do that."
            Ry normal "So do I."
            m "Vara walked up next to me."
            m "She snuggled up with us, using Remy as a side rest and my open hand as a pillow."
            c "I didn't know my dragon pillow came with dragon plushies as well!"
            Ry smile "I see you bought the deluxe bundle. It was a limited time offer."
            c "Well, I'm sure glad I did."
            Ry normal "Go ahead and sleep. I'll wake you up before Adine gets here."
            c "Thanks, Remy."
            scene black with dissolveslow
            hide remy with dissolvemed
            m "I closed my eyes and snuggled closer to Remy."
            m "I wrapped one of my arms around Amely and softly rubbed Vara's head."
            m "Remy's soft breathing quickly lulled me to sleep."
            stop music fadeout 2.0
            $ renpy.pause (3.0)
            m "I was awoken when my dragon pillow suddenly started moving."
            scene evalorphlight with dissolveslow
            show amely smnormal
            show vara smnormal behind amely
            show remy normal behind vara
            with dissolvemed
            c "Hey! Pillows aren't supposed to move!"
            Ry smile "Would you rather miss out on ice cream?"
            c "I guess not..."
            Ry normal "I woke you up just before Adine's shift ends. She should be here any minute now..."
            jump eval_everyone_1
        else:
            Ry look "I forgot that you aren't as strong as you usually are."
            Ry normal "How about you three sit down and rest for a while. She looks exhausted as well."
            Am smsad "No!"
            Vr smgrowl "Not tired!"
            m "Amely then let out a huge yawn."
            m "In response, Vara herself also yawned."
            Am smnormal "Maybe..."
            Vr smnormal "Fine..."
            m "I made my way to take a seat at a desk."
            Ry "Wait, [player_name]. You can rest on me if you like."
            Ry smile "I'm probably much more comfortable than any old desk."
            c "Oh boy, my very own full sized dragon pillow equipped with a built-in heater!"
            Ry "I'm the latest model."
            m "I carefully propped myself up against Remy's side. I could feel his body rising and falling with each breath."
            m "Amely then crawled up next to me and laid her head on my shoulder."
            Am smnormal "Goodnight."
            m "In an instant, the little dragon was fast asleep."
            c "Wow! I wish I could do that."
            Ry normal "So do I."
            c "Is she a deep sleeper?"
            Ry "Very. We can talk."
            m "Vara came up next to me and laid her head on my leg."
            m "Instead of sleeping, she idly gazed and listened as Remy and I engaged in lighthearted chatter."
            stop music fadeout 2.0
            jump eval_everyone_1
    else:
        jump eval_everyone_1
    
label eval_too_many_crackers:
    $ renpy.pause (3.0)
    scene o2 with dissolveslow
    m "I opened my eyes to find myself back in my apartment."
    m "Remy was resting on the couch next to me, and when I stirred, he got up."
    show remy normal with dissolvemed
    Ry "You're finally up."
    c "What happened?"
    Ry look "Well, I dragged you back here after you passed out at the orphanage."
    c "I think I had a little bit too much to eat."
    Ry normal "I'll say. I don't think we will be able to get any ice cream today, it's quite late."
    c "Not like I could eat another bite of food, anyways."
    Ry "I guess we'll just have to reschedule."
    Ry look "Although you're probably going to have to talk with Vara first."
    c "How come?"
    Ry sad "She blames herself for what happened at the orphanage. She locked herself in her room and hasn't come out since."
    c "Oh! Should I go and talk to her?"
    Ry look "Not yet. You should rest some more."
    Ry sad "I'm going to go and try and get her out of her room. You stay here and get better."
    hide remy with easeoutleft
    play sound "fx/door/doorchain.ogg"
    $ renpy.pause (2.0)
    scene black with dissolveslow
    $ renpy.pause (2.0)
    $ evalFail = "Cracker Addict"
    jump eval_fails