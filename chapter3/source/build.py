from pathlib import Path
import json, re, html, sys, collections, os
from content import GUIDE, VERBS, VOCAB, SECTIONS, QUESTIONS, READINGS, LISTENINGS

ROOT=Path(__file__).resolve().parents[1]
(ROOT/'audio').mkdir(exist_ok=True)
(ROOT/'output/pdf').mkdir(parents=True,exist_ok=True)
(ROOT/'qa').mkdir(exist_ok=True)

SOURCES=[
 ('Publisher’s official syllabus (Lesson 3 scope)', 'https://bookclub2.japantimes.co.jp/download/files/genki3/genki-3rd_syllabus_E.pdf'),
 ('Publisher’s sentence-pattern video collection (optional supplement)', 'https://genki.japantimes.co.jp/site/video/en/')
]
data=dict(guide=GUIDE,verbs=VERBS,vocab=VOCAB,sections=SECTIONS,questions=QUESTIONS,readings=READINGS,listening=LISTENINGS,sources=SOURCES)
blob=json.dumps(data,ensure_ascii=False,indent=2)
assert not re.search(r'[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]',blob),'Kanji detected'
(ROOT/'source/content.json').write_text(blob,encoding='utf-8')

# Audio scripts are separate from the questions and used only to render local WAV files.
tracks=[]
for lab in LISTENINGS:
    tracks.append(dict(id=lab['id'],dialogue=lab['id'] in ['L2','L5'],lines=lab['lines']))
tracks.append(dict(id='verb-warmup',dialogue=False,lines=[f'{v}。{stem}ます。{stem}ません。' for v,m,g,stem in VERBS]))
(ROOT/'source/audio-scripts.json').write_text(json.dumps(tracks,ensure_ascii=False,indent=2),encoding='utf-8')

template=(ROOT/'source/template.html').read_text(encoding='utf-8')
(ROOT/'index.html').write_text(template.replace('/*CONTENT_DATA*/',blob),encoding='utf-8')

readme='''# Lesson 3: Making a Date

Open START-HERE.html in Edge, Chrome, or Firefox. It is an offline study workbook; no server, account, or internet connection is required. Keep the audio and output folders beside the HTML file.

Exactly 200 numbered questions cover all eight Lesson 3 grammar topics, four reading labs, five listening labs, and a final checkpoint. All Japanese text uses kana. English explanations and answers are provided.

## Files

- START-HERE.html: guide, vocabulary, all questions, audio players, hidden answers and transcripts, progress tracking.
- output/pdf/Lesson-03-Workbook.pdf: printable guide, vocabulary, and 200 questions with writing space. Listening transcripts are excluded.
- output/pdf/Lesson-03-Answers-and-Transcripts.pdf: explanations for all 200 answers, reading translations, and listening transcripts/translations.
- audio/: normal and slow WAV files for five listening labs, plus a verb-form warmup at both speeds.

## Study plan

1. Session 1: guide and questions 001-040.
2. Session 2: questions 041-080.
3. Session 3: questions 081-120.
4. Session 4: questions 121-165.
5. Session 5: questions 166-200. Keep listening transcripts hidden until you answer.

Try each item before opening its answer. Compare your response and choose Correct or Review. Open responses have model answers, and natural alternatives may be correct. Each numbered question is worth one point; multipart questions require every requested part. Saved status is self-assessed, not automatic grading. Browser storage can be cleared or vary for local files, so use Export progress to keep a backup; Import progress restores that backup.

Aim for 8/10 on the final checkpoint, 24/30 on conjugation, and 20/25 on listening without the guide. Redo all mistakes the next day. These are study targets, not a guarantee of mastery.

## Audio

WAV files were generated locally using installed Japanese speech synthesis. The narration uses Microsoft Haruka Desktop; dialogue turns use Haruka and Ichiro when available. The slow versions are separately synthesized. All audio is synthetic and is original practice content, not publisher audio. Audio playback works offline.

## Scope and sources

This is an independent original supplement aligned to the publisher’s Lesson 3 topic outline. It does not reproduce textbook exercises, passages, or audio. Small amounts of extra vocabulary are glossed. The optional external resources may display kanji; the supplied study material does not.

- Official syllabus: https://bookclub2.japantimes.co.jp/download/files/genki3/genki-3rd_syllabus_E.pdf
- Optional publisher videos: https://genki.japantimes.co.jp/site/video/en/
'''
# The repository's chapter README is maintained separately.

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether, HRFlowable
from reportlab.lib.enums import TA_LEFT
regular_font=os.environ.get('GENKI_FONT_REGULAR','C:/Windows/Fonts/meiryo.ttc')
bold_font=os.environ.get('GENKI_FONT_BOLD','C:/Windows/Fonts/meiryob.ttc')
if not Path(regular_font).exists() or not Path(bold_font).exists():
    raise SystemExit('Set GENKI_FONT_REGULAR and GENKI_FONT_BOLD to Japanese TrueType font files before generating PDFs.')
