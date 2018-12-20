# Mystique Doggy Transformations

image Mystique_Doggy:
    ConditionSwitch(
    "newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_Doggy",
    "newgirl['Mystique'].LooksLike == 'Raven'", "Mystique_Blue_Doggy",
    "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Doggy",
    "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Doggy",
    "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Doggy",
    "True", "Mystique_Blue_Doggy",
    ),


# Emma Section ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
image Mystique_Emma_Doggy:
    LiveComposite(                                                                                 #Base body
        (420,750),
        (0,0), ConditionSwitch(                                                         #Shows different upper body motion depending on events
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Mystique_Emma_Doggy_Fuck3_Top",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Mystique_Emma_Doggy_Fuck2_Top",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Mystique_Emma_Doggy_Fuck_Top",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Emma_Doggy_Anal_Head_Top",
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Mystique_Emma_Doggy_Fuck2_Top",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Mystique_Emma_Doggy_Fuck_Top",
            "True", "Mystique_Emma_Doggy_Body",
            ),
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Mystique_Emma_Doggy_Fuck3_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Mystique_Emma_Doggy_Fuck2_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Mystique_Emma_Doggy_Fuck_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Emma_Doggy_Anal_Head_Ass",
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Mystique_Emma_Doggy_Fuck2_Ass",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Mystique_Emma_Doggy_Fuck_Ass",
            "True", "Mystique_Emma_Doggy_Ass",
            ),
        )
    align (0.6,0.0)


image Mystique_Emma_Doggy_Body = LiveComposite(                                                                                         #Upper body
        (420,750),
        (0,0), ConditionSwitch(                                                                                 #Hair underlayer
            #"E_Water", Null(),
            "True", +str(emma_doggy_loc)"/Emma_Doggy_HairBack.png",
            ),
        # (0,0), ConditionSwitch(                                                                                 #Mouth
        #     "newgirl['Mystique'].Gag == 'ballgag'", +str(rogue_doggy_loc)"/Rogue_Doggy_BallGag.png",
        #     "True", Null(), #Rogue_Doggy_BallGag
        #     ),
        (0,0), ConditionSwitch(
            # "E_Tan", +str(emma_doggy_loc)"/Emma_Doggy_T3Body.png",
            # "E_Tan == 'tan3'", +str(emma_doggy_loc)"/Emma_Doggy_T3Body.png",
            "True", +str(emma_doggy_loc)"/Emma_Doggy_Body.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Mouth
            #"R_Gag == 'ballgag'", +str(rogue_doggy_loc)"/Rogue_Doggy_BallGagTop.png",
            #"'mouth' in R_Spunk and R_Gag == 'ringgag'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_BlowW.png",
            #"R_Gag == 'ringgag'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_Blow.png",
            #"E_Tan", Null(),
            "'mouth' in E_Spunk and newgirl['Mystique'].Gag", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_BlowW.png",
            "E_Gag", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_Blow.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'lipbite'", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_LipbiteW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'surprised'", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_SurprisedW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sucking'", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_BlowW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sad'", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_SadW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'smile'", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_SmileW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'tongue'", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_TongueW.png",
            "'mouth' in newgirl['Mystique'].Spunk", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_NormalW.png",
            "newgirl['Mystique'].Mouth == 'normal'", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_Normal.png",
            "newgirl['Mystique'].Mouth == 'lipbite'", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_Lipbite.png",
            "newgirl['Mystique'].Mouth == 'sucking'", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_Blow.png",
            "newgirl['Mystique'].Mouth == 'kiss'", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_Surprised.png",
            "newgirl['Mystique'].Mouth == 'sad'", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_Sad.png",
            "newgirl['Mystique'].Mouth == 'smile'", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'grimace'", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'surprised'", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_Surprised.png",
            "newgirl['Mystique'].Mouth == 'tongue'", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_Tongue.png",
            "True", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_Smile.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Mouth
            "newgirl['Mystique'].Gag == 'ballgag'", +str(emma_doggy_loc)"/Emma_Doggy_Mouth_Ballgag.png",
            "True", Null(), #Emma_Doggy_Gag
            ),
        (0,0), "Mystique_Emma Doggy Blink",
        (0,0), ConditionSwitch(                                                                                 #Brows
            "newgirl['Mystique'].Brows == 'normal'", +str(emma_doggy_loc)"/Emma_Doggy_Brows_Normal.png",
            "newgirl['Mystique'].Brows == 'angry'", +str(emma_doggy_loc)"/Emma_Doggy_Brows_Angry.png",
            "newgirl['Mystique'].Brows == 'sad'", +str(emma_doggy_loc)"/Emma_Doggy_Brows_Sad.png",
            "newgirl['Mystique'].Brows == 'surprised'", +str(emma_doggy_loc)"/Emma_Doggy_Brows_Surprised.png",
            "newgirl['Mystique'].Brows == 'confused'", +str(emma_doggy_loc)"/Emma_Doggy_Brows_Normal.png",
            "True", +str(emma_doggy_loc)"/Emma_Doggy_Brows_Normal.png",
            ),
        # (0,0), ConditionSwitch(
        #     "E_Blindfold", +str(emma_doggy_loc)"/Emma_Doggy_Blindfold.png",
        #     "True", Null(),
        #     ),                                                                             #Eyes
        #(0,0), ConditionSwitch(                                                                                 #Collar
        #    "R_Neck == 'spiked collar'", +str(rogue_doggy_loc)"/Rogue_Doggy_Collar.png",
        #    "True", Null(),                #R_Arms == 'gloved' or not R_Arms
        #    ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].Water", +str(rogue_doggy_loc)"/Rogue_Doggy_WetTop.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #Hair
            # "E_HairColor == 'black' and E_Hair == 'long'", +str(emma_doggy_loc)"/Emma_Doggy_Hair_Black.png",
            # "E_HairColor == 'black' and E_Hair == 'evo'", +str(emma_doggy_loc)"/Emma_Doggy_Hair_Ponytail_Black.png",
            # "E_Hair == 'long'", +str(emma_doggy_loc)"/Emma_Doggy_Hair.png",
            # "E_Hair == 'evo'", +str(emma_doggy_loc)"/Emma_Doggy_Hair_Ponytail.png",
            "True", +str(emma_doggy_loc)"/Emma_Doggy_HairFront.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #face spunk
            "not newgirl['Mystique'].Spunk", Null(),
            "'facial' in newgirl['Mystique'].Spunk", +str(rogue_doggy_loc)"/Rogue_Doggy_Facial.png",
            "True", Null(),
            ),
        )

