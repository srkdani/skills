import json,sys,re,os
D=os.path.dirname(os.path.abspath(__file__))
root=D
if len(sys.argv)>1:
    root=sys.argv[1]
    if not os.path.isabs(root):
        root=os.path.join(D,root)
force=int(sys.argv[2]) if len(sys.argv)>2 else None
from playwright.sync_api import sync_playwright
JS=r"""()=>{
const hue=(r,g,b)=>{r/=255;g/=255;b/=255;const mx=Math.max(r,g,b),mn=Math.min(r,g,b),d=mx-mn;if(d<.15)return -1;let h=mx==r?((g-b)/d)%6:mx==g?(b-r)/d+2:(r-g)/d+4;h*=60;return h<0?h+360:h};
const emo=/\p{Extended_Pictographic}/u;
const parseRGB=s=>{const m=String(s).match(/rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)/);if(!m)return null;return {r:+m[1],g:+m[2],b:+m[3],a:m[4]===undefined?1:+m[4]}};
const lin=v=>{v/=255;return v<=0.04045?v/12.92:Math.pow((v+0.055)/1.055,2.4)};
const lum=c=>0.2126*lin(c.r)+0.7152*lin(c.g)+0.0722*lin(c.b);
const ratio=(a,b)=>{const L1=lum(a),L2=lum(b),hi=Math.max(L1,L2),lo=Math.min(L1,L2);return (hi+0.05)/(lo+0.05)};
const bgOf=el=>{let n=el;while(n){const bg=parseRGB(getComputedStyle(n).backgroundColor);if(bg&&bg.a>=0.95)return bg;n=n.parentElement}return {r:255,g:255,b:255,a:1}};
const R={bluePurpleGradients:0,shadows:0,pills:0,emoji:0,glass:0,equalIconGrids:0,eyebrows:0,contrastFailures:0,radii:new Set(),fs:new Set(),fw:new Set(),sp:new Set(),heroPrimaryButtons:0};
const els=[...document.querySelectorAll('body *')];
for(const el of els){const c=getComputedStyle(el);const bx=el.getBoundingClientRect();if(bx.width==0||bx.height==0)continue;
 for(const ps of [c,getComputedStyle(el,'::before'),getComputedStyle(el,'::after')]){
  const bg=ps.backgroundImage;if(bg&&bg.includes('gradient')){const cols=[...bg.matchAll(/rgba?\((\d+),\s*(\d+),\s*(\d+)/g)];if(cols.some(m=>{const h=hue(+m[1],+m[2],+m[3]);return h>=220&&h<=290}))R.bluePurpleGradients++}
  if(ps!==c&&ps.content&&ps.content!='none'&&emo.test(ps.content))R.emoji++;
  if(ps!==c&&ps.content&&ps.content!='none'&&ps.content.length>3&&parseFloat(ps.borderTopLeftRadius)>=100)R.pills++;}
 if(c.boxShadow!='none')R.shadows++;
 if(c.backdropFilter&&c.backdropFilter!='none')R.glass++;
 const rad=parseFloat(c.borderTopLeftRadius);
 const tx=[...el.childNodes].filter(n=>n.nodeType==3).map(n=>n.textContent).join('').trim();
 if(rad>=100&&tx.length>1&&bx.height<48)R.pills++; else if(rad>0&&rad<100&&!(bx.width<50&&Math.abs(bx.width-bx.height)<2)&&!(rad>=bx.height/2-1))R.radii.add(Math.round(rad*10)/10);
 if(tx){R.fs.add(c.fontSize);R.fw.add(c.fontWeight);if(emo.test(tx))R.emoji++;
  const fs=parseFloat(c.fontSize);
  const ls=c.letterSpacing==='normal'?0:parseFloat(c.letterSpacing);
  const upper=c.textTransform==='uppercase'||(tx.length>2&&tx===tx.toUpperCase()&&/[A-Z]/.test(tx));
  if(fs<=14&&tx.length<=42&&upper&&ls>=fs*0.04)R.eyebrows++;
  const fg=parseRGB(c.color);
  if(fg&&fg.a>0.4){const bg=bgOf(el);const cr=ratio(fg,bg);const large=fs>=24||(fs>=18.66&&+c.fontWeight>=700);if(cr<(large?3:4.5))R.contrastFailures++}}
 for(const p of ['paddingTop','paddingRight','paddingBottom','paddingLeft','marginTop','marginBottom','marginLeft','marginRight','rowGap','columnGap']){const v=parseFloat(c[p]);if(v>0)R.sp.add(v)}
 if(c.display=='grid'){const k=[...el.children];if(k.length>=3){const w=k.map(x=>Math.round(x.getBoundingClientRect().width));if(new Set(w).size==1&&k.every(x=>x.firstElementChild&&x.firstElementChild.getBoundingClientRect().width<60))R.equalIconGrids++}}}
const bodyFs=parseFloat(getComputedStyle(document.body).fontSize);
const h1el=document.querySelector('h1')||els.filter(e=>[...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim())).sort((a,b)=>parseFloat(getComputedStyle(b).fontSize)-parseFloat(getComputedStyle(a).fontSize))[0];
const hc=getComputedStyle(h1el);
const h1fs=parseFloat(hc.fontSize);
const h1ls=hc.letterSpacing==='normal'?0:parseFloat(hc.letterSpacing)/h1fs;
const h1lh=parseFloat(hc.lineHeight)/h1fs;
const fold=[...document.querySelectorAll('a,button,[role="button"]')].filter(e=>{const b=e.getBoundingClientRect();if(b.top>=window.innerHeight||b.width<40||b.height<28||b.height>80||b.width>420)return false;const c=getComputedStyle(e);const bg=c.backgroundColor;return bg&&bg!='rgba(0, 0, 0, 0)'});
const fills=fold;
const text=(document.body.innerText||'').toLowerCase();
const banned=['seamless','powerful','stunning','next-level','elevate','unlock'];
const bannedHits=banned.filter(w=>text.includes(w));
const notJust=(text.match(/not just\b/g)||[]).length;
return {...R,radii:R.radii.size,radiiVals:[...R.radii],fontSizes:R.fs.size,fontWeights:R.fw.size,spacingValues:R.sp.size,h1Ratio:+(h1fs/bodyFs).toFixed(2),h1LetterSpacingEm:+h1ls.toFixed(3),h1LineHeight:+h1lh.toFixed(2),h1Font:hc.fontFamily,primaryButtonsAboveFold:fills.length,bannedWords:bannedHits.length+notJust,bannedHits:bannedHits.concat(notJust?['not just']:[]),contrastFailures:R.contrastFailures,eyebrows:R.eyebrows}}"""
out={}
with sync_playwright() as p:
  b=p.chromium.launch()
  for t,vw in [('landing',1280),('pricing',1280),('mobile',390)]:
    use=force or vw
    for v in ['baseline','A','B','B2']:
      src=f'{root}/src/{t}_{v}.html'
      if not os.path.exists(src):
        continue
      pg=b.new_page(viewport={'width':use,'height':900 if use>=1000 else 844},device_scale_factor=1)
      pg.goto(f'file://{src}');pg.wait_for_timeout(250)
      out[f'{t}_{v}']=pg.evaluate(JS)
      pg.screenshot(path=f'{root}/{t}_{v}.png',full_page=True);pg.close()
  b.close()
json.dump(out,open(f'{root}/scores.json','w'),indent=1)
for k,r in out.items():print(k,{x:y for x,y in r.items() if x not in ('radiiVals','bannedHits')})