pdfmetrics.registerFont(TTFont('JP',regular_font,subfontIndex=0))
pdfmetrics.registerFont(TTFont('JPBold',bold_font,subfontIndex=0))
pdfmetrics.registerFontFamily('JP',normal='JP',bold='JPBold',italic='JP',boldItalic='JPBold')
INK=colors.HexColor('#203333');TEAL=colors.HexColor('#166659');MUTED=colors.HexColor('#627571');LINE=colors.HexColor('#d4ded7')
styles={
 'body':ParagraphStyle('body',fontName='JP',fontSize=10.2,leading=17,textColor=INK,spaceAfter=8),
 'small':ParagraphStyle('small',fontName='JP',fontSize=8.8,leading=14,textColor=MUTED,spaceAfter=6),
 'h1':ParagraphStyle('h1',fontName='JPBold',fontSize=24,leading=32,textColor=TEAL,spaceAfter=16),
 'h2':ParagraphStyle('h2',fontName='JPBold',fontSize=15,leading=23,textColor=TEAL,spaceAfter=12),
 'h3':ParagraphStyle('h3',fontName='JPBold',fontSize=11,leading=18,textColor=INK,spaceAfter=9),
 'jp':ParagraphStyle('jp',fontName='JP',fontSize=12,leading=23,textColor=INK,spaceAfter=14),
 'question':ParagraphStyle('question',fontName='JP',fontSize=10.5,leading=18,textColor=INK,spaceAfter=7),
 'table':ParagraphStyle('table',fontName='JP',fontSize=9,leading=14,textColor=INK),
}
def clean(s):
    return str(s).replace('–','-').replace('—','-').replace('‑','-')
def P(s,style='body'):
    return Paragraph(html.escape(clean(s)).replace('\n','<br/>'),styles[style])
def footer(c,d):
    c.saveState(); w,h=d.pagesize
    c.setStrokeColor(LINE);c.line(46,40,w-46,40)
    c.setFont('JP',8);c.setFillColor(MUTED)
    c.drawString(46,26,'LESSON 03  /  MAKING A DATE  /  KANA ONLY')
    c.drawRightString(w-46,26,str(d.page));c.restoreState()
def pdf(path,story):
    SimpleDocTemplate(str(path),pagesize=(612,792),rightMargin=46,leftMargin=46,topMargin=45,bottomMargin=53,title=path.stem,author='Original study supplement',pageCompression=1).build(story,onFirstPage=footer,onLaterPages=footer)
def table(rows,widths):
    out=Table([[P(v,'table') for v in row] for row in rows],colWidths=widths,repeatRows=1,hAlign='LEFT')
    out.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e4eee8')),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),.7,TEAL),('LINEBELOW',(0,1),(-1,-1),.3,LINE),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
    return out

story=[Spacer(1,45),P('LESSON 03','h3'),P('Making a Date','h1'),P('Read. Listen. Build the verb.','h2'),P('200 original questions\n4 reading labs / 5 listening labs\nKana-only Japanese / English explanations','jp'),Spacer(1,15),P('Your workbook','h2'),P('Learn the patterns first, then retrieve them from memory. Use the separate answer book after you try each item. Play the listening tracks from START-HERE.html or the audio folder.'),P('Name: ___________________________________\nStart date: _________________________________\nFinish date: ________________________________','body'),Spacer(1,20),P('Independent supplement aligned to Genki I Lesson 3. All exercises and recordings in this pack are original.','small'),PageBreak()]
for title,paras in GUIDE:
    story.extend([P(title,'h2')]+[P(p) for p in paras]+[PageBreak()])
story.extend([P('Verb reference','h2'),P('Cover the last two columns and produce the forms aloud. The group is part of what you memorize.'),table([['Dictionary','Meaning / group','Affirmative','Negative']]+[[v,f'{m} / {g}',stem+'ます',stem+'ません'] for v,m,g,stem in VERBS],[95,185,120,120]),PageBreak()])
story.extend([P('Vocabulary for the labs','h2'),P('Extra words are supported here so you can concentrate on grammar. Personal names in the passages do not need translation.'),table([['Kana','English','Kana','English']]+[[*VOCAB[i],*(VOCAB[i+1] if i+1<len(VOCAB) else ('',''))] for i in range(0,len(VOCAB),2)],[118,142,118,142]),PageBreak()])
story.extend([P('Your question map','h2'),table([['Questions','Practice']]+[[r,title[5:]] for _,title,r,_ in SECTIONS],[100,420]),Spacer(1,15),P('Scoring and review','h2'),P('Give one point per fully correct numbered question. For open responses, check the intended meaning, conjugation, and particles. Word order may vary naturally. Write the IDs you need to redo.'),P('Review IDs: __________________________________________________\n____________________________________________________________\n____________________________________________________________'),PageBreak()])