image Mystique_Emma_Doggy_Ass = LiveComposite(                                                                                          #Lower body
        (420,750), #(210,375), #(419,750),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            # "E_Tan", +str(emma_doggy_loc)"/Emma_Doggy_T3Ass.png",
            # "E_Tan == 'tan3'", +str(emma_doggy_loc)"/Emma_Doggy_T3Ass.png",
            "True", +str(emma_doggy_loc)"/Emma_Doggy_Ass.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].Water", +str(rogue_doggy_loc)"/Rogue_Doggy_WetAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #Pussy Composite
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Emma_Doggy_Pussy_Fucking3",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Emma_Doggy_Pussy_Fucking2",
            "P_Sprite and P_Cock == 'in' and Speed", "Emma_Pussy_Moving",
            "P_Sprite and P_Cock == 'in'", "Emma_Pussy",
            # "E_Tan and Trigger == 'lick pussy'", +str(emma_doggy_loc)"/Emma_Doggy_T3Pussy_Open.png",
            # "E_Tan == 'tan3' and Trigger == 'lick pussy'", +str(emma_doggy_loc)"/Emma_Doggy_T3Pussy_Open.png",
            "Trigger == 'lick pussy'", +str(emma_doggy_loc)"/Emma_Doggy_Pussy_Open.png",
            # "E_Tan", +str(emma_doggy_loc)"/Emma_Doggy_T3Pussy_Closed.png",
            # "E_Tan == 'tan3'", +str(emma_doggy_loc)"/Emma_Doggy_T3Pussy_Closed.png",
            "True", +str(emma_doggy_loc)"/Emma_Doggy_Pussy_Closed.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Anus Composite
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Emma_Doggy_Anal_Fucking3",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Emma_Doggy_Anal_Fucking2",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Emma_Doggy_Anal_Fucking",
            "P_Sprite and P_Cock == 'anal' and Speed", "Emma_Doggy_Anal_Heading",
            "P_Sprite and P_Cock == 'anal'", "Emma_Anal",
            "P_Sprite and P_Cock == 'plug' and Speed", "Emma_Anal_Plug_Heading",
            "P_Sprite and P_Cock == 'plug' and newgirl['Mystique'].Plugged", +str(emma_doggy_loc)"/Emma_Doggy_Plugged.png",
            "P_Sprite and P_Cock == 'plug'", "Emma_Anal_Plug",
            "newgirl['Mystique'].Plugged", +str(emma_doggy_loc)"/Emma_Doggy_Plugged.png",
            # "E_Tan and E_Loose", +str(emma_doggy_loc)"/Emma_Doggy_T3Asshole_Loose.png",
            # "E_Tan == 'tan3' and E_Loose", +str(emma_doggy_loc)"/Emma_Doggy_T3Asshole_Loose.png",
            "newgirl['Mystique'].Loose", +str(emma_doggy_loc)"/Emma_Doggy_Asshole_Loose.png",
            # "E_Tan", +str(emma_doggy_loc)"/Emma_Doggy_T3Asshole_Tight.png",
            # "E_Tan == 'tan3'", +str(emma_doggy_loc)"/Emma_Doggy_T3Asshole_Tight.png",
            "True", +str(emma_doggy_loc)"/Emma_Doggy_Asshole_Tight.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Hose
            "newgirl['Mystique'].Spank >= 1 and newgirl['Mystique'].Spank <= 4 and newgirl['Mystique'].Plugged", +str(emma_doggy_loc)"/Emma_Doggy_SpankPlugged1.png",
            "newgirl['Mystique'].Spank >= 1 and newgirl['Mystique'].Spank <= 4 and (P_Cock == 'anal' or P_Cock == 'plug')", +str(emma_doggy_loc)"/Emma_Doggy_SpankAnal1.png",
            "newgirl['Mystique'].Spank >= 1 and newgirl['Mystique'].Spank <= 4", +str(emma_doggy_loc)"/Emma_Doggy_Spank1.png",
            "newgirl['Mystique'].Spank >= 5 and newgirl['Mystique'].Spank <= 10 and newgirl['Mystique'].Plugged", +str(emma_doggy_loc)"/Emma_Doggy_SpankPlugged2.png",
            "newgirl['Mystique'].Spank >= 5 and newgirl['Mystique'].Spank <= 10 and (P_Cock == 'anal' or P_Cock == 'plug')", +str(emma_doggy_loc)"/Emma_Doggy_SpankAnal2.png",
            "newgirl['Mystique'].Spank >= 5 and newgirl['Mystique'].Spank <= 10", +str(emma_doggy_loc)"/Emma_Doggy_Spank2.png",
            "newgirl['Mystique'].Spank >= 11 and newgirl['Mystique'].Plugged", +str(emma_doggy_loc)"/Emma_Doggy_SpankPlugged3.png",
            "newgirl['Mystique'].Spank >= 11 and (P_Cock == 'anal' or P_Cock == 'plug')", +str(emma_doggy_loc)"/Emma_Doggy_SpankAnal3.png",
            "newgirl['Mystique'].Spank >= 11", +str(emma_doggy_loc)"/Emma_Doggy_Spank3.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #spunkanal Layer
            "'anal' in newgirl['Mystique'].Spunk and P_Sprite", Null(),
            "'anal' in newgirl['Mystique'].Spunk and P_Cock == 'anal'", +str(rogue_doggy_loc)"/Rogue_Doggy_SpunkAnalOpen.png",
            "'anal' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Loose", +str(rogue_doggy_loc)"/Rogue_Doggy_SpunkAnalLoose.png",
            "'anal' in newgirl['Mystique'].Spunk", +str(rogue_doggy_loc)"/Rogue_Doggy_SpunkAnalLoose.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #spunkass Layer
            "'back' in newgirl['Mystique'].Spunk", +str(rogue_doggy_loc)"/Rogue_Doggy_SpunkAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #Hotdogging underlayer
            "not P_Sprite or P_Cock != 'out'", Null(),
            #"(R_Legs == 'skirt' or R_Legs == 'cheerleader skirt') and R_Upskirt", +str(rogue_doggy_loc)"/Rogue_Doggy_HotdogUpskirtBack.png",
            #"(R_Legs == 'skirtshort' or R_Legs == 'cheerleader skirt') and R_Upskirt", +str(rogue_doggy_loc)"/Rogue_Doggy_HotdogUpskirtBack.png",
            "True", +str(rogue_doggy_loc)"/Rogue_Doggy_HotdogBack.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Hotdogging Cock w/ alpha
            "not P_Sprite or P_Cock != 'out'", Null(),
            #"(R_Legs == 'skirt' or R_Legs == 'cheerleader skirt') and R_Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", +str(rogue_doggy_loc)"/Rogue_Doggy_HotdogMasE_Upskirt.png"),
            #"(R_Legs == 'skirt' or R_Legs == 'cheerleader skirt') and R_Upskirt", AlphaMask("Zero_Hotdog_Static", +str(rogue_doggy_loc)"/Rogue_Doggy_HotdogMasE_Upskirt.png"),
            #"(R_Legs == 'skirtshort' or R_Legs == 'cheerleader skirt') and R_Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", +str(rogue_doggy_loc)"/Rogue_Doggy_HotdogMasE_Upskirt.png"),
            #"(R_Legs == 'skirtshort' or R_Legs == 'cheerleader skirt') and R_Upskirt", AlphaMask("Zero_Hotdog_Static", +str(rogue_doggy_loc)"/Rogue_Doggy_HotdogMasE_Upskirt.png"),
            "Speed", AlphaMask("Zero_Hotdog_Moving", +str(rogue_doggy_loc)"/Rogue_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_Hotdog_Static", +str(rogue_doggy_loc)"/Rogue_Doggy_HotdogMask.png"),
            ),
        (0,0), ConditionSwitch(                                                                                 #UI tool layer
            "not UI_Tool", Null(),
            "UI_Tool", "Slap_Ass",
            #"not UI_Tool", "Slap_Ass",
            "True", Null(),
            ),
        )

