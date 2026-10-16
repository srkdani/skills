import json,sys,re,os
D=os.path.dirname(os.path.abspath(__file__))
from playwright.sync_api import sync_playwright
JS=r"""()=>{
const hue=(r,g,b)=>{r/=255;g/=255;b/=255;const mx=Math.max(r,g,b),mn=Math.min(r,g,b),d=mx-mn;if(d<.15)return -1;let h=mx==r?((g-b)/d)%6:mx==g?(b-r)/d+2:(r-g)/d+4;h*=60;return h<0?h+360:h};
const emo=/\p{Extended_Pictographic}/u;
const R={bluePurpleGradients:0,shadows:0,pills:0,emoji:0,glass:0,equalIconGrids:0,radii:new Set(),fs:new Set(),fw:new Set(),sp:new Set(),heroPrimaryButtons:0};
const els=[...document.querySelectorAll('body *')];
for(const el of els){const c=getComputedStyle(el);const bx=el.getBoundingClientRect();if(bx.width==0)continue;
 for(const ps of [c,getComputedStyle(el,'::before'),getComputedStyle(el,'::after')]){
  const bg=ps.backgroundImage;if(bg&&bg.includes('gradient')){const cols=[...bg.matchAll(/rgba?\((\d+), (\d+), (\d+)/g)];if(cols.some(m=>{const h=hue(+m[1],+m[2],+m[3]);return h>=220&&h<=290}))R.bluePurpleGradients++}
  if(ps!==c&&ps.content&&ps.content!='none'&&emo.test(ps.content))R.emoji++;
  if(ps!==c&&ps.content&&ps.content!='none'&&ps.content.length>3&&parseFloat(ps.borderTopLeftRadius)>=100)R.pills++;}
 if(c.boxShadow!='none')R.shadows++;
 if(c.backdropFilter&&c.backdropFilter!='none')R.glass++;
 const rad=parseFloat(c.borderTopLeftRadius);
 const tx=[...el.childNodes].filter(n=>n.nodeType==3).map(n=>n.textContent).join('').trim();
 if(rad>=100&&tx.length>1&&bx.height<40)R.pills++; else if(rad>0&&rad<100&&!(bx.width<50&&Math.abs(bx.width-bx.height)<2)&&!(rad>=bx.height/2-1))R.radii.add(rad);
 if(tx){R.fs.add(c.fontSize);R.fw.add(c.fontWeight);if(emo.test(tx))R.emoji++}
 for(const p of ['paddingTop','paddingRight','paddingBottom','paddingLeft','marginTop','marginBottom','marginLeft','marginRight','rowGap','columnGap']){const v=parseFloat(c[p]);if(v>0)R.sp.add(v)}
 if(c.display=='grid'){const k=[...el.children];if(k.length>=3){const w=k.map(x=>Math.round(x.getBoundingClientRect().width));if(new Set(w).size==1&&k.every(x=>x.firstElementChild&&x.firstElementChild.getBoundingClientRect().width<60))R.equalIconGrids++}}}
const h1=els.filter(e=>[...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim())).sort((a,b)=>parseFloat(getComputedStyle(b).fontSize)-parseFloat(getComputedStyle(a).fontSize))[0];const body=parseFloat(getComputedStyle(document.body).fontSize);
const fold=els.filter(e=>{const b=e.getBoundingClientRect();return b.top<window.innerHeight&&/btn/.test(e.className)&&!/(^| )s( |$)|link/.test(e.className)});
const fills=fold.filter(e=>{const c=getComputedStyle(e).backgroundColor;return c!='rgba(0, 0, 0, 0)'||getComputedStyle(e).backgroundImage!='none'});
return {...R,radii:R.radii.size,radiiVals:[...R.radii],fontSizes:R.fs.size,fontWeights:R.fw.size,spacingValues:R.sp.size,h1Ratio:+(parseFloat(getComputedStyle(h1).fontSize)/body).toFixed(2),primaryButtonsAboveFold:fills.length}}"""
out={}
with sync_playwright() as p:
  b=p.chromium.launch()
  for t,vw in [('landing',1280),('pricing',1280),('mobile',390)]:
    for v in ['baseline','A','B']:
      pg=b.new_page(viewport={'width':vw,'height':844 if vw==390 else 800},device_scale_factor=1)
      pg.goto(f'file://{D}/src/{t}_{v}.html');pg.wait_for_timeout(200)
      out[f'{t}_{v}']=pg.evaluate(JS)
      pg.screenshot(path=f'{D}/{t}_{v}.png',full_page=True);pg.close()
  b.close()
json.dump(out,open(f'{D}/scores.json','w'),indent=1)
for k,r in out.items():print(k,{x:y for x,y in r.items() if x!='radiiVals'})
