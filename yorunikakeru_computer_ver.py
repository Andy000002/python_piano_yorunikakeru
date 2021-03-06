import winsound,time
tone = [
    156,175,196,208,233,262,294,
    311,349,392,415,466,523,587,
    622,698,784,831,932,1047
]
spec = [
    0,247,  #B3 verse   1-3 
    988,    #B5 verse   8-3
    494     #B4 chorus  2-4
]
full = [
    3,5,6,4,3,2,1,              2,6,5,6,3,2,1,              -1,1,2,0,4,3,10,                9,7,1,7,5,6,5,
    3,5,6,4,3,2,7,              6,5,5,6,7,8,3,              3,2,1,3,10,                     9,7,

    -2,-1,1,5,6,5,3,-1,1,2,     3,-1,8,7,5,3,5,6,5,3,       2,-1,3,2,1,-1,100,4,            3,0,2,1,5,4,3,-2,           #100 = B3(247)
    -2,-1,1,5,6,5,3,-1,1,2,     3,-1,8,7,5,3,5,6,5,3,       2,-1,1,5,3,2,1,-1,100,4,        3,0,-2,-1,1,2,3,6,5,2,3,-1,    
    1,6,7,8,7,5,                3,5,6,5,5,6,                8,9,10,6,6,10,9,12,             11,11,10,10,13,12,
    10,9,8,6,8,6,8,9,           8,7,10,7,5,6,               6,7,8,9,10,9,8,                 7,7,6,6,
    5,6,7,8,7,5,                3,5,6,5,5,6,                8,9,10,9,10,12,13,12,           10,9,10,10,13,12,
    10,9,8,6,8,6,8,9,           8,7,9,7,5,6,                6,7,8,9,10,9,8,                 7,7,6,5,5,
    5,6,6,8,8,6,10,10,          9,10,9,5,5,5,6,10,10,10,    12,12,12,10,6,6,8,8,9,10,8,6,   8,6,8,9,10,11,12,10,
    9,8,6,8,10,9,8,             8,9,10,200,10,9,8,          7,5,6,5,6,8,6,                  8,11,10,8,                  #200 = B5(988)

    7,5,5,6,3,2,1,              2,6,5,3,3,2,1,              1,5,4,3,2,1,0,1,                2,4,3,1,6,5,
    3,5,6,4,3,2,1,              2,6,5,6,3,2,1,              -1,0,1,-1,1,2,3,1,              3,6,300,1,1,8,
    7,5,5,6,3,2,1,              2,6,5,3,3,2,1,              1,5,4,3,2,1,0,1,                2,4,3,2,3,6,5,
    3,5,6,4,3,2,7,              6,5,300,6,7,8,3,            2,1,-1,1,4,3,1,                 2,1,6,5,3,-1,1,2,           #300 = B4(494)

    3,-1,8,7,5,3,5,6,5,3,       2,-1,3,2,1,-1,100,4,        3,0,2,1,5,4,3,-2,               -2,-1,1,5,6,5,3,-1,1,2, 
    3,-1,8,7,5,3,5,6,5,3,       2,-1,1,5,3,2,1,-1,100,4,    3,0,-2,-1,1,2,3,6,5,2,3,-1,     1,
]
full_dur = [
    1,1,1.5,1.5,1,1,1,                      1,1,1,0.5,1,1.5,2,                  1,1,1.5,1.5,1,1,1,                                  1,1,1.5,1.5,1,1,1,
    1,1,1.5,1.5,1,1,1,                      1,1,1,1,1,2,1,                      1,1,4,1,1,                                          1,7,

    0.5,0.5,0.5,0.5,0.5,1,1.5,1,1,1,        0.5,0.5,0.5,0.5,0.5,1,1.5,1,1,1,    1,1,0.5,1,1.5,1,1,1,                                1,1,1,0.5,1.5,1,1,1,
    0.5,0.5,0.5,0.5,0.5,1,1.5,1,1,1,        0.5,0.5,0.5,0.5,0.5,1,1.5,1,1,1,    0.5,0.5,0.5,0.5,0.5,1,1.5,1,1,1,                    1,2,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
    2,1,1,1,2,1,                            1,2,2,1,1,1,                        1,1,1,1,1,1,1,1,                                    1,2,2,1,1,1,
    1,1,1,1,1,1,1.5,2,                      1,1,0.5,1.5,1,1.5,                  1,1,1,1,1,2,1,                                      1,2,1,5,
    1,1,1,1,2,1,                            1,2,2,1,1,1,                        1,1,1,1,1,1,1,1,                                    1,2,2,1,1,1,
    1,1,1,1,1,1,1.5,2,                      1,1,0.5,1.5,1,1.5,                  1,1,1,1,1,2,1,                                      1,2,4,0.5,0.5,
    1,1,1.5,1.5,1.5,0.5,0.5,0.5,            1,1,1,0.5,1,0.5,1.5,0.5,0.5,0.5,    0.5,0.5,0.5,1.5,0.5,0.5,0.5,0.5,0.5,1.5,0.5,0.5,    0.5,0.5,0.5,3.5,1,1,0.5,1,    
    0.5,2,1,1,1,1,1,                        1,1,1,1,1,2,1,                      1,1,1,1,1,2,1,                                      1,1,5,1,

    1,1,1.5,1.5,1,1,1,                      1,1,1,0.5,1,1.5,2,                  1,1,1,1,1,1,1,1,                                    1,1,1.5,1.5,1,2,
    1,1,1.5,1.5,1,1,1,                      1,1,1,0.5,1,1.5,2,                  1,1,1,1,1,1,1,1,                                    1,1,3,1,1,1,
    1,1,1.5,1.5,1,1,1,                      1,1,1,0.5,1,1.5,2,                  1,1,1,1,1,1,1,1,                                    1,1,1,0.5,1,1.5,2,
    1,1,1.5,1.5,1,1,1,                      1,1,1,1,1,2,1,                      1,2,1,1,0.5,1.5,1,                                  1,1,0.5,1,1.5,1,1,1,

    0.5,0.5,0.5,0.5,0.5,1,1.5,1,1,1,        1,1,0.5,1,1.5,1,1,1,                1,1,1,0.5,1.5,1,1,1,                                0.5,0.5,0.5,0.5,0.5,1,1.5,1,1,1,
    0.5,0.5,0.5,0.5,0.5,1,1.5,1,1,1,        0.5,0.5,0.5,0.5,0.5,1,1.5,1,1,1,    1,2,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,        2
]
# full
for i in range(len(full)):
    print(full[i],full_dur[i])
    if(full[i]<100):
        winsound.Beep(tone[full[i]+6],int(full_dur[i]*230))
    else:
        winsound.Beep(spec[int(full[i]/100)],int(full_dur[i]*230))

