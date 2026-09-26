# Chapter 3 - Making a Date

**[Study online](https://umeshchhabra.github.io/japanese-learning/chapter3/)**

200 questions cover verb groups, polite nonpast forms, particles, time references, invitations, frequency, word order, and the topic particle は. Includes four reading labs, five listening labs, and a final checkpoint. Japanese text is kana only.

## Study materials

- `index.html`: interactive workbook with hidden answers/transcripts and self-checked progress.
- `START-HERE.html`: compatibility link to the workbook.
- `audio/`: normal and slow recordings for the five labs plus a verb-form warmup (12 WAV files).
- `output/pdf/Lesson-03-Workbook.pdf`: printable grammar guide and 200 questions.
- `output/pdf/Lesson-03-Answers-and-Transcripts.pdf`: answer explanations, translations, and listening transcripts.
- `downloads/Lesson-03-Making-a-Date.zip`: original offline pack. Extract it and open START-HERE.html on a desktop browser; keep its audio and output folders beside it.

## Suggested sessions

1. Guide + questions 001-040.
2. Questions 041-080.
3. Questions 081-120.
4. Questions 121-165.
5. Questions 166-200. Keep listening transcripts closed until you answer.

Give one point per fully correct numbered question. Compare open responses with the model; equivalent natural Japanese may be correct. Use Correct / Review again to record your own assessment. Targets: 24/30 on verb forms, 20/25 on listening, and 8/10 on the final checkpoint without help. Redo missed items the next day.

Progress stays in each browser. Export a JSON backup before switching browsers/devices, then import it at the destination. There is no automatic cross-device sync.

## Edit and regenerate

Edit `source/content.py` for content and `source/template.html` for layout. Python 3 and the packages in `source/requirements.txt` are needed to regenerate the page, JSON, and PDFs:

```sh
python -m pip install -r chapter3/source/requirements.txt
python chapter3/source/build.py
```

PDF generation uses the Meiryo fonts on Windows by default. On another system, set `GENKI_FONT_REGULAR` and `GENKI_FONT_BOLD` to suitable Japanese TrueType font files. Existing PDFs are ready to use without installing anything.

To regenerate WAV files on Windows, run `source/make-audio.ps1` with Windows PowerShell and installed Japanese voices. Narration uses Microsoft Haruka Desktop; dialogue alternates Haruka and Ichiro when available. Nothing runs automatically when you open the workbook.

PDF checks: install Poppler and run `python chapter3/source/check.py`. Use `PDFTOPPM` if the executable is not on PATH. Browser checks: install dependencies in `chapter3/source`, run `npx playwright install chromium`, then `npm run check:browser`. `BROWSER_PATH` can select an existing browser; `STUDY_URL` can target a local or deployed site. Browser tests use a temporary profile and do not change your personal progress.

## Sources and attribution

These are original exercises and synthetic recordings, not publisher worksheets or audio. The topic scope was checked against the [official syllabus](https://bookclub2.japantimes.co.jp/download/files/genki3/genki-3rd_syllabus_E.pdf). Optional [publisher videos](https://genki.japantimes.co.jp/site/video/en/) are external and may show kanji.