image Mystique_Emma Doggy Blink:                                                                                        #Eyes
    ConditionSwitch(
    "newgirl['Mystique'].Eyes == 'sexy'", +str(emma_doggy_loc)"/Emma_Doggy_Eyes_Sexy.png",
    "newgirl['Mystique'].Eyes == 'side'", +str(emma_doggy_loc)"/Emma_Doggy_Eyes_Side.png",
    "newgirl['Mystique'].Eyes == 'normal'", +str(emma_doggy_loc)"/Emma_Doggy_Eyes_Normal.png",
    "newgirl['Mystique'].Eyes == 'closed'", +str(emma_doggy_loc)"/Emma_Doggy_Eyes_Closed.png",
    "newgirl['Mystique'].Eyes == 'manic'", +str(emma_doggy_loc)"/Emma_Doggy_Eyes_Surprised.png",
    "newgirl['Mystique'].Eyes == 'down'", +str(emma_doggy_loc)"/Emma_Doggy_Eyes_Sexy.png",
    "newgirl['Mystique'].Eyes == 'stunned'", +str(emma_doggy_loc)"/Emma_Doggy_Eyes_Stunned.png",
    "newgirl['Mystique'].Eyes == 'surprised'", +str(emma_doggy_loc)"/Emma_Doggy_Eyes_Surprised.png",
    "newgirl['Mystique'].Eyes == 'squint'", +str(emma_doggy_loc)"/Emma_Doggy_Eyes_Sexy.png",
    "True", +str(emma_doggy_loc)"/Emma_Doggy_Eyes_Normal.png",
    ),
    3
    # This randomizes the time between blinking.
    +str(emma_doggy_loc)"/Emma_Doggy_Eyes_Closed.png"
    .25
    repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                                                                                  #Insert cock animations

image Mystique_Emma_Doggy_Fuck3_Top:                #animation for anal fucking2 top half
    contains:
        subpixel True
        "Mystique_Emma_Doggy_Body"
        ypos 20
        block:
            pause .15
            ease .1 ypos 0
            pause .1
            easein .2 ypos 20
            pause .05
            repeat

image Mystique_Emma_Doggy_Fuck3_Ass:                #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Mystique_Emma_Doggy_Ass"
        ypos 5
        block:
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .1 ypos 5
            pause .05
            repeat #.90


image Mystique_Emma_Doggy_Fuck2_Top:                #animation for anal fucking2 top half
    contains:
        subpixel True
        "Mystique_Emma_Doggy_Body"
        ypos 20
        block:
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20
            pause .05
            repeat

image Mystique_Emma_Doggy_Fuck2_Ass:                #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Mystique_Emma_Doggy_Ass"
        ypos 5
        block:
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .4 ypos 5
            pause .05
            repeat

image Mystique_Emma_Doggy_Fuck_Top:                #animation for anal fucking top half
    contains:
        subpixel True
        "Mystique_Emma_Doggy_Body"
        ypos 15#28
        pause .4
        block:
            ease .2 ypos 5#10
            pause .3
            ease 2 ypos 15#28
            repeat

image Mystique_Emma_Doggy_Fuck_Ass:                #animation for anal fucking ass half
    contains:
        subpixel True
        "Mystique_Emma_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0
            repeat

image Mystique_Emma_Doggy_Anal_Head_Top:                #animation for anal fucking top half
    contains:
        subpixel True
        "Mystique_Emma_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Mystique_Emma_Doggy_Anal_Head_Ass:                #animation for anal fucking ass half
    contains:
        subpixel True
        "Mystique_Emma_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easein .1 ypos -7
            easeout .9 ypos 0
            pause .9
            repeat
















# Rogue Section ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
image Mystique_Rogue_Doggy:
    LiveComposite(                                                                                 #Base body
        (420,750),
        (0,0), ConditionSwitch(                                                         #Shows different upper body motion depending on events
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Mystique_Rogue_Doggy_Fuck3_Top",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Mystique_Rogue_Doggy_Fuck2_Top",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Mystique_Rogue_Doggy_Fuck_Top",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Rogue_Doggy_Anal_Head_Top",
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Mystique_Rogue_Doggy_Fuck2_Top",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Mystique_Rogue_Doggy_Fuck_Top",
            "True", "Mystique_Rogue_Doggy_Body",
            ),
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Mystique_Rogue_Doggy_Fuck3_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Mystique_Rogue_Doggy_Fuck2_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Mystique_Rogue_Doggy_Fuck_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Rogue_Doggy_Anal_Head_Ass",
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Mystique_Rogue_Doggy_Fuck2_Ass",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Mystique_Rogue_Doggy_Fuck_Ass",
            "True", "Mystique_Rogue_Doggy_Ass",
            ),
        )
    align (0.6,0.0)


