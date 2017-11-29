from PIL import Image

sz=(1080,720)
wt=(255,255,255)
blk=(0,0,0)
def create_img():
    im = Image.new("RGB", size=sz, color=wt)
    im.show()
    return im



if __name__=='__main__':
    im=create_img()
    (x0,y0,x1,y1)=map(int, input("please input start point and end point:").split(' '))
    print(x0,y0,x1,y1)
    a=y0-y1
    b=x1-x0
    c=x0*y1-x1*y0
    d=2*a+b
    delta1=2*a
    delta2=2*(a+b)
    x=x0
    y=y0
    while(x<x1):
        if d<0:
            x+=1
            y+=1
            d+=delta2
        else:
            x+=1
            d+=delta1
        im.putpixel((x,y),value=blk)
    im.show()