for key,title,rng,intro in SECTIONS:
    story.extend([P(title,'h2'),P(f'Questions {rng} / {intro}')])
    if key=='reading':labs=READINGS
    elif key=='listening':labs=LISTENINGS
    else:labs=[None]
    for ix,lab in enumerate(labs):
        if lab:
            if ix:story.append(PageBreak())
            story.extend([P(f"{lab['id']} / {lab['title']}",'h3')])
            if key=='reading':story.append(P(lab['text'],'jp'))
            else:
                story.extend([P(lab['focus']),P(f"Audio: audio/{lab['id']}-normal.wav or audio/{lab['id']}-slow.wav",'small'),P('Listen without the transcript. Use normal speed twice, then slow if needed. The transcript is in the answer book.','small')])
        qs=[item for item in QUESTIONS if item['section']==key and (not lab or item['lab']==lab['id'])]
        for item in qs:
            lines=2 if key in ['mastery','invites','structure'] or len(item['answer'])>70 else 1
            block=[P(f"{item['id']:03d}. {item['prompt']}",'question')]
            for _ in range(lines):block.extend([Spacer(1,13),HRFlowable(width='100%',thickness=.35,color=LINE)])
            block.append(Spacer(1,13))
            story.append(KeepTogether(block))
    story.append(PageBreak())
story.extend([P('Checkpoint and next-day review','h2'),P('My total: ______ / 200\nVerb forms: ______ / 30 (031-060)\nListening: ______ / 25 (166-190)\nFinal checkpoint: ______ / 10 (191-200)'),P('Redo any section below 80%. For every mistake, explain the rule in one sentence and make one new example. Next day, retry the missed questions without looking.'),P('I can ...','h2')])
for s in ['identify u, ru, and irregular verbs, including かえる.','build ます and ません from the correct stem.','distinguish a habit, a plan, and an ongoing action.','choose を, で, に, and destination へ.','use clock times and relative time expressions correctly.','make, accept, and gently decline a ませんか invitation.','use あまり and ぜんぜん with negative verbs.','keep the final verb and phrase particles in the right places.','recognize people, objects, and time expressions as topics with は.']:
    story.append(P('[  ] '+s))
story.extend([Spacer(1,12),P('Scope and optional resources','h2'),P('The official syllabus was checked for topic alignment. All explanations, questions, passages, and synthetic recordings were created for this pack. External resources may contain kanji.','small')])
for title,url in SOURCES:story.append(Paragraph(f'<link href="{url}" color="#166659">{html.escape(title)}</link>',styles['small']))
pdf(ROOT/'output/pdf/Lesson-03-Workbook.pdf',story)

story=[P('Answers and transcripts','h1'),P('Lesson 3 / Making a Date','h2'),P('Use this book only after attempting the corresponding workbook items. Models are not the only possible correct wording. Equivalent natural Japanese is accepted unless the prompt requires a particular particle or word.'),P('Each numbered item is one point. For a multipart item, all requested parts must be correct. Explain the rule after checking, then try the item again the next day.'),PageBreak()]
for key,title,rng,intro in SECTIONS:
    story.extend([P(title,'h2'),P(f'Answer key / {rng}','small')])
    for item in [x for x in QUESTIONS if x['section']==key]:
        story.append(KeepTogether([P(f"{item['id']:03d}. {item['answer']}",'question'),P(item['why'],'small'),Spacer(1,5)]))
    story.append(PageBreak())
for lab in READINGS:
    story.extend([P(f"{lab['id']} / {lab['title']}",'h2'),P('Reading text and translation','small'),P(lab['text'],'jp'),P(lab['translation']),PageBreak()])
for lab in LISTENINGS:
    story.extend([P(f"{lab['id']} / {lab['title']}",'h2'),P('Listening transcript - reveal after answering','small'),P('\n'.join(lab['lines']),'jp'),P('Meaning','h3'),P(lab['translation']),P('Repair routine: identify the missed ending, time, or particle. Replay the matching audio line, repeat it aloud, then listen again with this page closed.','small'),PageBreak()])
story.extend([P('Choose your next practice','h2')])
for rng,title,target in [('001-030','Groups','Memorize each dictionary form with its group; explain why かえる differs from たべる.'),('031-060','Forms','Cover the reference chart; produce both polite forms for every verb.'),('061-075','Nonpast meanings','Add a time expression and explain whether it signals habit or a plan.'),('076-115','Particles and time','Name the role first: object, action location, destination, clock time, or relative day.'),('116-130','Invitations','Say one invitation, one acceptance, and one soft refusal aloud.'),('131-145','Frequency and topics','Check negative endings after あまり and ぜんぜん; identify what は introduces.'),('146-165','Reading','Find the exact phrase supporting every answer; do not guess unstated information.'),('166-190','Listening','Compare transcript and notes, replay, then shadow at normal speed.'),('191-200','Final check','Redo missed topics. Retry the checkpoint tomorrow without the guide.')]:
    story.extend([P(f'{rng} / {title}','h3'),P(target)])
pdf(ROOT/'output/pdf/Lesson-03-Answers-and-Transcripts.pdf',story)

from pypdf import PdfReader
summary={p.name:len(PdfReader(p).pages) for p in (ROOT/'output/pdf').glob('*.pdf')}
print(json.dumps(dict(questions=len(QUESTIONS),sections=dict(collections.Counter(q['section'] for q in QUESTIONS)),pdf_pages=summary),indent=2))