image Mystique_Rogue_Doggy_Body = LiveComposite(                                                                                         #Upper body
        (420,750),
        (0,0), ConditionSwitch(                                                                                 #Hair underlayer
            "newgirl['Mystique'].Water", Null(),
            "R_Hair == 'evo' and R_HairColor == 'black'", +str(rogue_doggy_loc)"/Rogue_Doggy_HairBlackB.png",
            "R_Hair == 'evo' and R_HairColor == 'blonde'", +str(rogue_doggy_loc)"/Rogue_Doggy_HairBlondeB.png",
            "R_Hair == 'evo'", +str(rogue_doggy_loc)"/Rogue_Doggy_HairB.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "R_Tan and newgirl['Mystique'].Gag == 'ballgag'", +str(rogue_doggy_loc)"/Rogue_tDoggy_BallGag.png",
            "newgirl['Mystique'].Gag == 'ballgag'", +str(rogue_doggy_loc)"/Rogue_Doggy_BallGag.png",
            "True", Null(), #Rogue_Doggy_BallGag
            ),
        (0,0), ConditionSwitch(
            "R_Tan == 'tan1'", +str(rogue_doggy_loc)"/Rogue_t1Doggy_Body.png",
            "R_Tan == 'tan'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Body.png",
            "True", +str(rogue_doggy_loc)"/Rogue_Doggy_Body.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Mouth
            "R_Tan and newgirl['Mystique'].Gag == 'ballgag'", +str(rogue_doggy_loc)"/Rogue_tDoggy_BallGagTop.png",
            "newgirl['Mystique'].Gag == 'ballgag'", +str(rogue_doggy_loc)"/Rogue_Doggy_BallGagTop.png",
            "R_Tan and 'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Gag == 'ringgag'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_BlowW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Gag == 'ringgag'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_BlowW.png",
            "R_Tan and newgirl['Mystique'].Gag == 'ringgag'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_Blow.png",
            "newgirl['Mystique'].Gag == 'ringgag'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_Blow.png",
            "R_Tan and 'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'lipbite'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_LipbiteW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'lipbite'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_LipbiteW.png",
            "R_Tan and 'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'surprised'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_SurprisedW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'surprised'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_SurprisedW.png",
            "R_Tan and 'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sucking'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_BlowW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sucking'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_BlowW.png",
            "R_Tan and 'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sad'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_SadW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sad'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_SadW.png",
            "R_Tan and 'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'smile'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_SmileW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'smile'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_SmileW.png",
            "R_Tan and 'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'tongue'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_TongueW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'tongue'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_TongueW.png",
            "R_Tan and 'mouth' in newgirl['Mystique'].Spunk", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_NormalW.png",
            "'mouth' in newgirl['Mystique'].Spunk", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_NormalW.png",
            "R_Tan and newgirl['Mystique'].Mouth == 'normal'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_Normal.png",
            "newgirl['Mystique'].Mouth == 'normal'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_Normal.png",
            "R_Tan and newgirl['Mystique'].Mouth == 'lipbite'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_Lipbite.png",
            "newgirl['Mystique'].Mouth == 'lipbite'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_Lipbite.png",
            "R_Tan and newgirl['Mystique'].Mouth == 'sucking'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_Blow.png",
            "newgirl['Mystique'].Mouth == 'sucking'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_Blow.png",
            "R_Tan and newgirl['Mystique'].Mouth == 'kiss'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_Surprised.png",
            "newgirl['Mystique'].Mouth == 'kiss'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_Surprised.png",
            "R_Tan and newgirl['Mystique'].Mouth == 'sad'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_Sad.png",
            "newgirl['Mystique'].Mouth == 'sad'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_Sad.png",
            "R_Tan and newgirl['Mystique'].Mouth == 'smile'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'smile'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_Smile.png",
            "R_Tan and newgirl['Mystique'].Mouth == 'grimace'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'grimace'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_Smile.png",
            "R_Tan and newgirl['Mystique'].Mouth == 'surprised'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_Surprised.png",
            "newgirl['Mystique'].Mouth == 'surprised'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_Surprised.png",
            "R_Tan and newgirl['Mystique'].Mouth == 'tongue'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_Tongue.png",
            "newgirl['Mystique'].Mouth == 'tongue'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_Tongue.png",
            "R_Tan", +str(rogue_doggy_loc)"/Rogue_tDoggy_Mouth_Smile.png",
            "True", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_Smile.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Blush
            "R_Tan and newgirl['Mystique'].Blush and newgirl['Mystique'].Gag == 'ballgag'", +str(rogue_doggy_loc)"/Rogue_tDoggy_BlushEvoBallGag.png",
            "newgirl['Mystique'].Blush and newgirl['Mystique'].Gag == 'ballgag'", +str(rogue_doggy_loc)"/Rogue_Doggy_BlushEvoBallGag.png",
            "R_Tan and newgirl['Mystique'].Blush", +str(rogue_doggy_loc)"/Rogue_tDoggy_BlushEvo.png",
            "newgirl['Mystique'].Blush", +str(rogue_doggy_loc)"/Rogue_Doggy_BlushEvo.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #Mouth
            "newgirl['Mystique'].Gag == 'ringgag'", +str(rogue_doggy_loc)"/Rogue_Doggy_RingGag.png",
            "True", Null(), #Rogue_Doggy_RingGag
            ),
        (0,0), ConditionSwitch(                                                                                 #Brows
            "newgirl['Mystique'].Brows == 'normal'", +str(rogue_doggy_loc)"/Rogue_Doggy_Brows_Normal.png",
            "newgirl['Mystique'].Brows == 'angry'", +str(rogue_doggy_loc)"/Rogue_Doggy_Brows_Angry.png",
            "newgirl['Mystique'].Brows == 'sad'", +str(rogue_doggy_loc)"/Rogue_Doggy_Brows_Sad.png",
            "newgirl['Mystique'].Brows == 'surprised'", +str(rogue_doggy_loc)"/Rogue_Doggy_Brows_Surprised.png",
            "newgirl['Mystique'].Brows == 'confused'", +str(rogue_doggy_loc)"/Rogue_Doggy_Brows_Normal.png",
            "True", +str(rogue_doggy_loc)"/Rogue_Doggy_Brows_Normal.png",
            ),
        (0,0), "Mystique_Rogue Doggy Blink",                                                                             #Eyes
        (0,0), ConditionSwitch(                                                                                 #Collar
            "newgirl['Mystique'].Glasses", +str(rogue_doggy_loc)"/Rogue_Doggy_Glasses.png",
            "True", Null(),                #R_Arms == 'gloved' or not R_Arms
            ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].Water", +str(rogue_doggy_loc)"/Rogue_Doggy_WetTop.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(                                                                                 #Hair
            "newgirl['Mystique'].Water and R_HairColor == 'black'", +str(rogue_doggy_loc)"/Rogue_Doggy_HairBlackWet.png",
            "newgirl['Mystique'].Water and R_HairColor == 'blonde'", +str(rogue_doggy_loc)"/Rogue_Doggy_HairBlondeWet.png",
            "newgirl['Mystique'].Water", +str(rogue_doggy_loc)"/Rogue_Doggy_HairWet.png",
            "R_Hair == 'evo' and R_HairColor == 'black'", +str(rogue_doggy_loc)"/Rogue_Doggy_HairBlackF.png",
            "R_Hair == 'evo' and R_HairColor == 'blonde'", +str(rogue_doggy_loc)"/Rogue_Doggy_HairBlondeF.png",
            "R_Hair == 'evo'", +str(rogue_doggy_loc)"/Rogue_Doggy_HairF.png",
            "True and R_HairColor == 'black'", +str(rogue_doggy_loc)"/Rogue_Doggy_HairBlackF.png",
            "True and R_HairColor == 'blonde'", +str(rogue_doggy_loc)"/Rogue_Doggy_HairBlondeF.png",
            "True", +str(rogue_doggy_loc)"/Rogue_Doggy_HairF.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #face spunk
            "not newgirl['Mystique'].Spunk", Null(),
            "'facial' in newgirl['Mystique'].Spunk", +str(rogue_doggy_loc)"/Rogue_Doggy_Facial.png",
            "True", Null(),
            ),
        )

