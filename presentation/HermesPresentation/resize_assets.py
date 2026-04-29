from pathlib import Path
from PIL import Image, ImageOps
root=Path('/mnt/c/Users/chris/BASECAMP')
out=root/'presentation/HermesPresentation'
assets=out/'assets'; assets.mkdir(exist_ok=True)
imgs={
'hero':'people/george-vaux/artifacts/descriptions34193_wmcr-vaux-1v-v653-ps-095.jpg',
'hero2':'people/george-vaux/artifacts/descriptions34196_wmcr-vaux-1v-v653-ps-098.jpg',
'vaux_mary':'people/mary-vaux/artifacts/descriptions34237_wmcr-vaux-1v-v653-ps-140.jpg',
'contact1':'people/george-vaux/research/1906_shotlist/thumbs/contact_1906_p1.jpg',
'contact2':'people/george-vaux/research/1906_shotlist/thumbs/contact_1906_p2.jpg',
'contact3':'people/george-vaux/research/1906_shotlist/thumbs/contact_1906_p3.jpg',
'contact4':'people/george-vaux/research/1906_shotlist/thumbs/contact_1906_p4.jpg',
'camp_group':'people/edouard-feuz/artifacts/descriptions49447_v200_13_na66_184.jpg',
'feuz':'people/gottfried-feuz/artifacts/descriptions37634_wmcr-barnes-v48-na-268.jpg',
'parker':'people/elizabeth-parker/artifacts/descriptions7261_v14_ac55p_35_38_2.jpg',
'emerald':'people/george-vaux/artifacts/descriptions34205_wmcr-vaux-1v-v653-ps-107.jpg',
'glacier':'people/george-vaux/artifacts/descriptions35955_wmcr-vaux-1o-v653-na-0519.jpg',
}
for name, rel in imgs.items():
    src=root/rel
    dst=assets/f'{name}.jpg'
    im=Image.open(src)
    im=ImageOps.exif_transpose(im).convert('RGB')
    max_dim=1800 if not name.startswith('contact') else 1200
    im.thumbnail((max_dim,max_dim), Image.Resampling.LANCZOS)
    im.save(dst, 'JPEG', quality=84, optimize=True, progressive=True)
    print(name, im.size, dst.stat().st_size)
p=out/'index.html'
s=p.read_text()
repls={
'../../people/george-vaux/artifacts/descriptions34193_wmcr-vaux-1v-v653-ps-095.jpg':'assets/hero.jpg',
'../../people/george-vaux/artifacts/descriptions34196_wmcr-vaux-1v-v653-ps-098.jpg':'assets/hero2.jpg',
'../../people/mary-vaux/artifacts/descriptions34237_wmcr-vaux-1v-v653-ps-140.jpg':'assets/vaux_mary.jpg',
'../../people/george-vaux/research/1906_shotlist/thumbs/contact_1906_p1.jpg':'assets/contact1.jpg',
'../../people/george-vaux/research/1906_shotlist/thumbs/contact_1906_p2.jpg':'assets/contact2.jpg',
'../../people/george-vaux/research/1906_shotlist/thumbs/contact_1906_p3.jpg':'assets/contact3.jpg',
'../../people/george-vaux/research/1906_shotlist/thumbs/contact_1906_p4.jpg':'assets/contact4.jpg',
'../../people/edouard-feuz/artifacts/descriptions49447_v200_13_na66_184.jpg':'assets/camp_group.jpg',
'../../people/gottfried-feuz/artifacts/descriptions37634_wmcr-barnes-v48-na-268.jpg':'assets/feuz.jpg',
'../../people/elizabeth-parker/artifacts/descriptions7261_v14_ac55p_35_38_2.jpg':'assets/parker.jpg',
'../../people/george-vaux/artifacts/descriptions34205_wmcr-vaux-1v-v653-ps-107.jpg':'assets/emerald.jpg',
'../../people/george-vaux/artifacts/descriptions35955_wmcr-vaux-1o-v653-na-0519.jpg':'assets/glacier.jpg',
}
for a,b in repls.items(): s=s.replace(a,b)
p.write_text(s)
print('html bytes', p.stat().st_size)
