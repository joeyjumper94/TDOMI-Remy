#Changes dialogue for when you arrive at the orphanage
#Incorporate a Vara mood counter for how she reacts? Oh god that sounds not fun
label eval_secret_orphanage_arrival:
    Ry "Amely? Vara? Are you two here?"
    show amely smnormal with easeinright
    Am "Hello!"
    Ry smile "Hello, Amely."
    Ry normal "Do you know where Vara is?"
    Am "She is coming."
    show vara smnormal behind amely with easeinright
    Vr "..."
    c "Hi, Vara."
    Vr "Hello."
    Ry "She's been talking much more since you last saw her, [player_name]."
    c "That's great to hear."
    Vr "It's dark."
    Ry "I see that, Vara. I wonder who turned the lights off. Usually we leave them on for you."
    c "Wait, is the orphanage just a classroom?"
    Ry look "Sadly, this is most of the space that the orphans get. They play, learn, study, and eat in here or outside for most of the day."
    c "Where do they sleep?"
    Ry normal "We have some small bedrooms for them down the hall."
    Ry "At the moment, the council has it completely closed off."
    c "Is that for any particular reason?"
    Ry "Not exactly. They probably don't want random dragons just waltzing in and taking the childrens' beds."
    c "That makes sense. So what exactly are we doing here today?"
    Ry "Let's take a look."
    hide remy with easeoutleft
    Am "I come!"
    hide amely with easeoutleft
    m "Vara stayed by my side as the two dragons went to the lightswitch."
    play sound "fx/lightswitch.mp3"
    $ renpy.pause (1.0)
    play sound "fx/lightbreak.mp3"
    $ renpy.pause (2.0)
    Am "Uh oh!"
    show vara smshocked with dissolvemed
    Ry look "Well, that's not good."
    play sound "fx/lightswitch.mp3"
    $ renpy.pause (2.0)
    play sound "fx/lightswitch.mp3"
    $ renpy.pause (2.0)
    show remy normal flip behind vara with easeinleft
    show remy normal behind vara with dissolvemed
    show amely smnormal flip with easeinleft
    show amely smnormal with dissolvemed
    show vara smnormal behind amely with dissolvemed
    Ry "I think I know something that we're going to have to do."
    c "Fix the lights?"
    Ry smile "How'd you guess?"
    c "Not sure. Maybe I'm psychic."
    Ry "Well, if you're psychic, do you know what else is wrong here?"
    c "I think my powers only work once a day."
    Ry normal "Alright then. From what I can remember, that desk in the middle of the room is very broken."
    c "How'd that happen?"
    Ry look "You know how I said that learning to control fire or acid breath can be difficult for young dragons?"
    Ry "Well, Vara managed to melt one of the legs of the desk."
    Am "It was cool!"
    Vr smsad "I didn't mean to..."
    Ry normal "Don't feel bad, Vara. You were still learning and nobody got hurt."
    Vr "..."
    Vr smnormal "Okay..."
    Ry normal "Anyways, we should also try to go through the hatchlings' art and the paperwork left around."
    Ry "And finally, just clean up the place a little bit. These walls have seen one too many crayons in their time."
    m "I noticed a plethora of crayon scribbles on the wall that stopped at around Amely's height."
    Ry look "Not to mention that the books in here have seen better days."
    c "How should we do this?"
    Ry normal "Most of the supplies we have here are scattered around in a few locations near this building."
    Ry "So I think you should stay here while I grab things for you."
    Am "I help?"
    Ry "Sure, Amely."
    Am "Yay!!!"
    Ry "Would you like to come along as well, Vara?"
    Vr "I stay here."
    c "It'll be nice to have an extra set of hands, or I guess claws, to help."
    Ry smile "Sounds like a plan. Let's do this!"
    show remy normal behind vara with dissolvemed
    jump eval_secret_orphanage_game_init

