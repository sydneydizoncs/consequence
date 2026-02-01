# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    # bleep callbacks for characters    
    def bleep009(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/voice/bleep009.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)
    
    def bleep010(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/voice/bleep010.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)
                      
    def bleep016(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/voice/bleep016.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)
                   
    def bleep018(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/voice/bleep018.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)
            
    def bleep020(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/voice/bleep020.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)

    def bleep022(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/voice/bleep022.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)          
         
    def bleep025(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/voice/bleep025.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)
            
define audio.mi_bleep = "audio/voice/bleep009.mp3"
define audio.c_bleep = "audio/voice/bleep018.mp3"
define audio.b_bleep = "audio/voice/bleep022.mp3"
define audio.my_bleep = "audio/voice/bleep016.mp3"
define audio.l_bleep = "audio/voice/bleep025.mp3"
define audio.a_bleep = "audio/voice/bleep010.mp3"   

define mi = Character("Mia",   image="mia", callback = [bleep009, name_callback], who_color="#ffffff", cb_name = "mia")
define c  = Character("Cole",  image="cole", callback = [bleep018, name_callback], who_color="#daa580", cb_name = "cole")
define b  = Character("Bel",   image="bel", callback = [bleep022, name_callback], who_color="#daa580", cb_name = "bel")
define my = Character("Myles", image="myles", callback = [bleep016, name_callback], who_color="#daa580", cb_name = "myles")
define l  = Character("Lillia",image="lillia", callback = [bleep025, name_callback], who_color="#daa580", cb_name = "lillia")
define a  = Character("Akira", image="akira", callback = [bleep010, name_callback], who_color="#daa580", cb_name = "akira")
define e = Character("Everyone", who_color="#daa580")
#callback=everyone
#everyone=['mi', 'c', 'b', 'my', 'l', 'a'])

image side mia serious = "images/ui/mia serious.png"
image side mia happy = "images/ui/mia happy.png"
image side mia talk = "images/ui/mia talk.png"
image side mia worry = "images/ui/mia worry.png"

# character highlight function from 01autho-highlight
# creds to Renpy Auto Highlight, from Wattson on Itch.io

# bel's images
image bel_happy = "bel happy.png"
image bel_smile   = "bel smile.png"
image bel_serious = "bel serious.png"
image bel_talk = "bel talk.png"

# cole's images
image cole_smile = "cole smile.png"
image cole_serious = "cole serious.png"
image cole_talk = "cole talk.png"
image cole_happy = "cole happy.png"
image cole_grin = "cole grin.png"

#lillia's images
image lillia_happy = "lillia happy.png" 
image lillia_serious = "lillia serious.png" 
image lillia_smile = "lillia smile.png"
image lillia_talk = "lillia talk.png"
image lillia_worry = "lillia worry.png" 

# myle's images
image myles_smile = "myles smile.png"
image myles_serious = "myles serious.png"
image myles_talk = "myles talk.png"

# akira's images
image akira_blush = "akira blush.png"
image akira_smile = "akira smile.png"
image akira_talk = "akira talk.png"
image akira_mumble = "akira mumble.png"
image akira_happy = "akira happy.png"
image akira_serious = "akira serious.png"

# bel's init
image bel happy = At('bel_happy', sprite_highlight('bel'))
image bel serious = At('bel_serious', sprite_highlight('bel'))
image bel smile = At('bel_smile', sprite_highlight('bel'))
image bel talk = At('bel_talk', sprite_highlight('bel'))

#cole's init
image cole smile = At('cole_smile', sprite_highlight('cole'))
image cole grin = At('cole_grin', sprite_highlight('cole'))
image cole serious = At('cole_serious', sprite_highlight('cole'))
image cole talk = At('cole_talk', sprite_highlight('cole'))
image cole happy = At('cole_happy', sprite_highlight('cole'))

