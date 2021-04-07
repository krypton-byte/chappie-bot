from moviepy.editor import concatenate_videoclips, VideoFileClip, AudioFileClip, CompositeAudioClip, concatenate_audioclips
class Convert:
    def __init__(self, videoClips):
        self.video       = VideoFileClip(videoClips)
        self.constIphone = VideoFileClip("/".join(__file__.split("/")[:-1])+"/iphone.mp4")
        self.audio       = AudioFileClip("/".join(__file__.split("/")[:-1])+"/iphone.mp3")
    def __repr__(self):
        return f"<source : {self.video.filename}>"
    def Merge(self, OutPut):
        merged   = concatenate_videoclips([self.video, self.constIphone.resize(self.video.size)])
        mixaudio = CompositeAudioClip([
                                        self.audio.subclip(0, audio1:=(self.audio.duration-self.constIphone.duration)+1), 
                                        self.video.audio.subclip(audio2:=self.video.duration-audio1)
                                    ])
        if self.video.duration-audio1 < 0:
            self.audio       = AudioFileClip("/".join(__file__.split("/")[:-1])+"/iphone.mp3").subclip(audio1-self.video.duration)
            mixaudio = CompositeAudioClip([
                                        self.audio.subclip(0, audio1:=(self.audio.duration-self.constIphone.duration)+1), 
                                        self.video.audio.subclip(audio2:=self.video.duration-audio1)
                                    ])
        merged.audio=concatenate_audioclips([
                        self.video.audio.subclip(0, audio2), 
                        mixaudio, 
                        self.audio.subclip(audio1)
                    ])
        merged.write_videofile(OutPut, threads=10)