image Mystique_Rogue_Doggy_Ass = LiveComposite(                                                                                          #Lower body
        (420,750), #(210,375), #(419,750),
        (0,0), ConditionSwitch(                                                                                 #Pussy Composite
            "R_Tan == 'tan1'", +str(rogue_doggy_loc)"/Rogue_t1Doggy_Ass.png",
            "R_Tan == 'tan'", +str(rogue_doggy_loc)"/Rogue_tDoggy_Ass.png",
            "True", +str(rogue_doggy_loc)"/Rogue_Doggy_Ass.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].Water", +str(rogue_doggy_loc)"/Rogue_Doggy_WetAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #Pussy Composite
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Rogue_Pussy_Fucking3",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Rogue_Pussy_Fucking2",
            "P_Sprite and P_Cock == 'in' and Speed", "Rogue_Pussy_Moving",
            "P_Sprite and P_Cock == 'in'", "Rogue_Pussy",
            "Trigger == 'lick pussy'", +str(rogue_doggy_loc)"/Rogue_Doggy_Pussy_Open.png",
            "True", +str(rogue_doggy_loc)"/Rogue_Doggy_Pussy_Closed.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #pubes
            "not newgirl['Mystique'].Pubes", Null(),
            "P_Sprite and P_Cock == 'in'", Null(),
            "True and R_HairColor == 'black'", +str(rogue_doggy_loc)"/Rogue_Doggy_PubesBlack.png",
            "True and R_HairColor == 'blonde'", +str(rogue_doggy_loc)"/Rogue_Doggy_PubesBlonde.png",
            "True", +str(rogue_doggy_loc)"/Rogue_Doggy_Pubes.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Pussy Piercings
            "P_Sprite", Null(),
            "R_Pierce == 'ring'", +str(rogue_doggy_loc)"/Rogue_Doggy_PussyRing.png",
            "R_Pierce == 'barbell'", +str(rogue_doggy_loc)"/Rogue_Doggy_PussyBarbell.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #Anus Composite
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Rogue_Anal_Fucking3",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Rogue_Anal_Fucking2",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Rogue_Anal_Fucking",
            "P_Sprite and P_Cock == 'anal' and Speed", "Rogue_Anal_Heading",
            "P_Sprite and P_Cock == 'anal'", "Rogue_Anal",
            "P_Sprite and P_Cock == 'plug' and Speed", "Rogue_Anal_Plug_Heading",
            "P_Sprite and P_Cock == 'plug' and newgirl['Mystique'].Plugged", +str(rogue_doggy_loc)"/Rogue_Doggy_Plugged.png",
            "P_Sprite and P_Cock == 'plug'", "Rogue_Anal_Plug",
            "newgirl['Mystique'].Plugged", +str(rogue_doggy_loc)"/Rogue_Doggy_Plugged.png",
            "newgirl['Mystique'].Loose", +str(rogue_doggy_loc)"/Rogue_Doggy_Asshole_Loose.png",
            "True", +str(rogue_doggy_loc)"/Rogue_Doggy_Asshole_Tight.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Hose
            #"R_Spank == 0", +str(rogue_doggy_loc)"/Rogue_Doggy_Spank0.png",
            "newgirl['Mystique'].Spank >= 1 and newgirl['Mystique'].Spank <= 4 and newgirl['Mystique'].Plugged", +str(rogue_doggy_loc)"/Rogue_Doggy_SpankPlugged1.png",
            "newgirl['Mystique'].Spank >= 1 and newgirl['Mystique'].Spank <= 4 and (P_Cock == 'anal' or P_Cock == 'plug')", +str(rogue_doggy_loc)"/Rogue_Doggy_SpankAnal1.png",
            "newgirl['Mystique'].Spank >= 1 and newgirl['Mystique'].Spank <= 4", +str(rogue_doggy_loc)"/Rogue_Doggy_Spank1.png",
            "newgirl['Mystique'].Spank >= 5 and newgirl['Mystique'].Spank <= 10 and newgirl['Mystique'].Plugged", +str(rogue_doggy_loc)"/Rogue_Doggy_SpankPlugged2.png",
            "newgirl['Mystique'].Spank >= 5 and newgirl['Mystique'].Spank <= 10 and (P_Cock == 'anal' or P_Cock == 'plug')", +str(rogue_doggy_loc)"/Rogue_Doggy_SpankAnal2.png",
            "newgirl['Mystique'].Spank >= 5 and newgirl['Mystique'].Spank <= 10", +str(rogue_doggy_loc)"/Rogue_Doggy_Spank2.png",
            "newgirl['Mystique'].Spank >= 11 and newgirl['Mystique'].Plugged", +str(rogue_doggy_loc)"/Rogue_Doggy_SpankPlugged3.png",
            "newgirl['Mystique'].Spank >= 11 and (P_Cock == 'anal' or P_Cock == 'plug')", +str(rogue_doggy_loc)"/Rogue_Doggy_SpankAnal3.png",
            "newgirl['Mystique'].Spank >= 11", +str(rogue_doggy_loc)"/Rogue_Doggy_Spank3.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #spunkanal Layer
            "'anal' in newgirl['Mystique'].Spunk and P_Sprite", Null(),
            "'anal' in newgirl['Mystique'].Spunk and P_Cock == 'anal'", +str(rogue_doggy_loc)"/Rogue_Doggy_SpunkAnalOpen.png",
            "'anal' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Loose", +str(rogue_doggy_loc)"/Rogue_Doggy_SpunkAnalLoose.png",
            "'anal' in newgirl['Mystique'].Spunk", +str(rogue_doggy_loc)"/Rogue_Doggy_SpunkAnalLoose.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #spunkass Layer
            "'back' in newgirl['Mystique'].Spunk", +str(rogue_doggy_loc)"/Rogue_Doggy_SpunkAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #Hotdogging underlayer
            "not P_Sprite or P_Cock != 'out'", Null(),
            "True", +str(rogue_doggy_loc)"/Rogue_Doggy_HotdogBack.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Hotdogging Cock w/ alpha
            "not P_Sprite or P_Cock != 'out'", Null(),
            "Speed", AlphaMask("Zero_Hotdog_Moving", +str(rogue_doggy_loc)"/Rogue_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_Hotdog_Static", +str(rogue_doggy_loc)"/Rogue_Doggy_HotdogMask.png"),
            ),
        (0,0), ConditionSwitch(                                                                                 #UI tool layer
            "not UI_Tool", Null(),
            "UI_Tool", "Slap_Ass",
            #"not UI_Tool", "Slap_Ass",
            "True", Null(),
            ),
        )

image Mystique_Rogue Doggy Blink:                                                                                        #Eyes
    ConditionSwitch(
    "newgirl['Mystique'].Eyes == 'sexy'", +str(rogue_doggy_loc)"/Rogue_Doggy_Eyes_Sexy.png",
    "newgirl['Mystique'].Eyes == 'side'", +str(rogue_doggy_loc)"/Rogue_Doggy_Eyes_Side.png",
    "newgirl['Mystique'].Eyes == 'normal'", +str(rogue_doggy_loc)"/Rogue_Doggy_Eyes_Normal.png",
    "newgirl['Mystique'].Eyes == 'closed'", +str(rogue_doggy_loc)"/Rogue_Doggy_Eyes_Closed.png",
    "newgirl['Mystique'].Eyes == 'manic'", +str(rogue_doggy_loc)"/Rogue_Doggy_Eyes_Surprised.png",
    "newgirl['Mystique'].Eyes == 'down'", +str(rogue_doggy_loc)"/Rogue_Doggy_Eyes_Sexy.png",
    "newgirl['Mystique'].Eyes == 'stunned'", +str(rogue_doggy_loc)"/Rogue_Doggy_Eyes_Stunned.png",
    "newgirl['Mystique'].Eyes == 'surprised'", +str(rogue_doggy_loc)"/Rogue_Doggy_Eyes_Surprised.png",
    "newgirl['Mystique'].Eyes == 'squint'", +str(rogue_doggy_loc)"/Rogue_Doggy_Eyes_Sexy.png",
    "True", +str(rogue_doggy_loc)"/Rogue_Doggy_Eyes_Normal.png",
    ),
    3
    # This randomizes the time between blinking.
    +str(rogue_doggy_loc)"/Rogue_Doggy_Eyes_Closed.png"
    .25
    repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                                                                                  #Insert cock animations

