from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import math

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'assets'
OUT.mkdir(exist_ok=True)
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
def font(s, bold=False, mono=False): return ImageFont.truetype(MONO if mono else BOLD if bold else FONT,s)
def text(d, xy, t, s=16, fill='#eaf2ff', bold=False, mono=False):d.text(xy,t,font=font(s,bold,mono),fill=fill)
def bg(w,h,t):
 y,x=np.mgrid[0:h,0:w];x=x/w;y=y/h
 a=np.exp(-((x-(.68+.17*math.cos(t)))**2/.12+(y-(.3+.2*math.sin(t)))**2/.7))
 b=np.exp(-((x-(.25+.12*math.sin(t)))**2/.16+(y-.85)**2/.5))
 c=np.exp(-((x-.95)**2/.05+(y-.95)**2/.5))
 arr=np.stack([9+30*a+6*b+12*c,16+11*a+43*b+15*c,28+49*a+35*b+29*c],axis=-1)
 return Image.fromarray(np.uint8(np.clip(arr,0,255)),'RGB')
def pill(d,x,y,label,color='#b6f7dc'):
 w=int(d.textlength(label,font=font(12,mono=True)))+26
 d.rounded_rectangle((x,y,x+w,y+29),radius=14,fill='#162e35',outline='#34544f')
 text(d,(x+13,y+6),label,12,color,mono=True)
 return w

def hero(t):
 im=bg(1000,350,t);d=ImageDraw.Draw(im)
 for x in range(560,1000,32):
  for y in range(30,340,32):d.ellipse((x,y,x+1,y+1),fill='#38505b')
 # Orbital architecture motif, drawn behind copy.
 for r in [75,105,138]:
  d.ellipse((822-r,171-r,822+r,171+r),outline='#375065',width=1)
 for i,r in enumerate([75,105,138]):
  a=t+i*2.1;xx=822+math.cos(a)*r;yy=171+math.sin(a)*r
  d.ellipse((xx-4,yy-4,xx+4,yy+4),fill=['#a3ffd5','#a9c8ff','#d4b4ff'][i])
 d.rounded_rectangle((781,130,863,212),radius=24,fill='#142735',outline='#5a817f',width=1)
 text(d,(796,154),'</>',26,'#a3ffd5',mono=True)
 text(d,(42,32),'HOANGVH238  /  ENGINEERING & PRODUCT',12,'#9bb7c6',mono=True)
 text(d,(40,85),'Hoang Huy Vo',53,bold=True)
 text(d,(43,161),'From idea to production.',29,'#b6f7dc')
 text(d,(43,211),'Full-stack engineering. AI-powered products.',18,'#b7c7d9')
 text(d,(43,240),'Built for real users and the next stage of growth.',16,'#8fa6bb')
 x=43
 for l in ['.NET','NEXT.JS','AI / RAG']:
  x+=pill(d,x,293,l)+10
 text(d,(795,306),'DA NANG / VN',12,'#a7becb',mono=True)
 d.rounded_rectangle((1,1,998,348),radius=22,outline='#48616b',width=1)
 return im

def rank(t):
 im=bg(1000,227,t);d=ImageDraw.Draw(im)
 text(d,(34,22),'FREELANCE TRACK RECORD',12,'#a7becb',mono=True)
 pill(d,846,15,'TOP RATED')
 columns=[(34,'#703','AI Development rank'),(285,'Top 8%','AI Development'),(536,'100%','Job Success'),(787,'31','Completed jobs')]
 for i,(x,v,label) in enumerate(columns):
  if i:d.line((x-25,75,x-25,149),fill='#405360')
  mix=(math.sin(t-i*.7)+1)/2
  color=tuple(int(a*(1-mix)+b*mix) for a,b in zip((221,233,255),(163,255,213)))
  text(d,(x,76),v,40,color,bold=True)
  text(d,(x,134),label,13,'#b7c7d9')
 text(d,(34,187),'UPWORKRANK SNAPSHOT / 14 NOV 2026',11,'#90a7b8',mono=True)
 text(d,(614,187),'THIRD-PARTY RANKING · NOT A SKILL SCORE',11,'#90a7b8',mono=True)
 d.rounded_rectangle((1,1,998,225),radius=22,outline='#48616b',width=1)
 return im

for name, fn in [('hero',hero),('rank',rank)]:
 frames=[fn(2*math.pi*i/48) for i in range(48)]
 frames[0].save(OUT/f'{name}.png')
 # A shared palette avoids frame-to-frame palette flicker.
 sample=Image.new('RGB',(1000,frames[0].height*4))
 for i,k in enumerate([0,12,24,36]):sample.paste(frames[k],(0,i*frames[0].height))
 palette=sample.quantize(colors=128)
 q=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
 q[0].save(OUT/f'{name}.gif',save_all=True,append_images=q[1:],duration=125,loop=0,optimize=True,disposal=1)
 print(name,len(q),'frames', (OUT/f'{name}.gif').stat().st_size,'bytes')