# lillia's init
image lillia happy = At('lillia_happy', sprite_highlight('lillia'))
image lillia serious = At('lillia_serious', sprite_highlight('lillia'))
image lillia smile = At('lillia_smile', sprite_highlight('lillia'))
image lillia talk = At('lillia_talk', sprite_highlight('lillia'))
image lillia worry = At('lillia_worry', sprite_highlight('lillia'))

# myles' init
image myles smile = At('myles_smile', sprite_highlight('myles'))
image myles serious = At('myles_serious', sprite_highlight('myles'))
image myles talk = At('myles_talk', sprite_highlight('myles'))

# akira's init
image akira blush = At('akira_blush', sprite_highlight('akira'))
image akira smile = At('akira_smile', sprite_highlight('akira'))
image akira talk = At('akira_talk', sprite_highlight('akira'))
image akira mumble = At('akira_mumble', sprite_highlight('akira'))
image akira happy = At('akira_happy', sprite_highlight('akira'))
image akira serious = At('akira_serious', sprite_highlight('akira'))

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg livingroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    menu:
        "Play Game":
            jump chapter_1
        "Play Heart Minigame":
            jump heartgame
            
label chapter_1:

    # beginning pos
    show akira smile at left with fade
    show myles serious at farright with fade
    show cole smile at centerleft with fade
    show lillia smile at centerright with fade
    show bel serious at center with fade

    # dialogue start
    mi talk "…Okay. King’s Cup. Rules are written down here."
    mi worry "Please, Cole, I know you only have two brain cells knocking around in that beautiful noggin of yours, but, seriously. Don’t make up any rules this time."
    
    # music start
    play music "audio/music/chill.mp3" fadein 1.0

    show bel smile
    "Bel flops onto the couch beside Lillia, legs crossed, grinning."

    b happy "Freestyling is the soul of drinking games, oh great Student Council President."
    show bel smile
    my talk "That’s not true. The soul is consistent."
    show myles serious
    b talk "Wow. You actually sound hot when you say it like that."
    show bel smile
    my talk "That was not an invitation, Isabel."
    show myles serious
    
    show bel serious
    "Bel sighs."

    b happy "Do you have to ruin every compliment you get?"
    b talk "Also, why do you keep calling me by my full name? Literally everyone else just calls me Bel."
    show bel serious

    "Cole is squinting at the cards like they personally offended his whole lineage."

    c talk "So wait—if I get a four… that means I ask if anyone else has another four?"
    show cole smile

    mi talk "…What?"

    "Akira blinks, quiet. A look of disbelief crosses his face."

    l talk "…Cole, honey. That’s “Go Fish”."
    show lillia smile at centerright

    c grin "Yeah! That’s what I said."
    show cole smile

    l happy "No, that’s the wrong game, silly! We’re playing King’s Cup!!"
    show lillia smile at centerright

    c talk "…Okay, but there areee cards. And we areee sitting in a circle. So I feel like I’m not wrong."
    show cole serious

    "You pinch the bridge of your nose, sighing."

    mi talk "You draw a card. You follow the rule listed on the paper."
    mi happy "No fishing involved."

    c happy "Right, right, right. Totally. Got it."
    show cole smile

    "He draws a card, looks at it, then lights up."

    c happy "DO YOU HAVE ANY FOUR—"


    show bel talk
    play sound "audio/voice/bleep09.ogg"
    play sound "audio/voice/bleep010.ogg"
    play sound "audio/voice/bleep016.ogg"
    e "NO."
    show bel serious

    show cole serious
    "Cole throws the Four of Hearts back onto the table."

    c talk "Okay, damn. Just thought it was funny…"
    show cole serious

    "A beat of silence."

    b talk "Oh my god, I need at least three more shots and a cigarette to deal with you tonight, Cole."
    show bel smile

    "Akira nervously fiddles with his sleeve."

    a talk "Um, s-so… what does a seven do again?"

    mi talk "Seven is “Heaven”. Everyone points up. Last one to point, drinks."

    a happy "Oh. O-Okay, thanks, Mia."
    show akira smile

    my talk "You didn’t even hesitate to answer… How many times have you played this game?"
    show myles serious

    mi happy "None. I just made the rules list."

    my talk "I see. Of course you did."
    show myles serious

    a blush"…Sorry if I’m delaying the start of the game… I haven’t really played drinking games too much."

    c happy "That’s fine, Akira! You don’t gotta have any experience to have fun in a drinking game!"
    c grin "You just lose some rounds, take a few shots… and all of a sudden you’re having fun!"
    show cole smile
    show akira smile

    # cutscene start
    scene black with fade
    "You all play for a few minutes. Laughter. Mild bickering. Normalcy."

    c "Okay but imagine—"
    c "Some people meet playing card games and then, like, thirty years later they’re married with kids and they’re like,"
    c "“Yeah, it all started with King’s Cup.”"

    mi "Ew… gross, Cole. We are not starting that legacy now."
    mi "This friend group has to stay dating-free! That’d just make it weird..."

    c "I’m just saying. The stories have gotta start somewhere."

    # end cutscene
    scene bg livingroom with fade

    # reinit pos
    show akira smile at left
    show myles serious at farright
    show cole smile at centerleft
    show lillia smile at centerright
    show bel serious at center

    "Cole chooses a six, prompting all of the boys to drink."
    "Akira winces at the taste, setting his cup down before drawing a card."

    mi happy "Oh, you got a two! That means you pick someone to take two sips."

    a happy "Oh, uh… then I guess I’ll choose you, Mia— as thanks for explaining the rules to me."
    a blush "But you don’t have to drink— I can always just choose myself—"

    "You immediately bring the cup to your mouth, a denial at Akira’s obvious self-sacrificing behavior."

    mi happy "Too late!"
    show akira smile

    b talk "Gosh, I need some booze in my system too, all of us are filthy lightweights…"
    show bel smile

    show bel serious
    "Bel draws a card and freezes."

    b talk "…Is this a King?"
    show bel serious

    mi happy "Yep! Pour a little into the center."

    b talk "Ew, don’t call it “the center”. That gives me weird vibes."
    b happy "It’s the Bitch Cup— say it with your chest!"
    show bel smile

    "She pours dramatically."

    b happy "And there goes my generous donation! Sorry to the fucker that has to drink that."

    b talk "If this nasty concoction somehow summons a demon... I want it on record that this was not my idea."
    show bel serious

    l worry "I’d be really polite to it. Like——what if it’s having a bad day?"

    my talk "If any demon we summon has feelings, that’s its own problem."
    my talk "But I highly doubt any cursed lifeform has the semblance of emotion to perceive a “bad day”."
    show myles serious

    "Cole stares at the red solo cup in the center."

    c talk "So… when do we drink the forbidden soup?"
    show cole serious

    mi talk "When the fourth King is drawn."

    c happy "Ah. Final boss rules."
    show cole smile

    "He leans back, chair creaking."

    c grin "Okay but—counterpoint— What if we did something even funner?"
    show cole smile

    mi worry "Cole, we just started playing—"

    my talk "Colsen. “Funner” is not a word."
    show myles serious

    c happy "Well, since Mia so graciously went out of her way to plan and pay for this trip, I so graciously in return brought activities."
    show cole grin

    "He rummages through his bag."

    a blush "W-Wait——what kind of activities…?"

    show cole smile
    "Cole pulls out a flat wooden board."

    "Silence."
    show akira serious
    "Bel turns white."

    b talk "…No."
    show bel serious

    l happy "Is that—"
    show lillia smile at centerright

    my talk "That is a Ouija board."
    show myles serious

    c grin "YES! Thank you! See? Someone appreciates culture."

    mi talk "Absolutely not."

    c happy "Aww, c’mon, Mia!"
    c grin "It’s just a board game!"
    show cole smile

    my talk "It is not a board game."
    show myles serious

    b talk "It’s literally a board where you ask ghosts questions. That’s, like… the opposite purpose of a board game."
    show bel serious

    c happy "Worst case scenario? Nothing even happens."
    show cole smile

    a talk "And… the best case?"
    show akira serious

    c talk "We talk to a ghost."
    show cole serious

    "A pause."

    c talk "I dunno. I just really like the idea that people don’t just disappear."
    c happy "That connections stick. Even when you can’t see them anymore."
    show cole smile

    l worry "If there is a ghost, it might be lonely…"
    show lillia serious at centerright

    "You sigh, looking at Lillia."

    b talk"Okay but——hypothetically——If the ghost is real and we *don’t* play… isn’t that kind of rude?"
    b "Won't it, like, haunt us if we don't play?"
    show bel serious

    my talk "That logic makes no sense."
    show myles serious

    b talk "Neither do ghosts, Myles. Keep up."
    show bel serious

    "Everyone looks at you."
    "You hesitate. Just a second too long."

    mi worry "We’re not summoning anything. If we do this, it’s just for fun."
    mi talk "Only one question."

    my talk "You’re always telling us to be careful."
    show myles smile

    mi happy "I know. That’s why I’ll be here to make sure it doesn’t get stupid."

    c grin "YES! Democracy wins!"
    show cole smile

    show myles serious
    "They clear the table. The Ouija board is placed dead center."
    "The room feels… quieter."

    b talk "Okay. But just saying, if we all die..."
    b happy "...I hope everyone in this room remembers how hot and funny I was when we’re in the afterlife."
    show bel smile

    a mumble "That’s if we all make it to the same afterlife you do…"

    "You snort. After seeing how Bel acted at Cole’s frat parties… if Bel’s going to any afterlife, it’s definitely not heaven."
    show akira blush
    "Akira glances at you shyly, a little embarrassed that you heard him."


    my talk "This is exactly how horror movies start."
    show myles serious
    show akira serious
    c grin "Or love stories~! You never know!"
    show cole smile

    b talk "…Those are two very different genres."

    c talk "Well, I dunno… sometimes they overlap."

    c grin "Don’t worry guys, I won’t let anything happen to you! Even though I don’t always know what I’m doing, I do know I wouldn’t let you guys get hurt. Ever."

    "At that moment, everyone seemed to sober up at his sincerity– Cole had a tendency to make that happen."
    "For most people, they’d shake their heads, droning on about how Cole was just that standard hero archetype."
    "But you knew Cole."
    "You’d seen what he’d been through, and what his friends meant to him, and how he’d do anything to protect and care for those that he loved."
    "Warmth flooded your heart at the thought– and as you looked around at your friends, you knew they shared that sentiment."
    "Even Bel’s spirits seemed to lift at the prospect of Cole being there to beat up any malicious spirits."

    "Cole places the planchette down, and everyone rests one hand on it."

    c happy "Alright, enough with the chit chat."
    c grin "So, whaddya say, spooky spirit! You got any fours?"

    "The lights flicker."
    
    # prologue end scene

    scene bg ouija with fade
    # music start
    play music "audio/music/rise.ogg" fadein 1.0

    "The candles flicker low, their light bending strangely across the table."
    "The ouija board sits between them—scuffed wood, worn letters, the plastic planchette cold beneath six sets of fingers. Lillia clears her throat."

    l talk "Okay. Just—just to be clear. We’re doing this as a joke, right?"
    "Cole smirks."
    my "Obviously."
    b happy "Speak for yourself. If a ghost wants to gossip, I’m listening."
    mi serious"Let’s just… not antagonize anything."
    l worry "I don’t like this. I never like this. Every horror movie starts exactly like this."
    mi happy "We’re all here. Nothing’s going to happen."
    "Akira nods, though he doesn’t look convinced."
    a "I’ve never done this before."
    b talk "Lucky you."

    "Everyone shifts, their fingers growing antsy on the planchette. You feel like it’s lighter than expected, it’s almost too smooth."
    "Seconds stretch. A minute. Nothing happens."
    "Lillia shifts in her chair."

    l worry "Is it supposed to take this long?" 
    b happy "...Maybe the ghost is thinking."
    mi serious "I don’t know, Lils. Maybe we should just give it time."
    my "Or, more probable, it’s not real."

    "Out of the corner of your eye, you see Lillia’s gaze sharpen."

    l talk "Don’t say that."
    l talk "If it is real, don’t insult it."
    c grin "See? She believes."
    l serious "I'm a {i}Libra{/i}! Of {i}course{/i} I believe in the paranormal!"
    mi serious "Everyone’s touching it, right? Don’t mess around."
    a "Y-Yeah, I’m touching it."
    l "I swear, if someone’s pushing it—"
    b "Okay, verdict. This is {i}boooring{/i}. I’m calling it."
    
    # music stop
    "Bel starts to pull her hand away, but before she can--"

    # music switch
    play music "audio/music/arrival.ogg" fadein 1.0

    "The planchette {i}jerks{/i}."
    mi "--!"
    b "—Uh."
    l "{i}—W-Wait{/i}! Did you do that?!"
    b "No! I swear, I was just about to pull my hand away!"
    "The planchette slides slowly across the board."

    scene bg hide1 with fade
    "H."
    "Time seems to stop. Your breath catches in your throat, heart hammering."
    mi "Cole, knock it {i}off{/i}!"
    c "I’m not doing anything!"

    scene bg hide2 with fade
    "I."
    b "T-This isn’t funny anymore!"
    my "Lillia, are you doing this?!"
    l "N-No! I would {i}never{/i} anger a spirit like this!"

    scene bg hide3 with fade
    "D."
    "The planchette continues to move, spelling out a word."

    scene bg hide4 with fade
    "E."
    
    scene black with fade
    "Silence swallows the room."

    scene bg livingroom with fade
    # reinit pos
    show akira serious at left
    show myles serious at farright
    show cole serious at centerleft
    show lillia serious at centerright
    show bel serious at center

    l worry "That spells—"
    my "We {i}know{/i} what it spells."
    mi serious "…'HIDE'?"
    c grin "Oh my god. It wants to play 'Hide and Seek'!"
    l serious "{i}Absolutely{/i} not!"
    l talk "No games. We say goodbye, burn the board in the fire, and {i}never{/i} talk about this again."
    c happy "Aw, c’mon Lils! That’s quitter talk!"
    "Cole begins to push back his chair, rising from his seat."
    c grin "This is awesome!"
    mi talk "Cole, sit down."
    c happy "I'll be the seeker! You guys hide!"
    c grin "No cheating, okay? Proper hide and seek. Ghost rules."
    my talk "Cole, you are {i}not{/i} seeking anyone."
    c happy "Too late! Sixty!"
    "Cole announces, closing his eyes. You can hear his grin as he counts, loud and clear."
    l worry "What—wait—"
    c happy"Fifty-nine! Fifty-eight!"
    "Lillia scrambles to her feet."
    l worry "I didn’t agree to this!"
    "Chairs scrape. You sit on the floor, still in fearful shock."
    c "Fourty-nine!"
    "Cole moved the planchette himself... {i}right{/i}?"
    "Ghosts most definitely aren't real. Right?"
    c "Fourty-one! Fourty! Thirty-nine!"
    "You look up, and your eyes land on Akira. While everyone else went to go hide, Akira is frozen in place, hand and eyes still glued on the planchette."

    menu:
            "HIDE WITH AKIRA.":
                jump hide_akira
            "STAY WITH COLE.":
                jump stay_cole

    label hide_akira:
        "You grab Akira's wrist frantically."
        mi "Come on. We’ll go this way."

        scene black with fade
        "You and Akira sneak away quietly, hearts pounding."

        "You slip into a narrow storage room off the hall. You ease the door shut, leaving only a thin crack of light."

        # music switch
        play music "audio/music/contemplation.ogg" fadein 1.0

        scene ak00 with fade
        "You look to your side; Akira sits beside you."
        "The tension is palpable. Dust hangs in the air, illuminated by the faint light. You can hear Cole in the distance, faintly counting."
        c "…Twenty-eight! Twenty-seven!"
        scene ak01
        a "M-Mia… do you think it’s really real?"
        scene ak02
        "You scoff."
        mi "Of course not. It’s just a game. Cole’s probably just fucking with us."
        "You laugh nervously, trying to convince both Akira and yourself."
        mi "He's good at that."
        scene ak05
        a "Y-Yeah… I guess you’re right."
        scene ak03
        "You both sit in silence, the seconds stretching on."
        c "…Nineteen!"
        scene ak04
        a "Hey, um... I'm sorry."
        scene ak02s
        "You blink."
        mi "For what?"
        scene ak01
        a "For being here. I mean, I know you probably didn’t want me to come on this trip."
        scene ak02
        mi "Akira… don’t be an idiot. You quite literally {i}carried{/i} me through Calc II last semester."
        scene ak04
        a "Well... you didn't have to invite me. Everyone else knows each other. I don’t belong here."
        scene ak02
        mi "I {i}wanted{/i} to invite you. I hope it's not hard to believe that I actually {i}enjoy{/i} having you around, Akira."
        mi "Besides, with the assignments that Professor Tompkins gave us, I think we both have a trauma bond now."
        scene ak03
        "Akira chuckles softly, the tension easing slightly."
        scene ak05
        a "Y-Yeah… I guess we do."
        scene ak03
        c "Seven! Six!"
        mi "Whether you like it or not, I'm inducting you into my friend group. No take-backs."
        c "...Three! Two! One!"
        c "Ready or not, here I come!"
        "The sound of his footsteps retreats down the hall, careless and eager."
        "There’s a pause. Somewhere, a door slams. Cole’s voice echoes distantly."
        "Akira's fingers curl against the hard wood of the storage room floor as he whispers to you."
        a "Do you think we picked a good enough hiding spot?"
        a "I-I feel like… a storage closet is pretty {i}obvious{/i}."
        mi "Ehh, I think we’re fine. Cole’s an airhead, anyways. I think Lils or Bel will be found first."
        "The scream rips through the house, piercing through your ears."
        "Pained. Panicked. {i}Wrong{/i}."
        "You bolt upright from your slouched position on the floor, but before either of you can get up to run out of the closet— something in the air shifts."

        scene black
        "The lights go out. And then... that's when you hear it."
        "Footsteps press against the floorboards—slow, uneven. Too heavy on one step, dragging slightly on the next, like whatever’s walking hasn’t quite learned how yet."
        "There’s a faint wet sound, a soft {i}thud—scrape—thud{/i} that doesn’t match the rhythm of a person."
        "You’ve known Cole since high school. You know his mannerisms like the back of your hand; Cole loved to sneak over to Bel during sleepovers and scare the shit out of Bel, and even then, his footsteps were clean. Clumsy, loud, and ever so Cole-coded."
        "But this? Whatever was walking in the house now… was {i}not{/i} Cole."
        "Akira’s breath hitches. You clamp a hand over your mouth before the gasp even has a change to escape-- because you can hear it. The footsteps— they’re growing closer."
        "Each step seems to bend reality around itself, warping the silence until you were almost choking on it. Tears pricked at the corners of your eyes."
        "The steps pause just outside the closet. Your heart hammers so hard she’s sure it can be heard. You press your forehead to Akira’s shoulder. You start to hold your breath."

        # HEARTBEAT MINIGAME

        play music "audio/music/heartbeat.ogg" fadein 1.0
        # if win: continue
        # win == no losses
        # if lose: return

        "But then... whatever it was passes."
        "Eventually, the sound of its steps drift down the hall, growing quieter, until it dissolving into nothing."

        scene ak10
        "The lights snap back on."
        scene ak12
        a "A-Are you okay? What... {i}what was that{/i}?"
        scene ak11
        mi "I-I don't know, but... {i}that wasn’t Cole{/i}."




        jump after_choice

    label stay_cole:
        mi "Go... go hide, Akira."
        return

    label after_choice:
        "Everyone shifts uneasily."
        return





    # This ends the game.

    return