label eval_everyone_1:
    play sound "fx/wooshes.ogg"
    $ renpy.pause (3.0)
    Ry smile "I wonder who that could be?"
    play sound "fx/door/door_open.wav"
    hide amely
    hide vara
    hide remy
    with dissolvemed
    show amely smnormal at right
    show vara smnormal behind amely at right
    show remy normal behind vara at right
    with dissolvemed
    show adine normal c flip behind amely at left
    play music "mx/cruising.ogg"
    Am "Adine!"
    show amely smnormal at left with move
    m "The little dragon ran up to Adine and gave her a big hug."
    show amely smnormal flip at left with dissolvemed
    Ad giggle c flip "Hello, Amely. you act like I just came back from a long trip when I just saw you this morning."
    Am "I missed you!"
    play sound "fx/undress.ogg"
    show adine normal b flip with dissolvemed
    m "Adine took off her goggles."
    Ad "Hey guys! What are you doing here?"
    Ry "Looking for you!"
    Ad giggle b flip "Well, I guess you found me, or rather, I found you."

    if not evalReplaceBulbs or not evalResetBreaker:
        Ad think b flip "Hey, Remy. Why are the lights turned off?"
        Ry look "Well... they're broken."
        Ad dissapoint b flip "Oh. Poor Amely and Vara. They were stuck in the dark all this time?"
        Am "Dark!"
        Vr smnone "Very dark."
        Ad sad b flip "Oh, I'm so sorry you two. I didn't know."
        Ry "I wouldn't worry too much, Adine. They both seem quite alright."
        Ad dissapoint b flip "I guess..."
        show vara smnormal at right with dissolvemed
    
    if evalOrphanageScore == 2:
        Ad think b flip "Wait a minute..."
        show adine think b with dissolvemed
        $ renpy.pause (0.5)
        show adine think b flip with dissolvemed
        Ad giggle b flip "What did you guys do? The orphanage looks amazing!"
        Ry "Well, [player_name] and I wanted to surprise you by cleaning up the place a little bit."
        show adine think b with dissolvemed
        $ renpy.pause (0.5)
        show adine gigglbe b flip with dissolvemed
        Ad "This isn't real. My eyes are deceiving me."
        c "You don't believe us?"
        Ad normal b flip "Are you kidding me? This place hasn't looked this good in years!"
        Ad "How did you two manage to do all of this so quickly?"
        Vr "Hey! We helped!"
        Am "Yeah!"
        Ad giggle b flip "I'm sorry. How did you {i}four{/i} manage to do all of this so quickly."
        Ry normal "Teamwork. Amely and I gathered supplies while [player_name] and Vara did all the handiwork."
        Ad normal b flip "You do not understand how grateful I am that you did this."
        hide adine with dissolvemed
        play sound "fx/hug.mp3"
        m "Adine walked up and gave me a big hug." #The wyvern gives you a hug. Mission complete.
        m "With wings as arms, I was engulfed completely."
        play sound "fx/hug.mp3"
        m "She then walked over to Remy and repeated the process."
        show remy shy behind vara at right with dissolvemed
        Am "Me! Me!"
        Vr "Me too!"
        hide adine with dissolvemed
        hide amely
        hide vara
        with dissolvemed
        play sound "fx/hug.mp3"
        m "Adine got down on her knees and completely hid the two little dragons within her wings."
        show adine normal b flip at left with dissolvemed
        show amely smnormal flip at left with dissolvemed
        show vara smnormal at right with dissolvemed
        Ad "Now, I know the real reason you came here wasn't just to clean up the place."
        c "Alright you caught us."
        Ad "What was your real motive, then?"
        Ry normal "Hey! We wanted to surprise you by cleaning up the place as well."
        Ad giggle b flip "I'm just messing with you guys."
    elif evalOrphanageScore == 1:
        Ad "Wait... Did you guys do something here?"
        Ry smile "Well, [player_name] and I did a bit of work while we were wating for you."
        Ad "Really? That's so kind of you! What were you waiting on me for?"
    else:
        Ad normal b flip "I expected to find you here Remy, but what is [player_name] doing here?"
    c "We have come to offer you the deal of a lifetime."
    c "Free ice cream from the world renowned Katsuharu!"
    Ad giggle b flip "Can't say I expected that."
    Ad think b flip "I have never heard of that dragon giving anyone free ice cream."
    Ad "You must have done something quite spectacular to get a deal like that."
    c "Just a little bit of business advice. I told him to move his stand down to Tatsu Park."
    Ad "That's it?"
    c "Does there need to be more?"
    Ad normal b flip "I guess not. Count me in."
    Ry smile "That's great! This is going to be fun!"
    Ad giggle b flip "Two dragons, a human with a big appetite, and two little hatchlings with unlimited access to delicious ice cream. I sure hope Katsuharu has enough stock."
    c "We couldn't possibly eat {i}that{/i} much ice cream, could we?"
    Ad normal b flip "Coming from someone who has had three scoops in one sitting, it is definitely possible."
    Ry normal "So, Amely and Vara, are you excited to have your first ever scoop of ice cream?"
    Vr "Ice cream!"
    Am smsad "Ice cream?"
    c "Well, Amely. Ice cream is kind of like... Well... Um..."
    m "I didn't think it would be so difficult to describe something as simple as ice cream."
    Vr "Soft, frozen dessert!"
    c "Yes, Vara described it perfectly."
    m "Vara gave us a proud expression."
    Vr "I read about it in a book!"
    c "Have you tried it before."
    Vr smnone "No..."
    Ry "Well, I'm sure you'll love it, Vara."
    show vara smnormal
    m "Amely still didn't look completely sold on the idea of ice cream."
    Am "Sugar?"
    c "Yes, lots of sugar."
    Am smsmile "Sugar!!!"
    if not evalOrphanageScore == 2:
        Ry look "What about the orphanage, Adine?"
        Ad normal b flip "We can do the maintenance work any time we want. I don't know how many other opportunities these two little dargons would get to experience something like this."
        Ry normal "Good point."
    Ad think b flip "Wait a minute."
    Ad "How are we supposed to get over to Tatsu Park?"
    Ad "I can fly Amely over, but how are [player_name] and Vara going to make it there in a reasonable amount of time?"
    Ry normal "They could just ride on my back."
    Ad giggle b flip "What are you? A dragon shuttle?"
    Ry smile "I charge my clients in ice cream."
    Ad "What a coincidence."
    Ry normal "Quite the coincidence indeed."
    Ad normal b flip "Alright, Amely, let's go."
    Am "Sugar!!!"
    hide amely with easeoutright
    play sound "fx/door/door_open.wav"
    $ renpy.pause (0.5)
    Ad "Whoah! Wait for me, Amely! I'm the one with wings here!"
    hide adine with easeoutright
    $ renpy.pause (1.0)
    play sound "fx/door/door_open.wav"
    $ renpy.pause (1.5)
    play sound "fx/takeoff.ogg"
    m "After a moment, Adine caught up with Amely. Clutching the little hatchling in her claws, she took off and soared into the air."
    hide remy
    hide vara
    with dissolvemed
    if not evalRodeRemy:
        c "Can't say I've ever ridden on the back of a dragon before."
        Ry normal "There's a first for everything."
    else:
        Ry normal "Well, are you two ready."
        Vr "Yes!"
        c "Sure am."
    hide remy with dissolvemed
    play sound "fx/bed.ogg"
    m "Remy got down on all fours."
    m "Making sure not to mess up his tie, I carefully hopped onto his back. He folded his wings back to give me as much room as possible."
    m "Vara sat on her hind legs and stretched her arms towards me. I lifted her up and placed her in front of me on Remy's back."
    Ry "How is it back there?"
    Vr "Fun!"
    if not evalRodeRemy:
        c "A bit uncomfortable. I think I need a saddle."
        Ry "Funnily enough, you can actually buy dragon saddles."
        c "That's... Interesting."
        Ry "They exist. I didn't say they were popular."
    else:
        c "I'm seriously considering the saddle now."
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (3.0)
    play sound "fx/door/door_open.wav"
    scene hatchery with dissolveslow
    Ry "Would you mind locking the door and hiding the key again?"
    c "Sure."
    m "Not wanting to repeat the process of getting on Remy, I grabbed the key and stretched my arm towards the door."
    play sound "fx/door/doorchain.ogg"
    m "Even with Vara in front of me, I managed to slip in the key and lock the door."
    c "How do I get the key back under the pot?"
    Ry "Like this."
    m "Remy walked over to the pot and tilted it up with his muzzle."
    m "I put the key back, and he carefully rested the pot back in it's upright position."
    Ry "Perfect! Let's go!"
    if not evalRodeRemy:
        m "Remy then slowly started walking forward, picking up speed surprisingly quickly."
        $ evalRodeRemy = True
    else:
        m "Remy walked forward and quickly picked up speed."
    
    if not evalRodeRemy:
        if evalRodeBryce:
            m "It wasn't as uncomfortable as I had first imagined."
            m "It was almost like riding a horse, if the horse had scales, giant wings, and a tie."
            m "In a way, it also felt strangely familiar, like I had done this before."
            m "The experience was almost relaxing, with the light breeze and rhythmic thumping of Remy's feet on the grass and pavement."
            m "I gently held onto Vara to keep her safe as I watched the dragon world pass by me."
        else:
            m "It wasn't as uncomfortable as I had first imagined."
            m "It was almost like riding a horse, if the horse had scales, giant wings, and a tie."
            m "I gently held onto Vara to keep her safe as I watched the dragon world pass by me."
    else:
        m "As a seasoned dragon rider. I sat back and gazed up at the sky, gently holding onto Vara to keep her safe." #Is this too... weird?
    
    $ renpy.pause (0.5)
    m "It seemed as if it took mere minutes to arrive back at Tatsu Park."
    Ry "Ladies and gentledragons, this will be our final stop. Please make sure to grab all of your belongings and safely exit the vehicle."
    if not evalRodeRemy:
        c "Very funny Remy."
        Ry "Thanks, I can tell that you sincerely mean that."
    else:
        c "Saying the same joke twice doesn't make it funnier, Remy."
        Ry "Nonsense."
    play sound "fx/bed.ogg"
    m "I gracefully slid off of Remy's back."
    m "I then grabbed Vara and gently rested her on the ground."
    scene park2 with dissolveslow
    show remy normal with dissolvemed
    show vara smnormal with dissolvemed
    play music "mx/funness.ogg"
    if evalRodeRemy:
        c "That was fun! I should ride you around more often!"
    else:
        c "Damn, why didn't I just ride you over to the orphanage as well. That was fun!"
    Ry smile "Wow, [player_name], I didn't know you wanted to ride me so badly."
    m "My face turned bright red."
    Ry "You look like a tomato."
    c "I'll get you back for this, Remy."
    Ry "I'm sure you will."
    m "I spotted Adine and Amely walking over to us."
    show remy normal at right
    show vara smnormal at right
    with move
    show amely smnormal flip at left
    show adine normal b flip behind amely at left
    with easeinleft
    Ad "Took you three long enough to get here."
    Ad giggle b flip "I don't suppose you had to make any other stops or pick up any more passengers on your way over here, Remy."
    Ry "Nope. We just had to lock up the orphanage on our way out."
    Ad "So, you said Katsuharu relocated here. Any idea where he is?"
    m "Suddenly, inspiration struck me as Adine idly moved her tail in my direction."
    c "Not sure, Adine. Why don't we call and find out?"
    m "I stepped and grabbed the end of Adine's tail."
    Ad think b flip "What the..."
    Ry look "[player_name], what are you doing?"
    m "I held the crescent moon end of Adine's tail up to my ear like a telephone."
    c "Hey, is this Katsuharu? We were just wondering where you set up for the day."
    Ry smile "Ah, the ol' banana phone."
    Ad annoyed b flip "This is so unbelievably stupid."
    c "Oh, you're at the front of that long line of dragons over there? Thanks!"
    $ evalAdineSlaps += 1
    play sound "fx/slap1.wav"
    m "The second I released my grip, Adine flicked her tail and slapped me square in the face."
    Am "Ouch!"
    c "Totally worth it."
    Ry "I have to admit, that was pretty funny."
    Ad "I hate you both."
    c "Hey! You were asking for it."
    Ad "I guess I was. But still, screw you guys."
    Ry normal "Now we're even."
    Ad giggle b flip "Oh, you think this is over? This is only the beginning."
    c "Oh no."
    Ad normal b flip "Oh yes."
    Am "Ice cream?"
    Ry "I almost forgot about the ice cream! We should probably go before Katsuharu closes up for the day."
    scene black with dissolveslow
    m "We made our way to the end of the line of dragons I had seen earlier."
    scene town2 with dissolveslow
    show vara smnormal at right
    show remy normal behind vara at right
    show amely smnormal flip at left
    show adine normal b flip behind amely at left
    with dissolvemed
    Ry "Wow! This is quite the line!"
    c "I think my advice has paid off for him after all."
    Ry smile "It seems so."
    Ad "So, are we planning on waiting in line with everyone else?"

    menu:
        "It would be rude to skip everyone.":
            c "It would be rude to skip everyone."
            Ry "I would have to agree with you. All of these people have been waiting for a long time to get their ice cream, and I'm sure it would make them unhappy if we just skipped ahead."
            Ad think b flip "I'm not too sure."
            Ad "If Katsuharu was willing to give you free ice cream, I'm sure he would be more than willing to let you skip the line as well."
            Ry normal "It's not that. I just don't think we should be attracting so much attention to ourselves, especially with [player_name]."
            Ad normal b flip "True."
            c "Looks like the line is about an hour long." #Do I add a mini game??? Tune in next time for //Is Eval Lazy?\\ Yes I am no minigame for you.
            m "For a few minutes, Remy, Adine and I engaged in lighthearted chatter, discussing the events that had gone on while I was in my coma."
            show amely snormal at left with dissolvemed
            hide amely with easeoutleft
            m "However, our conversation was rudly inturrupted when I noticed Amely running off."
            c "Ummm, Adine? Where is Amely going?"
            Ad annoyed b flip "Good question. I'll go grab her."
            show adine annoyed b with dissolvemed
            hide adine with easeoutleft
            Ry "Well, what do we do now?"
            c "Why not talk more?"
            Ry look "I think I'm fresh out of topics."
            Vr smnone "I talk."
            Ry normal "What about?"
            Vr smnormal "Cooking!"
            c "Go ahead, Vara. We're all ears."
            show vara smnone with dissolvemed
            m "At first, her words came out nervously, and she was almost inaudible."
            show vara smnormal with dissolvemed
            m "However, as she continued, she spoke with more clarity and confidence."
            m "By the time we reached the front of the line, I felt like a chef."
        
        "I think we can skip the line.":
            c "I think that my unlimited ice cream pass also includes an express pass to the front of the line."
            Ry look "Are you sure? I'm not sure how well some of his customers will react to us cutting them in line."
            Ad "If Katsuharu was willing to give [player_name] free ice cream, then I'm sure he would be more than willing to let him skip the line as well."
            Ry "I guess. I just feel like we shouldn't be attracting so much attention to ourselves, especially with [player_name]."
            Ad "Most of the concern and interest in humans has already died off. Sure, we might get a few stares here or there, but nothing more."
            Ry normal "I suppose you're right."
            c "You guys have had front row seats to the whole human show as well though. You might be a bit more used to me than everyone else."
            Ad "With the amount of press about your arrival. I'm sure just about every person in this line has seen or read everything about you."
            c "Wow, I'm famous."
            Ry "Don't let it get to your head."
            c "Too late, I think it already has."
            m "As we passed down the line, we were met with a mix of expressions. Some of the people seemed quite intrigued by my appearance, while others seemed annoyed, probably understanding our intentions to skip the line."
            m "Approaching the stand, I caught the attention of Katsuharu. He waved and beckoned us to come."
        
        scene town7 with dissolveslow
        show amely amely at right
        show vara snmornal behind amely at right
        show remy normal behind vara at right
        show adine normal b behind remy at Position (xpos=0.6)
        with dissolvemed
        show katsu normal flip at Position (xpos=0.1) with easeinleft

        Ka "Well, if it isn't the business saving human, [player_name]! What brings you here today?"

        menu:
        "Hey! Long time no see.":
            c "Yeah, it's really been a while, hasn't it. A lot has gone on since we last saw each other."
            Ka exhausted flip "Quite a lot it seems. You have caused quite the chaos since you arrived."
            c "I guess I just have a knack for it."
            c "Hopefully it should all return back to the peaceful way it was."
            c "Everything has more or less resolved itself and the conflict is over."
            Ka smile flip "Glad to hear that."
            c "Is it alright if I brought these three along as well?"
            Ka exhausted flip "Wow... When I offered you that ice cream, I didn't think you would bring all of your friends as well."
            Ry look "Listen, Katsuharu. If it's too much, just give [player_name] their ice cream."
            Ka "Hmmm..."
            Ka smile flip "You know, not once in my time working this cart have I ever left a potential customer hungry."
            Ka "How about this?"
            Ka "You four get as much ice cream as you desire. But first, you have to help me serve some customers for a while."
            Ry normal "That doesn't sound that bad."
            Ad think b "Yeah, I honestly wouldn't mind doing that for some ice cream."
            Ad normal b "It might even be fun."
            Vr "I want to make ice cream!"
            Am "Ice cream!"
            Ry "I guess it's really up to you, [player_name]. This was your idea after all."
        
        "No time for chatting.":
            c "No time for chatting, we are here for important ice cream related matters."
            show remy look at right behind amely with dissolvemed
            show adine annoyed b at Position (xpos=0.6) behind remy with dissolvemed
            Ka smile flip "*chuckles* Well, I guess I can't blame you for the enthusiasm."
            Ka normal flip"I actually remember Remy's first time getting ice cream from me, back when he was just a young little dragon."
            Ry shy "You do?"
            Ka smile flip "Yep, you were just as enthusiastic. Your eyes were practically bulging out of your head looking at all of the different flavors."
            Ry normal "I... guess I do remember being quite excited that day."
            Ka "I also remember Adine's first time as well."
            Ad giggle b "You do?"
            Ka "Of course. You really, really wanted three cones that day."
            Ka "It was quite entertaining watching you hop away on one foot while holding ice cream in your hands and other foot."
            Ad "I remember getting a lot of strange looks from other dragons that day."
            Ry smile "I think I remember that too. Didn't you almost fall."
            Ad annoyed b "Of course I didn't. My feet are very dextrous. Walking on one foot isn't a big deal."
            Ry normal "How sanitary is holding ice cream with your feet though, Adine?"
            Ad normal b "I was a kid, you really think I was worrying about something like that?"
            Ka "Well, enough about embarrassing childhood memories. [player_name], when I gave you that offer for ice cream, I didn't expect you to bring all of your friends."
            Ry look "Listen, Katsuharu. If it's too much, just give [player_name] their ice cream."
            Ka normal flip "You know, not once in my time working this cart have I ever left a potential customer hungry."
            Ka "How about this? You four get as much ice cream as you desire."
            Ka "But first, you have to help me serve some customers for a while."
            Ry normal "That doesn't sound that bad."
            Ad think b "Yeah, I honestly wouldn't mind doing that for some ice cream. It might even be fun."
            Vr "I want to make ice cream!"
            Am "Ice cream!"
            Ry "I guess it's really up to you, [player_name]. This was your idea after all."
    
    menu:
        "[[Help out Katsuharu]":
            c "You really think I would leave you guys like that? Of course we can help you, Katsuharu."
            show remy normal at right behind amely with dissolvemed
            show adine normal b at Position (xpos=0.6) behind remy with dissolvemed
            Ka exhausted flip "Thank goodness. Today has been quite rough, and It'll be nice to have some extra hands."
            Am "Ice cream?"
            Ry smile "Soon, Amely. First we have to help serve it."
            Am smsad "Why?"
            Ad giggle b "Because then you get two scoops of ice cream instead of one!"
            Am smnormal "More sugar?"
            Ad normal b "Yes, much more sugar."
            Am "I help! I help!"
            Ka excited flip "That's the spirited staff I want! Let's get to work!"
            m "The five dragons made their way behind the cart. I followed closely behind."
            show katsu normal at Position (xpos=0.1) with dissolvemed
            hide katsu with easeoutleft
            hide adine with easeoutleft
            hide remy with easeoutleft
            hide vara with easeoutleft
            hide amely with easeoutleft
            scene black with dissolveslow
            scene evalkatsucart with dissolveslow
            Ka normal "Alright, here's the plan everyone."
            Ka "Remy, grab a scoop from that drawer there."
            Ry normal "Yes, sir!"
            Vr "Can I make it too?"
            Ka smile "Of course you can, Vara. Grab a scoop as well."
            Ka "[player_name], you take orders."
            Ka "And Adine..."
            Ka "Just make sure Amely doesn't cause too much chaos."
            Ad giggle b "Sounds good, Katsuharu."
            Ka "Quick tip, [player_name]. Customers don't always want the same thing. Try adapting to their interests."
            c "Seems simple enough."
            jump eval_katsu_help_init

        "[[Enjoy your ice cream alone]":
            stop music fadeout 2.0
            if evalHelpOrphanage:
                c "I think I've already done enough work today helping at the orphanage."
            else:
                c "That seems like a lot more work than I want to put up with at the moment."
            
            Ka exhausted flip "I was looking forward to the extra help."
            Ry sad "Oh, I see, [player_name]."
            Am smsad "Ice cream?"
            Ry "Sorry, Amely. I guess not today."
            Am "Awwwwww."
            show remy sad flip with dissolvemed
            show amely smsad flip with dissolvemed
            hide remy with easeoutright
            hide amely with easeoutright
            m "With his head hung low, Remy walked away with Amely."
            Ka "I'll... go get you your ice cream, [player_name]."
            show katsu exhausted with dissolvemed
            hide katsu with easeoutleft
            Ad frustrated b "Did you seriously make us come all the way just to flake out on us?"
            c "Sorry, Adine. I just really don't feel like doing this right now."
            c "Also, can't you just wait in line and get the ice cream for yourselves."
            Ad "Ugh. It isn't about the ice cream any more, [player_name]! It was about spending time together."
            Ad sad b "But I see how it is. You care more about yourself than your friends."
            Ad annoyed b "I can't believe that I ever thought you were a friend of mine."
            Ad sad b "If you will excuse me, I'm going to go talk to Remy. You really hurt him with that, [player_name]."
            c "I..."
            Ad annoyed b "Shut up."
            show adine disappoint b flip with dissolvemed
            hide adine with easeoutright
            Ad sad b "Remy, are you alright?"
            m "I could hear faint crying in the distance."
            show katsu exhausted flip with easeinleft
            Ka "Well... Here you are."
            c "Thanks, Katsuharu."
            show katsu exhausted with dissolvemed
            hide katsu with easeoutleft
            m "Without another word, the old dragon returned to his stand."
            m "Watching him work, I spotted a single tear roll down one of his cheeks."
            m "As I looked behind me, I noticed that the attention of just about every dragon in line had shifted to me. They had seen everything."
            m "Shamefully, I started on my way back to my place."
            "???" "Did you see what that human just did? That was horrible!"
            "???" "I can't believe someone could be that selfish!"
            m "Hearing these comments, I picked up my pace."
            scene black with dissolveslow
            m "Wow, that was mean!"
            return