#B0  31
#C1  33
#CS1 35
#D1  37
#DS1 39
#E1  41
#F1  44
#FS1 46
#G1  49
#GS1 52
#A1  55
#AS1 58
#B1  62
#C2  65
#CS2 69
#D2  73
#DS2 78
#E2  82
#F2  87
#FS2 93
#G2  98
#GS2 104
#A2  110
#AS2 117
#B2  123
#C3  131
#CS3 139
#D3  147
#DS3 156
#E3  165
#F3  175
#FS3 185
#G3  196
#GS3 208
#A3  220
#AS3 233
#B3  247
#C4  262
#CS4 277
#D4  294
#DS4 311
#E4  330
#F4  349
#FS4 370
#G4  392
#GS4 415
#A4  440
#AS4 466
#B4  494
#C5  523
#CS5 554
#D5  587
#DS5 622
#E5  659
#F5  698
#FS5 740
#G5  784
#GS5 831
#A5  880
#AS5 932
#B5  988
#C6  1047
#CS6 1109
#D6  1175
#DS6 1245
#E6  1319
#F6  1397
#FS6 1480
#G6  1568
#GS6 1661
#A6  1760
#AS6 1865
#B6  1976
#C7  2093
#CS7 2217
#D7  2349
#DS7 2489
#E7  2637
#F7  2794
#FS7 2960
#G7  3136
#GS7 3322
#A7  3520
#AS7 3729
#B7  3951
#C8  4186
#CS8 4435
#D8  4699
#DS8 4978