image Mystique_Rogue_Doggy_Fuck3_Top:                #animation for anal fucking2 top half
    contains:
        subpixel True
        "Mystique_Rogue_Doggy_Body"
        ypos 20
        block:
            pause .15
            ease .1 ypos 0
            pause .1
            easein .2 ypos 20
            pause .05
            repeat

image Mystique_Rogue_Doggy_Fuck3_Ass:                #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Mystique_Rogue_Doggy_Ass"
        ypos 5
        block:
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .1 ypos 5
            pause .05
            repeat #.90


image Mystique_Rogue_Doggy_Fuck2_Top:                #animation for anal fucking2 top half
    contains:
        subpixel True
        "Mystique_Rogue_Doggy_Body"
        ypos 20
        block:
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20
            pause .05
            repeat

image Mystique_Rogue_Doggy_Fuck2_Ass:                #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Mystique_Rogue_Doggy_Ass"
        ypos 5
        block:
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .4 ypos 5
            pause .05
            repeat

image Mystique_Rogue_Doggy_Fuck_Top:                #animation for anal fucking top half
    contains:
        subpixel True
        "Mystique_Rogue_Doggy_Body"
        ypos 15#28
        pause .4
        block:
            ease .2 ypos 5#10
            pause .3
            ease 2 ypos 15#28
            repeat

image Mystique_Rogue_Doggy_Fuck_Ass:                #animation for anal fucking ass half
    contains:
        subpixel True
        "Mystique_Rogue_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0
            repeat

image Mystique_Rogue_Doggy_Anal_Head_Top:                #animation for anal fucking top half
    contains:
        subpixel True
        "Mystique_Rogue_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Mystique_Rogue_Doggy_Anal_Head_Ass:                #animation for anal fucking ass half
    contains:
        subpixel True
        "Mystique_Rogue_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easein .1 ypos -7
            easeout .9 ypos 0
            pause .9
            repeat
















# Kitty Section ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
image Mystique_Kitty_Doggy:
    LiveComposite(                                                                                 #Base body
        (420,750),
        (0,0), ConditionSwitch(                                                         #Shows different upper body motion depending on events
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Mystique_Kitty_Doggy_Fuck3_Top",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Mystique_Kitty_Doggy_Fuck2_Top",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Mystique_Kitty_Doggy_Fuck_Top",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Kitty_Doggy_Anal_Head_Top",
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Mystique_Kitty_Doggy_Fuck2_Top",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Mystique_Kitty_Doggy_Fuck_Top",
            "True", "Mystique_Kitty_Doggy_Body",
            ),
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Mystique_Kitty_Doggy_Fuck3_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Mystique_Kitty_Doggy_Fuck2_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Mystique_Kitty_Doggy_Fuck_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Kitty_Doggy_Anal_Head_Ass",
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Mystique_Kitty_Doggy_Fuck2_Ass",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Mystique_Kitty_Doggy_Fuck_Ass",
            "True", "Mystique_Kitty_Doggy_Ass",
            ),
        )
    align (0.6,0.0)


