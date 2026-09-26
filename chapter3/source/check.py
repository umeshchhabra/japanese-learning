from pathlib import Path
import json,re,subprocess,wave,collections,shutil,os
from PIL import Image,ImageDraw
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'source/content.json').read_text(encoding='utf-8'))
assert len(DATA['questions'])==200
assert [q['id'] for q in DATA['questions']]==list(range(1,201))
assert all(q['answer'] and q['why'] for q in DATA['questions'])
for name in ['index.html','README.md','source/content.json','source/audio-scripts.json']:
    assert not re.search(r'[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]',(ROOT/name).read_text(encoding='utf-8')),name
poppler=os.environ.get('PDFTOPPM') or shutil.which('pdftoppm')
if not poppler: raise SystemExit('Install Poppler and add pdftoppm to PATH, or set PDFTOPPM.')
(ROOT/'qa').mkdir(exist_ok=True)
report={'question_count':200,'kanji_scan':'passed','pdfs':{}}
for pdf in (ROOT/'output/pdf').glob('*.pdf'):
    prefix='workbook' if 'Workbook' in pdf.name else 'answers'
    reader=PdfReader(pdf)
    extracted='\n'.join(p.extract_text() for p in reader.pages)
    assert not re.search(r'[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]',extracted)
    missing=[n for n in range(1,201) if not re.search(rf'\b{n:03d}\.',extracted)]
    assert not missing,(pdf.name,missing)
    if prefix=='workbook':
        assert 'わたしはミカです。' not in extracted,'Listening transcript exposed in workbook'
    report['pdfs'][pdf.name]={'pages':len(reader.pages),'all_200_ids_present':True}
    subprocess.run([poppler,'-scale-to','950','-png',str(pdf),str(ROOT/'qa'/prefix)],check=True,capture_output=True)
    files=sorted((ROOT/'qa').glob(prefix+'-*.png'))
    for batch in range(0,len(files),9):
        sheet=Image.new('RGB',(1200,1650),'#dfe5dd');draw=ImageDraw.Draw(sheet)
        for i,path in enumerate(files[batch:batch+9]):
            im=Image.open(path).convert('RGB');im.thumbnail((380,510));x=10+(i%3)*400;y=25+(i//3)*550
            sheet.paste(im,(x,y));draw.text((x,y-18),path.stem,fill='black')
        sheet.save(ROOT/'qa'/f'{prefix}-contact-{batch//9+1}.jpg',quality=88)
    (ROOT/'qa'/f'{prefix}-text.txt').write_text(extracted,encoding='utf-8')
(ROOT/'qa/validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