# start = [
#     3,5,6,4,3,2,1,  2,6,5,6,3,2,1,  -1,1,2,0,4,3,10,    9,7,1,7,5,6,5,
#     3,5,6,4,3,2,7,  6,5,5,6,7,8,3,  3,2,1,3,10,         9,7,
# ]
# verse = [
#     -2,-1,1,5,6,5,3,-1,1,2,     3,-1,8,7,5,3,5,6,5,3,       2,-1,3,2,1,-1,100,4,            3,0,2,1,5,4,3,-2,
#     -2,-1,1,5,6,5,3,-1,1,2,     3,-1,8,7,5,3,5,6,5,3,       2,-1,1,5,3,2,1,-1,100,4,        3,0,-2,-1,1,2,3,6,5,2,3,-1,    #100 = B3(247)
#     1,6,7,8,7,5,                3,5,6,5,5,6,                8,9,10,6,6,10,9,12,             11,11,10,10,13,12,
#     10,9,8,6,8,6,8,9,           8,7,10,7,5,6,               6,7,8,9,10,9,8,                 7,7,6,6,
#     5,6,7,8,7,5,                3,5,6,5,5,6,                8,9,10,9,10,12,13,12,           10,9,10,10,13,12,
#     10,9,8,6,8,6,8,9,           8,7,9,7,5,6,                6,7,8,9,10,9,8,                 7,7,6,5,5,
#     5,6,6,8,8,6,10,10,          9,10,9,5,5,5,6,10,10,10,    12,12,12,10,6,6,8,8,9,10,8,6,   8,6,8,9,10,11,12,10,
#     9,8,6,8,10,9,8,             8,9,10,200,10,9,8,          7,5,6,5,6,8,6,                  8,11,10,8   #200 = B5(988)
# ]
# chorus = [
#     7,5,5,6,3,2,1,  2,6,5,3,3,2,1,      1,5,4,3,2,1,0,1,    2,4,3,1,6,5,
#     3,5,6,4,3,2,1,  2,6,5,6,3,2,1,      -1,0,1,-1,1,2,3,1,  3,6,300,1,1,8,
#     7,5,5,6,3,2,1,  2,6,5,3,3,2,1,      1,5,4,3,2,1,0,1,    2,4,3,2,3,6,5,
#     3,5,6,4,3,2,7,  6,5,300,6,7,8,3,    2,1,-1,1,4,3,1,     2,1,6,5,3,-1,1,2
# ]
# end = [
#     3,-1,8,7,5,3,5,6,5,3,   2,-1,3,2,1,-1,100,4,        3,0,2,1,5,4,3,-2,               -2,-1,1,5,6,5,3,-1,1,2, 
#     3,-1,8,7,5,3,5,6,5,3,   2,-1,1,5,3,2,1,-1,100,4,    3,0,-2,-1,1,2,3,6,5,2,3,-1,     1,  #100 = B3(247)
# ]
# start_dur = [
#     1,1,1.5,1.5,1,1,1,  1,1,1,0.5,1,1.5,2,  1,1,1.5,1.5,1,1,1,  1,1,1.5,1.5,1,1,1,
#     1,1,1.5,1.5,1,1,1,  1,1,1,1,1,2,1,      1,1,4,1,1,          1,7,
# ]
# verse_dur = [
#     0.5,0.5,0.5,0.5,0.5,1,1.5,1,1,1,    0.5,0.5,0.5,0.5,0.5,1,1.5,1,1,1,    1,1,0.5,1,1.5,1,1,1,                                1,1,1,0.5,1.5,1,1,1,
#     0.5,0.5,0.5,0.5,0.5,1,1.5,1,1,1,    0.5,0.5,0.5,0.5,0.5,1,1.5,1,1,1,    0.5,0.5,0.5,0.5,0.5,1,1.5,1,1,1,                    1,2,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
#     2,1,1,1,2,1,                        1,2,2,1,1,1,                        1,1,1,1,1,1,1,1,                                    1,2,2,1,1,1,
#     1,1,1,1,1,1,1.5,2,                  1,1,0.5,1.5,1,1.5,                  1,1,1,1,1,2,1,                                      1,2,1,5,
#     1,1,1,1,2,1,                        1,2,2,1,1,1,                        1,1,1,1,1,1,1,1,                                    1,2,2,1,1,1,
#     1,1,1,1,1,1,1.5,2,                  1,1,0.5,1.5,1,1.5,                  1,1,1,1,1,2,1,                                      1,2,4,0.5,0.5,
#     1,1,1.5,1.5,1.5,0.5,0.5,0.5,        1,1,1,0.5,1,0.5,1.5,0.5,0.5,0.5,    0.5,0.5,0.5,1.5,0.5,0.5,0.5,0.5,0.5,1.5,0.5,0.5,    0.5,0.5,0.5,3.5,1,1,0.5,1,    
#     0.5,2,1,1,1,1,1,                    1,1,1,1,1,2,1,                      1,1,1,1,1,2,1,                                      1,1,5,1
# ]
# chorus_dur = [
#     1,1,1.5,1.5,1,1,1,  1,1,1,0.5,1,1.5,2,  1,1,1,1,1,1,1,1,    1,1,1.5,1.5,1,2,
#     1,1,1.5,1.5,1,1,1,  1,1,1,0.5,1,1.5,2,  1,1,1,1,1,1,1,1,    1,1,3,1,1,1,
#     1,1,1.5,1.5,1,1,1,  1,1,1,0.5,1,1.5,2,  1,1,1,1,1,1,1,1,    1,1,1,0.5,1,1.5,2,
#     1,1,1.5,1.5,1,1,1,  1,1,1,1,1,2,1,      1,2,1,1,0.5,1.5,1,  1,1,0.5,1,1.5,1,1,1
# ]