image Mystique_Kitty_Doggy_Body = LiveComposite(                                                                                         #Upper body
        (420,750),
        (0,0), ConditionSwitch(                                                                                 #Hair underlayer
            "K_HairColor == 'blonde' and K_Hair == 'long'", +str(kitty_doggy_loc)"/Kitty_Doggy_Hair_Blonde.png",
            "K_HairColor == 'blonde' and K_Hair == 'evo'", +str(kitty_doggy_loc)"/Kitty_Doggy_Hair_Ponytail_Blonde.png",
            "K_HairColor == 'red' and K_Hair == 'long'", +str(kitty_doggy_loc)"/Kitty_Doggy_Hair_Red.png",
            "K_HairColor == 'red' and K_Hair == 'evo'", +str(kitty_doggy_loc)"/Kitty_Doggy_Hair_Ponytail_Red.png",
            "K_HairColor == 'black' and K_Hair == 'long'", +str(kitty_doggy_loc)"/Kitty_Doggy_Hair_Black.png",
            "K_HairColor == 'black' and K_Hair == 'evo'", +str(kitty_doggy_loc)"/Kitty_Doggy_Hair_Ponytail_Black.png",
            "K_Hair == 'long'", +str(kitty_doggy_loc)"/Kitty_Doggy_Hair.png",
            "K_Hair == 'evo'", +str(kitty_doggy_loc)"/Kitty_Doggy_Hair_Ponytail.png",
            "True", +str(kitty_doggy_loc)"/Kitty_Doggy_Hair.png",
            ),
        (0,0), ConditionSwitch(
            "K_Tan", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Body.png",
            "K_Tan == 'tan3'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Body.png",
            "True", +str(kitty_doggy_loc)"/Kitty_Doggy_Body.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Mouth
            "K_Tan", Null(),
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Gag", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_BlowW.png",
            "newgirl['Mystique'].Gag", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_Blow.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'lipbite'", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_LipbiteW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'surprised'", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_SurprisedW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sucking'", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_BlowW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sad'", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_SadW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'smile'", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_SmileW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'tongue'", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_TongueW.png",
            "'mouth' in newgirl['Mystique'].Spunk", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_NormalW.png",
            "newgirl['Mystique'].Mouth == 'normal'", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_Normal.png",
            "newgirl['Mystique'].Mouth == 'lipbite'", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_Lipbite.png",
            "newgirl['Mystique'].Mouth == 'sucking'", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_Blow.png",
            "newgirl['Mystique'].Mouth == 'kiss'", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_Surprised.png",
            "newgirl['Mystique'].Mouth == 'sad'", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_Sad.png",
            "newgirl['Mystique'].Mouth == 'smile'", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'grimace'", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'surprised'", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_Surprised.png",
            "newgirl['Mystique'].Mouth == 'tongue'", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_Tongue.png",
            "True", +str(kitty_doggy_loc)"/Kitty_Doggy_Mouth_Smile.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Mouth
            #"R_Gag == 'ballgag'", +str(rogue_doggy_loc)"/Rogue_Doggy_BallGagTop.png",
            #"'mouth' in R_Spunk and R_Gag == 'ringgag'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_BlowW.png",
            #"R_Gag == 'ringgag'", +str(rogue_doggy_loc)"/Rogue_Doggy_Mouth_Blow.png",
            "not K_Tan", Null(),
            "'mouth' in K_Spunk and K_Gag", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_BlowW.png",
            "K_Gag", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_Blow.png",
            "'mouth' in K_Spunk and K_Mouth == 'lipbite'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_LipbiteW.png",
            "'mouth' in K_Spunk and K_Mouth == 'surprised'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_SurprisedW.png",
            "'mouth' in K_Spunk and K_Mouth == 'sucking'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_BlowW.png",
            "'mouth' in K_Spunk and K_Mouth == 'sad'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_SadW.png",
            "'mouth' in K_Spunk and K_Mouth == 'smile'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_SmileW.png",
            "'mouth' in K_Spunk and K_Mouth == 'tongue'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_TongueW.png",
            "'mouth' in K_Spunk", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_NormalW.png",
            "K_Mouth == 'normal'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_Normal.png",
            "K_Mouth == 'lipbite'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_Lipbite.png",
            "K_Mouth == 'sucking'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_Blow.png",
            "K_Mouth == 'kiss'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_Surprised.png",
            "K_Mouth == 'sad'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_Sad.png",
            "K_Mouth == 'smile'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_Smile.png",
            "K_Mouth == 'grimace'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_Smile.png",
            "K_Mouth == 'surprised'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_Surprised.png",
            "K_Mouth == 'tongue'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_Tongue.png",
            "True", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Mouth_Smile.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Mouth
            "newgirl['Mystique'].Gag == 'ballgag'", +str(kitty_doggy_loc)"/Kitty_Doggy_Ballgag.png",
            "True", Null(), #Kitty_Doggy_Gag
            ),
        (0,0), ConditionSwitch(                                                                                 #Brows
            "newgirl['Mystique'].Brows == 'normal'", +str(kitty_doggy_loc)"/Kitty_Doggy_Brows_Normal.png",
            "newgirl['Mystique'].Brows == 'angry'", +str(kitty_doggy_loc)"/Kitty_Doggy_Brows_Angry.png",
            "newgirl['Mystique'].Brows == 'sad'", +str(kitty_doggy_loc)"/Kitty_Doggy_Brows_Sad.png",
            "newgirl['Mystique'].Brows == 'surprised'", +str(kitty_doggy_loc)"/Kitty_Doggy_Brows_Surprised.png",
            "newgirl['Mystique'].Brows == 'confused'", +str(kitty_doggy_loc)"/Kitty_Doggy_Brows_Normal.png",
            "True", +str(kitty_doggy_loc)"/Kitty_Doggy_Brows_Normal.png",
            ),
        (0,0), "Mystique_Kitty Doggy Blink",
        (0,0), ConditionSwitch(
            "newgirl['Mystique'].Blindfold", +str(kitty_doggy_loc)"/Kitty_Doggy_Blindfold.png",
            "True", Null(),
            ),                                                                             #Eyes
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].Water", +str(rogue_doggy_loc)"/Rogue_Doggy_WetTop.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #Hair
            "K_HairColor == 'blonde' and K_Hair == 'long'", +str(kitty_doggy_loc)"/Kitty_Doggy_Hair_Blonde.png",
            "K_HairColor == 'blonde' and K_Hair == 'evo'", +str(kitty_doggy_loc)"/Kitty_Doggy_Hair_Ponytail_Blonde.png",
            "K_HairColor == 'red' and K_Hair == 'long'", +str(kitty_doggy_loc)"/Kitty_Doggy_Hair_Red.png",
            "K_HairColor == 'red' and K_Hair == 'evo'", +str(kitty_doggy_loc)"/Kitty_Doggy_Hair_Ponytail_Red.png",
            "K_HairColor == 'black' and K_Hair == 'long'", +str(kitty_doggy_loc)"/Kitty_Doggy_Hair_Black.png",
            "K_HairColor == 'black' and K_Hair == 'evo'", +str(kitty_doggy_loc)"/Kitty_Doggy_Hair_Ponytail_Black.png",
            "K_Hair == 'long'", +str(kitty_doggy_loc)"/Kitty_Doggy_Hair.png",
            "K_Hair == 'evo'", +str(kitty_doggy_loc)"/Kitty_Doggy_Hair_Ponytail.png",
            "True", +str(kitty_doggy_loc)"/Kitty_Doggy_Hair.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "K_Tan", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Ear.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "newgirl['Mystique'].Headband == 'pink'", +str(kitty_doggy_loc)"/Kitty_Doggy_Headband_Pink.png",
            "newgirl['Mystique'].Headband == 'black'", +str(kitty_doggy_loc)"/Kitty_Doggy_Headband_Black.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #face spunk
            "not newgirl['Mystique'].Spunk", Null(),
            "'facial' in newgirl['Mystique'].Spunk", +str(rogue_doggy_loc)"/Rogue_Doggy_Facial.png",
            "True", Null(),
            ),
        )

