import os
import ffmpeg

def video_to_video_note(floc, nfloc):
    probe = ffmpeg.probe(floc)
    for stream in probe["streams"]:
        if stream["codec_type"]=="video":
            w = probe["streams"][0]['width']
            h = probe["streams"][0]['height']
    s = min(w,h)
    if w>h:
        x=(w-h)//2
        y=0
    if w==h:
        x=0
        y=0
    if w<h:
        x=0
        y=(h-w)//2
    os.system(f"ffmpeg -y -i {floc} -vf crop={s}:{s}:{x}:{y},scale=384:384,setsar=1:1 {nfloc}")
    return True