# end_dur = [
#     0.5,0.5,0.5,0.5,0.5,1,1.5,1,1,1,    1,1,0.5,1,1.5,1,1,1,                1,1,1,0.5,1.5,1,1,1,                            0.5,0.5,0.5,0.5,0.5,1,1.5,1,1,1,
#     0.5,0.5,0.5,0.5,0.5,1,1.5,1,1,1,    0.5,0.5,0.5,0.5,0.5,1,1.5,1,1,1,    1,2,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,    2
# ]
# # start
# for i in range(len(start)):
#     print(start[i],start_dur[i])
#     if(start[i]<100):
#         winsound.Beep(tone[start[i]+6],int(start_dur[i]*230))
#     else:
#         winsound.Beep(spec[int(start[i]/100)],int(start_dur[i]*230))
# # verse
# for i in range(len(verse)):
#     print(verse[i],verse_dur[i])
#     if(verse[i]<100):
#         winsound.Beep(tone[verse[i]+6],int(verse_dur[i]*230))
#     else:
#         winsound.Beep(spec[int(verse[i]/100)],int(verse_dur[i]*230))
# time.sleep(0.001)
# #chorus
# for j in range(len(chorus)):
#     print(chorus[j],chorus_dur[j])
#     if(chorus[j]<100):
#         winsound.Beep(tone[chorus[j]+6],int(chorus_dur[j]*230))
#     else:
#         winsound.Beep(spec[int(chorus[j]/100)],int(chorus_dur[j]*230))
# time.sleep(0.001)
# # end
# for k in range(len(end)):
#     print(end[k],end_dur[k])
#     if(end[k]<100):
#         winsound.Beep(tone[end[k]+6],int(end_dur[k]*230))
#     else:
#         winsound.Beep(spec[int(end[k]/100)],int(end_dur[k]*230))