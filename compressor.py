
#import os
import ffmpeg

import ffmpeg


#ffmpeg.input(input_file).output(output_file, b=bitrate, vf='scale=-1:720').run()

#os.system("ffmpeg -i input.mp4 -b:v 100k -y output.mp4 ")
import moviepy.editor as mp
clip = mp.VideoFileClip("input.mp4")
w, h = clip.size
if w<h:
    d = h-w
    print()
    print("w<h",d/2,h-d/2)
    new_clip = clip.crop(y1=d/2,y2=h-d/2)
    new_clip.write_videofile("sqOutput.mp4")
elif w>h:
    print("w>h")
    d = w-h
    new_clip = clip.crop(x1=d / 2, x2=w - d / 2)
    new_clip.write_videofile("sqOutput.mp4")



