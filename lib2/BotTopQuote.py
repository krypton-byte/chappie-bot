from PIL import Image, ImageDraw, ImageFont
class EditR:
    def __init__(self,fn, top='', bot='',color=(0,0,0)):
        self.top = top
        self.bottom = bot
        self.img = Image.open(fn)
        self.font = ImageFont.truetype("lib2/Rodwick.otf",60)
        self.draw = ImageDraw.Draw(self.img)
        self.x = lambda _: self.draw.textsize(_, self.font)
        self.color=color
        self.fn = fn
    def ExecuteCommand(self):
        if self.top:
            self.draw.text((int((self.img.width/2)-(self.x(self.top)[0]/2)),0), self.top, align='center', font=self.font, fill=self.color)
        if self.bottom:
            self.draw.text((int((self.img.width/2)-(self.x(self.bottom)[0]/2)),int((self.img.height/4))*3), self.bottom, align='center', font=self.font, fill=self.color)
        return self.img.save(self.fn)
    def __repr__(self):
        return f"<top:{1 if self.top else 0}, bot:f{1 if self.bottom else 0}, File: {self.fn}>"