image Mystique_Kitty_Doggy_Ass = LiveComposite(                                                                                          #Lower body
        (420,750), #(210,375), #(419,750),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "K_Tan", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Ass.png",
            "K_Tan == 'tan3'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Ass.png",
            "True", +str(kitty_doggy_loc)"/Kitty_Doggy_Ass.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].Water", +str(rogue_doggy_loc)"/Rogue_Doggy_WetAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #Pussy Composite
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Kitty_Pussy_Fucking3",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Kitty_Pussy_Fucking2",
            "P_Sprite and P_Cock == 'in' and Speed", "Kitty_Pussy_Moving",
            "P_Sprite and P_Cock == 'in'", "Kitty_Pussy",
            "K_Tan and Trigger == 'lick pussy'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Pussy_Open.png",
            "K_Tan == 'tan3' and Trigger == 'lick pussy'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Pussy_Open.png",
            "Trigger == 'lick pussy'", +str(kitty_doggy_loc)"/Kitty_Doggy_Pussy_Open.png",
            "K_Tan", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Pussy_Closed.png",
            "K_Tan == 'tan3'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Pussy_Closed.png",
            "True", +str(kitty_doggy_loc)"/Kitty_Doggy_Pussy_Closed.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Pussy Piercings
            "P_Sprite", Null(),
            "K_Pierce == 'ring'", +str(kitty_doggy_loc)"/Kitty_Doggy_Pussy_Ring.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #Anus Composite
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Kitty_Doggy_Anal_Fucking3",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Kitty_Doggy_Anal_Fucking2",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Kitty_Doggy_Anal_Fucking",
            "P_Sprite and P_Cock == 'anal' and Speed", "Kitty_Doggy_Anal_Heading",
            "P_Sprite and P_Cock == 'anal'", "Kitty_Anal",
            "P_Sprite and P_Cock == 'plug' and Speed", "Kitty_Anal_Plug_Heading",
            "P_Sprite and P_Cock == 'plug' and K_Plugged", +str(kitty_doggy_loc)"/Kitty_Doggy_Plugged.png",
            "P_Sprite and P_Cock == 'plug'", "Kitty_Anal_Plug",
            "newgirl['Mystique'].Plugged", +str(kitty_doggy_loc)"/Kitty_Doggy_Plugged.png",
            "K_Tan and newgirl['Mystique'].Loose", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Asshole_Loose.png",
            "K_Tan == 'tan3' and K_Loose", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Asshole_Loose.png",
            "newgirl['Mystique'].Loose", +str(kitty_doggy_loc)"/Kitty_Doggy_Asshole_Loose.png",
            "K_Tan", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Asshole_Tight.png",
            "K_Tan == 'tan3'", +str(kitty_doggy_loc)"/Kitty_Doggy_T3Asshole_Tight.png",
            "True", +str(kitty_doggy_loc)"/Kitty_Doggy_Asshole_Tight.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Hose
            "newgirl['Mystique'].Spank >= 1 and newgirl['Mystique'].Spank <= 4 and newgirl['Mystique'].Plugged", +str(kitty_doggy_loc)"/Kitty_Doggy_SpankPlugged1.png",
            "newgirl['Mystique'].Spank >= 1 and newgirl['Mystique'].Spank <= 4 and (P_Cock == 'anal' or P_Cock == 'plug')", +str(kitty_doggy_loc)"/Kitty_Doggy_SpankAnal1.png",
            "newgirl['Mystique'].Spank >= 1 and newgirl['Mystique'].Spank <= 4", +str(kitty_doggy_loc)"/Kitty_Doggy_Spank1.png",
            "newgirl['Mystique'].Spank >= 5 and newgirl['Mystique'].Spank <= 10 and newgirl['Mystique'].Plugged", +str(kitty_doggy_loc)"/Kitty_Doggy_SpankPlugged2.png",
            "newgirl['Mystique'].Spank >= 5 and newgirl['Mystique'].Spank <= 10 and (P_Cock == 'anal' or P_Cock == 'plug')", +str(kitty_doggy_loc)"/Kitty_Doggy_SpankAnal2.png",
            "newgirl['Mystique'].Spank >= 5 and newgirl['Mystique'].Spank <= 10", +str(kitty_doggy_loc)"/Kitty_Doggy_Spank2.png",
            "newgirl['Mystique'].Spank >= 11 and newgirl['Mystique'].Plugged", +str(kitty_doggy_loc)"/Kitty_Doggy_SpankPlugged3.png",
            "newgirl['Mystique'].Spank >= 11 and (P_Cock == 'anal' or P_Cock == 'plug')", +str(kitty_doggy_loc)"/Kitty_Doggy_SpankAnal3.png",
            "newgirl['Mystique'].Spank >= 11", +str(kitty_doggy_loc)"/Kitty_Doggy_Spank3.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #spunkanal Layer
            "'anal' in newgirl['Mystique'].Spunk and P_Sprite", Null(),
            "'anal' in newgirl['Mystique'].Spunk and P_Cock == 'anal'", +str(rogue_doggy_loc)"/Rogue_Doggy_SpunkAnalOpen.png",
            "'anal' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Loose", +str(rogue_doggy_loc)"/Rogue_Doggy_SpunkAnalLoose.png",
            "'anal' in newgirl['Mystique'].Spunk", +str(rogue_doggy_loc)"/Rogue_Doggy_SpunkAnalLoose.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #spunkass Layer
            "'back' in newgirl['Mystique'].Spunk", +str(rogue_doggy_loc)"/Rogue_Doggy_SpunkAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #Hotdogging underlayer
            "not P_Sprite or P_Cock != 'out'", Null(),
            "True", +str(rogue_doggy_loc)"/Rogue_Doggy_HotdogBack.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Hotdogging Cock w/ alpha
            "not P_Sprite or P_Cock != 'out'", Null(),
            "Speed", AlphaMask("Zero_Hotdog_Moving", +str(rogue_doggy_loc)"/Rogue_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_Hotdog_Static", +str(rogue_doggy_loc)"/Rogue_Doggy_HotdogMask.png"),
            ),
        (0,0), ConditionSwitch(                                                                                 #UI tool layer
            "not UI_Tool", Null(),
            "UI_Tool", "Slap_Ass",
            "True", Null(),
            ),
        )

image Mystique_Kitty Doggy Blink:                                                                                        #Eyes
    ConditionSwitch(
    "newgirl['Mystique'].Eyes == 'sexy'", +str(kitty_doggy_loc)"/Kitty_Doggy_Eyes_Sexy.png",
    "newgirl['Mystique'].Eyes == 'side'", +str(kitty_doggy_loc)"/Kitty_Doggy_Eyes_Side.png",
    "newgirl['Mystique'].Eyes == 'normal'", +str(kitty_doggy_loc)"/Kitty_Doggy_Eyes_Normal.png",
    "newgirl['Mystique'].Eyes == 'closed'", +str(kitty_doggy_loc)"/Kitty_Doggy_Eyes_Closed.png",
    "newgirl['Mystique'].Eyes == 'manic'", +str(kitty_doggy_loc)"/Kitty_Doggy_Eyes_Surprised.png",
    "newgirl['Mystique'].Eyes == 'down'", +str(kitty_doggy_loc)"/Kitty_Doggy_Eyes_Sexy.png",
    "newgirl['Mystique'].Eyes == 'stunned'", +str(kitty_doggy_loc)"/Kitty_Doggy_Eyes_Stunned.png",
    "newgirl['Mystique'].Eyes == 'surprised'", +str(kitty_doggy_loc)"/Kitty_Doggy_Eyes_Surprised.png",
    "newgirl['Mystique'].Eyes == 'squint'", +str(kitty_doggy_loc)"/Kitty_Doggy_Eyes_Sexy.png",
    "True", +str(kitty_doggy_loc)"/Kitty_Doggy_Eyes_Normal.png",
    ),
    3
    # This randomizes the time between blinking.
    +str(kitty_doggy_loc)"/Kitty_Doggy_Eyes_Closed.png"
    .25
    repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                                                                                  #Insert cock animations

image Mystique_Kitty_Doggy_Fuck3_Top:                #animation for anal fucking2 top half
    contains:
        subpixel True
        "Mystique_Kitty_Doggy_Body"
        ypos 20
        block:
            pause .15
            ease .1 ypos 0
            pause .1
            easein .2 ypos 20
            pause .05
            repeat

image Mystique_Kitty_Doggy_Fuck3_Ass:                #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Mystique_Kitty_Doggy_Ass"
        ypos 5
        block:
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .1 ypos 5
            pause .05
            repeat #.90


image Mystique_Kitty_Doggy_Fuck2_Top:                #animation for anal fucking2 top half
    contains:
        subpixel True
        "Mystique_Kitty_Doggy_Body"
        ypos 20
        block:
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20
            pause .05
            repeat

image Mystique_Kitty_Doggy_Fuck2_Ass:                #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Mystique_Kitty_Doggy_Ass"
        ypos 5
        block:
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .4 ypos 5
            pause .05
            repeat

image Mystique_Kitty_Doggy_Fuck_Top:                #animation for anal fucking top half
    contains:
        subpixel True
        "Mystique_Kitty_Doggy_Body"
        ypos 15#28
        pause .4
        block:
            ease .2 ypos 5#10
            pause .3
            ease 2 ypos 15#28
            repeat

image Mystique_Kitty_Doggy_Fuck_Ass:                #animation for anal fucking ass half
    contains:
        subpixel True
        "Mystique_Kitty_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0
            repeat

image Mystique_Kitty_Doggy_Anal_Head_Top:                #animation for anal fucking top half
    contains:
        subpixel True
        "Mystique_Kitty_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Mystique_Kitty_Doggy_Anal_Head_Ass:                #animation for anal fucking ass half
    contains:
        subpixel True
        "Mystique_Kitty_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easein .1 ypos -7
            easeout .9 ypos 0
            pause .9
            repeat
