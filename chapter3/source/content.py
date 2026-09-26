"""Original kana-only practice content. Run build.py to package the materials."""
SECTIONS = [
 ('groups','01 / Know your verbs','001-030','Identify the group before you conjugate. U, ru, and irregular are conjugation groups, not meanings.'),
 ('forms','02 / Build the forms','031-060','Write the requested polite nonpast form. Say the stem aloud before adding the ending.'),
 ('tense','03 / What does it mean?','061-075','Separate habit, future plans, ongoing actions, and negative statements.'),
 ('particles','04 / Choose the particle','076-100','Use を, で, に, or へ where requested. Keep each particle attached to its phrase.'),
 ('time','05 / Put it on the calendar','101-115','Use に for a specified clock time. Learn which time expressions normally stand alone.'),
 ('invites','06 / Make a date','116-130','Build invitations with the polite negative form plus か. Practise accepting and declining.'),
 ('structure','07 / Frequency, order, and は','131-145','Combine frequency, sentence structure, and the topic particle.'),
 ('reading','08 / Reading labs','146-165','Read once for the main idea, then again for details. Answer in English unless Japanese is requested.'),
 ('listening','09 / Listening labs','166-190','Keep transcripts closed. Play normal speed once for the main idea, again for details, then slow speed if needed.'),
 ('mastery','10 / Final checkpoint','191-200','Work without the guide or answer key. For each Japanese answer, explain your verb ending and particles aloud.')
]

# Dictionary form, English meaning, group, polite stem. The last two are supported extra vocabulary.
VERBS = [
 ('たべる','eat','ru','たべ'),('みる','see; watch','ru','み'),('おきる','get up','ru','おき'),
 ('ねる','sleep; go to bed','ru','ね'),('いく','go','u','いき'),('かえる','return home','u','かえり'),
 ('きく','listen; hear; ask','u','きき'),('のむ','drink','u','のみ'),('はなす','speak','u','はなし'),
 ('よむ','read','u','よみ'),('する','do','irregular','し'),('くる','come','irregular','き'),
 ('べんきょうする','study','irregular','べんきょうし'),('かう','buy [extra]','u','かい'),('まつ','wait [extra]','u','まち')
]

GUIDE = [
 ('Your route through Lesson 3',[
  'All Japanese in this pack uses hiragana or katakana. Spaces separate useful chunks for beginners. English explanations keep the focus on grammar. These are original practice materials, not copied textbook exercises.',
  'Use five sessions of about 45-60 minutes: (1) guide + 001-040; (2) 041-080; (3) 081-120; (4) 121-165; (5) 166-200. Split a session if needed. Begin each session by redoing five earlier mistakes.',
  'Try every question before revealing its answer. Each numbered item is one question, even when it asks for a form plus a reason. Use 1 point only when the whole answer is right; for open responses, compare meaning, ending, and particles with the model.',
  'The final 10 items are a checkpoint, not a promise of mastery. Aim for at least 8/10 without help, at least 24/30 on verb forms, and 20/25 on listening. Then redo missed items the next day without looking.'
 ]),
 ('1. Three conjugation groups',[
  'Start from the dictionary form: たべる, のむ, する. Group names describe how endings change. They are separate from meaning types such as action and state.',
  'Ru-verbs: remove the final る, then add ます or ません. たべる → たべ → たべます / たべません. みる → みます / みません. おきる → おきます. ねる → ねます.',
  'U-verbs: change the FINAL u-row kana to its i-row partner, then add ます or ません. のむ → のみ → のみます / のみません. はなす → はなし → はなします. Do not change earlier kana.',
  'Final-kana map: う → い; く → き; ぐ → ぎ; す → し; つ → ち; ぬ → に; ぶ → び; む → み; る → り. This is a polite-form rule; it is not a rule for every conjugation.',
  'Irregular: する → します / しません; くる → きます / きません. A word ending in する follows する: べんきょうする → べんきょうします / べんきょうしません.',
  'Do not decide from the last る alone. かえる (return home) is a u-verb: かえります, not かえます. Many verbs ending in an i/e sound + る are ru-verbs, but there are exceptions. Memorize the group with the dictionary form.',
  'The polite stem is the part immediately before ます: たべ, のみ, し, き. A stem is a building block, not usually a complete polite sentence by itself. Do not add です to a ます-form verb.'
 ]),
 ('2. Verb meanings and the so-called present tense',[
  'Conjugation group answers “How does the word change?” Meaning type answers “What kind of situation does it describe?” Most verbs practised here describe actions. Some describe a change or endpoint, such as おきる or かえる. Other Japanese verbs express states. These meaning categories do not decide whether a verb is u, ru, or irregular.',
  'ます is polite nonpast affirmative. With an action verb, it commonly describes a habit or a future action: まいにち ほんを よみます。 = I read books every day. あした ほんを よみます。 = I will read a book tomorrow.',
  'ません is polite nonpast negative: コーヒーを のみません。 = I do not drink coffee / I will not drink coffee. Context and time words choose the reading. Japanese does not add an equivalent of “will” here.',
  'An ordinary action verb in ます does not by itself mean “am doing right now.” テレビを みます normally means “watch TV” or “will watch TV.” The usual ongoing-action construction is taught later. Do not translate every ます form as an English -ing form.',
  'A state can hold at the present moment without being an action in progress. For example, わかります means “understand” (preview vocabulary, not tested here). Thus “nonpast” does not mean “never refers to now.” The important distinction is the meaning of the verb in context.',
  'A sentence without a time word may need context. がっこうに いきます can describe a regular activity or a coming trip. Politeness, positive/negative meaning, and time reference are different choices.',
  'Verb endings do not change for I, you, or they. わたしは たべます and アキさんは たべます use the same ending. The speaker or subject is often omitted when clear.'
 ]),
 ('3. Particles: を, で, に, and へ',[
  'を marks the direct object: the thing affected by an action. みずを のみます。 = I drink water. えいがを みます。 = I watch a movie. Write を; pronounce it “o.”',
  'で marks where an action happens: としょかんで ほんを よみます。 = I read books at the library. The library is the action setting; the book is the object.',
  'に marks a destination with いく, くる, and かえる: がっこうに いきます。 = I go to school. うちに かえります。 = I return home. に also marks specified times: しちじに おきます。',
  'へ can mark the direction/destination of movement: がっこうへ いきます。 Pronounce the particle へ as “e.” For the simple destination sentences in this pack, に and へ are both possible. へ cannot replace time に.',
  'Compare: としょかんに いきます。 = I go to the library. としょかんで べんきょうします。 = I study at the library. Choose the particle from the role of the place, not just from the English word “at.”',
  'Not every verb takes を. ねます and おきます do not need a direct object. With べんきょうする, にほんごを べんきょうします is natural. These lessons focus on action-location で; other uses come later.'
 ]),
 ('4. Time references',[
  'Use に with a specified clock time: ろくじに, しちじはんに, ごごさんじに. なんじに おきますか。 asks what time someone gets up.',
  'Normally use no に after relative times such as きょう (today), あした (tomorrow), あさって (the day after tomorrow), and こんや (tonight), or repeating expressions such as まいにち (every day) and まいあさ (every morning).',
  'いつ means “when” and normally appears without に: いつ いきますか。 Contrast なんじに (at what time).',
  'Days of the week allow に: どようびに いきます。 In many contexts it can be omitted. Broad times such as あさ (morning), ばん (evening), and しゅうまつ (weekend) can also appear without に; some permit に depending on context. The questions specify when a particular answer is required.',
  'Time can become the topic: あしたは べんきょうします。 = As for tomorrow, I will study. That は frames the sentence; it is not the same job as time に.',
  'Clock reminders: よじ = 4:00; しちじ = 7:00; くじ = 9:00; はん = half past. ごぜん = a.m.; ごご = p.m. じゅうにじ = 12:00.'
 ]),
 ('5. Invitations with ませんか',[
  'Take the polite negative form and add か: のむ → のみません → のみませんか。 In an invitation context: “Would you like to drink ...?” or “Shall we drink ...?” It is not simply a refusal.',
  'いっしょに ひるごはんを たべませんか。 = Would you like to have lunch together? どようびに えいがを みませんか。 = Would you like to see a movie on Saturday?',
  'A clear acceptance: いいですね。 = That sounds good. A gentle decline: すみません。どようびは ちょっと……。 = Sorry, Saturday is a little difficult. The unfinished ちょっと is a conventional soft refusal in this context.',
  'Ask for details with なんじに (what time), どこで (where an activity happens), or どこに (where someone goes). Use your existing forms: なんじに いきますか。',
  'Do not mix endings: たべませんか is correct; たべますませんか is not. The invitation pattern uses the same stem as ます. Avoid answering an invitation with a bare yes/no if that would be unclear; いいですね is a helpful beginner response.'
 ]),
 ('6. Frequency adverbs',[
  'まいにち = every day; いつも = always; たいてい = usually; よく = often; ときどき = sometimes. These can accompany an affirmative verb: よく おんがくを ききます。',
  'For the Lesson 3 pattern, pair あまり with a negative verb: あまり テレビを みません。 = I do not watch TV very much / very often. Pair ぜんぜん with a negative verb: ぜんぜん コーヒーを のみません。 = I do not drink coffee at all.',
  'Compare あまり のみません (not much / not often) and ぜんぜん のみません (not at all). The negative ending is part of the meaning. Frequency words are not exact percentages.',
  'A useful beginner position is after the topic or time phrase and before the object/place: わたしは よく うちで ほんを よみます。 Other natural positions are possible.'
 ]),
 ('7. Word order',[
  'A dependable starting pattern is: TOPIC は + TIME + PLACE で + OBJECT を + VERB. わたしは あした としょかんで にほんごを べんきょうします。',
  'For a movement verb, use DESTINATION に or へ: わたしは あした がっこうに いきます。 You do not need to fill every slot in every sentence.',
  'The verb normally closes these sentences; か follows it in a question. Keep particles with their phrases. あした わたしは にほんごを としょかんで べんきょうします is also possible, though the first pattern is easier to build.',
  'Do not treat the model word order as the only valid answer. In rearrangement questions, use every supplied chunk once and keep the final verb at the end. In translations, equivalent natural orders are accepted.'
 ]),
 ('8. The topic particle は',[
  'Write は and pronounce it “wa” when it is the topic particle. It introduces what the sentence is about, often with a contrast: わたしは まいにち べんきょうします。',
  'The topic need not be the person doing the action: しゅうまつは よく えいがを みます。 = On weekends, I often watch movies. Here the weekend is the topic.',
  'An object can become a topic. コーヒーを のみません is a neutral statement about not drinking coffee. コーヒーは のみません frames coffee as the topic, often contrasting it with something else. In this simple object-topic pattern, は replaces を; do not write をは.',
  'A location can be contrasted while preserving で: うちでは べんきょうしません。 = At home, I do not study. Here では is the location particle で plus the topic particle は, not a negative form of です.',
  'Do not replace every particle with は. は marks the topic; を, で, and に show other roles. The wider は/が distinction is outside this practice pack.'
 ]),
 ('How to use the labs',[
  'Reading: scan the title, read the kana passage without translating every word, answer the five questions, and check the evidence in the passage. Finally read it aloud once.',
  'Listening: read only the questions first. Listen at normal speed for the situation. Listen again and take notes. Try slow speed only if needed. Reveal the transcript after answering; underline the ending or particle you missed, then repeat each line aloud.',
  'The ten WAV files use an installed Japanese synthetic voice (Microsoft Haruka Desktop). They are study aids, not recordings from the textbook or a human speaker. Normal and slow versions contain the same content. No internet or installed Japanese voice is needed to play the saved audio.',
  'Give listening comprehension answers in English unless an item asks for kana. For dictation, ignore spaces and punctuation when comparing. After correction, listen again with the transcript closed.'
 ])
]

VOCAB = [
 ('わたし','I'),('ともだち','friend'),('いっしょに','together'),('がっこう','school'),('だいがく','university'),
 ('うち','home'),('としょかん','library'),('きっさてん','cafe'),('レストラン','restaurant'),('えき','station [extra]'),
 ('ほん','book'),('ざっし','magazine'),('しんぶん','newspaper'),('えいが','movie'),('テレビ','TV'),('おんがく','music'),
 ('にほんご','Japanese language'),('えいご','English language'),('みず','water'),('おちゃ','tea'),('コーヒー','coffee'),
 ('パン','bread'),('あさごはん','breakfast'),('ひるごはん','lunch'),('ばんごはん','dinner'),('テニス','tennis'),
 ('きょう','today'),('あした','tomorrow'),('あさって','day after tomorrow [extra]'),('こんや','tonight'),('あさ','morning'),('ばん','evening'),
 ('しゅうまつ','weekend'),('まいにち','every day'),('まいあさ','every morning'),('まいばん','every evening'),
 ('げつようび','Monday'),('かようび','Tuesday'),('すいようび','Wednesday'),('もくようび','Thursday'),('きんようび','Friday'),('どようび','Saturday'),('にちようび','Sunday'),
 ('ごぜん','a.m.'),('ごご','p.m.'),('はん','half past'),('なんじ','what time'),('いつ','when'),('どこ','where'),('なに／なん','what'),
 ('いつも','always'),('たいてい','usually'),('よく','often'),('ときどき','sometimes'),('あまり + negative','not very much / not often'),('ぜんぜん + negative','not at all'),
 ('いいですね','that sounds good'),('すみません','excuse me / sorry'),('ちょっと……','a little ...; soft refusal in context'),('でも','but [connector]'),('じゃあ','well then')
]

QUESTIONS=[]
def q(section,prompt,answer,why,lab=None):
    QUESTIONS.append(dict(id=len(QUESTIONS)+1,section=section,prompt=prompt,answer=answer,why=why,lab=lab))

for word,meaning,group,stem in VERBS:
    rule={'ru':'Remove final る.','u':'Change the final u-row kana to its i-row partner.','irregular':'Memorize this irregular stem.'}[group]
    q('groups',f'Classify {word} ({meaning}): u, ru, or irregular?',group,f'{rule} The polite stem is {stem}.')
for p,a,w in [
 ('True or false: every dictionary form ending in る is a ru-verb.','False.','かえる (return home) ends in る but is a u-verb.'),
 ('Which needs final る → り: たべる or かえる?','かえる','かえる is u; かえり + ます. たべる is ru; remove る.'),
 ('Which pair shares a conjugation group: みる + おきる, or みる + かえる?','みる + おきる','Both are ru-verbs. かえる is u.'),
 ('In the polite-form rule, what does final む change to?','み','のむ → のみ + ます.'),
 ('In the polite-form rule, what does final す change to?','し','はなす → はなし + ます.'),
 ('In the polite-form rule, what does final く change to?','き','いく → いき + ます.'),
 ('Extra pattern: final う in かう changes to which kana before ます?','い','かう → かい + ます.'),
 ('Extra pattern: final つ in まつ changes to which kana before ます?','ち','まつ → まち + ます.'),
 ('Write only the polite stem of たべる.','たべ','Remove final る from this ru-verb.'),
 ('Write only the polite stem of のむ.','のみ','For u-verbs, change only the final kana: む → み.'),
 ('Write only the polite stem of する.','し','する has an irregular stem before ます / ません.'),
 ('Write only the polite stem of くる.','き','The polite stem is き, not く.'),
 ('Does “action verb” tell you whether a verb is u or ru? Explain briefly.','No. Meaning type and conjugation group are different classifications.','たべる is an action ru-verb; のむ is an action u-verb.'),
 ('Which label tells you how to form ます: “u-verb” or “habitual action”?','u-verb','Habitual action describes a use in context, not a conjugation rule.'),
 ('You meet an unfamiliar verb ending in an e sound + る. Is that enough to know its group for certain?','No; check and learn its group.','The ending is a useful clue, but exceptions such as かえる exist.')
]:q('groups',p,a,w)

for word,meaning,group,stem in VERBS:
    q('forms',f'Write the polite nonpast affirmative of {word} ({meaning}).',stem+'ます',f'{word} → {stem} + ます ({group}).')
    q('forms',f'Write the polite nonpast negative of {word} ({meaning}).',stem+'ません',f'{word} → {stem} + ません ({group}).')

for p,a,w in [
 ('Translate: まいにち ほんを よみます。','I read books every day.','まいにち makes the nonpast form a habitual action.'),
 ('Translate: あした ほんを よみます。','I will read a book tomorrow.','あした makes the same verb form future in context.'),
 ('Translate: きょうは コーヒーを のみません。','Today, I will not drink coffee. / I am not drinking coffee today.','ません is negative; the English -ing option describes a plan for today, not an action in progress.'),
 ('Does テレビを みます by itself normally mean “I am watching TV right now”?','No. It normally means “I watch TV” or “I will watch TV.”','An ongoing action uses a later construction.'),
 ('Choose the best reading of まいあさ しちじに おきます: habit or future one-time plan?','Habit.','まいあさ means every morning.'),
 ('Choose the best reading of あした がっこうに いきます: daily habit or future plan?','Future plan.','あした means tomorrow.'),
 ('Make negative: えいがを みます。','えいがを みません。','Replace ます with ません after the stem み.'),
 ('Make affirmative: おんがくを ききません。','おんがくを ききます。','Keep the stem きき; use ます.'),
 ('Correct the ending: わたしは べんきょうしますです。','わたしは べんきょうします。','A ます-form verb is already a complete polite predicate.'),
 ('Does Japanese change たべます when the subject changes from I to アキさん?','No.','These verb forms do not change for grammatical person or number.'),
 ('Can がっこうに いきます mean either a habit or a future trip without more context?','Yes.','The polite nonpast form alone does not choose between those readings.'),
 ('What two basic meanings can のみません have: “do not drink,” “will not drink,” or “drank”?','“Do not drink” and “will not drink.”','It is negative nonpast, not past.'),
 ('Write: I will study tomorrow. Use べんきょうする; the subject may be omitted.','あした べんきょうします。','No に after あした; する → します.'),
 ('Write: I do not watch TV on Sundays. Begin にちようびは.','にちようびは テレビを みません。','The day is the topic; みません expresses a negative habit.'),
 ('In まいあさ しちじに おきます, is おきる a ru-verb, an irregular verb, or a tense label?','A ru-verb.','Its meaning is getting up; its group is ru, and ます describes a habit here.')
]:q('tense',p,a,w)

for p,a,w in [
 ('Fill with を, で, or に: みず（　）のみます。','を','Water is the direct object of drinking.'),
 ('Fill with を, で, or に: としょかん（　）ほんを よみます。','で','The library is where the reading happens.'),
 ('Fill with を, で, or に: がっこう（　）いきます。','に','School is the destination. へ is also possible outside this choice set.'),
 ('Fill with を, で, or に: しちじ（　）おきます。','に','A specified clock time takes に.'),
 ('Fill with を, で, or に: えいが（　）みます。','を','The movie is what is watched.'),
 ('Fill with を, で, or に: うち（　）べんきょうします。','で','Home is the action setting.'),
 ('Fill with を, で, or に: うち（　）かえります。','に','Home is the destination of returning.'),
 ('Fill with を, で, or に: おんがく（　）ききます。','を','Music is what is listened to.'),
 ('Fill with を, で, or に: きっさてん（　）コーヒーを のみます。','で','The cafe is where drinking happens.'),
 ('Fill with を, で, or に: にほんご（　）はなします。','を','The language spoken is marked by を in this sentence.'),
 ('Fill with を, で, or に: だいがく（　）きます。','に','The university is the destination of coming.'),
 ('Fill with を, で, or に: じゅういちじ（　）ねます。','に','A clock time takes に.'),
 ('Fill both blanks using を, で, or に: レストラン（　）ひるごはん（　）たべます。','で、を','Action location で; object を.'),
 ('Fill both blanks using を, で, or に: としょかん（　）にほんご（　）べんきょうします。','で、を','Studying happens at the library; Japanese is what is studied.'),
 ('Fill both blanks using を, で, or に: ごごさんじ（　）としょかん（　）いきます。','に、に','The first に marks time; the second marks destination.'),
 ('Replace destination に with another correct particle: がっこうに いきます。','がっこうへ いきます。','へ can mark direction/destination with movement verbs.'),
 ('How is the particle へ pronounced in がっこうへ いきます? Answer in English letters.','e','The particle is written へ but pronounced e.'),
 ('How is the particle を normally pronounced? Answer in English letters.','o','Its particle pronunciation is o.'),
 ('Correct the particle for the intended meaning “I study at the library”: としょかんに べんきょうします。','としょかんで べんきょうします。','Use で for the setting of studying.'),
 ('Correct the particle for “I go to the library”: としょかんで いきます。','としょかんに いきます。 / としょかんへ いきます。','Movement toward a destination takes に or へ.'),
 ('Correct the particle for “I drink coffee”: コーヒーで のみます。','コーヒーを のみます。','Coffee is the object, not the setting.'),
 ('For “Where do you study?”, choose どこで or どこに.','どこで','Ask about the setting of an activity: どこで べんきょうしますか。'),
 ('For “Where will you go?”, choose どこで or どこに.','どこに','Ask about a destination: どこに いきますか。 どこへ is also possible.'),
 ('Can へ replace に in しちじに おきます?','No.','へ marks direction, not clock time.'),
 ('Write: I read a magazine at home. Use うち, ざっし, よむ.','うちで ざっしを よみます。','で marks the place, を marks the object, and よむ → よみます.')
]:q('particles',p,a,w)

for p,a,w in [
 ('Fill with に or nothing: あした（　）べんきょうします。','Nothing.','あした normally stands without time に.'),
 ('Fill with に or nothing: きょう（　）うちに かえります。','Nothing.','きょう is a relative time expression.'),
 ('Fill with に or nothing: まいにち（　）おんがくを ききます。','Nothing.','Repeating expressions such as まいにち normally take no に.'),
 ('Fill with に or nothing: こんや（　）テレビを みます。','Nothing.','こんや normally takes no に.'),
 ('Fill with に or nothing: ごぜんくじ（　）がっこうに いきます。','に','A specified clock time takes に.'),
 ('Fill with に or nothing: しちじはん（　）あさごはんを たべます。','に','Half past seven is a specified clock time.'),
 ('Fill with に or nothing: いつ（　）いきますか。','Nothing.','いつ normally has no に.'),
 ('Fill with に or nothing: なんじ（　）おきますか。','に','The standard question is なんじに.'),
 ('For どようび（　）いきます, are both に and no particle possible?','Yes.','Days of the week can take に, and it can be omitted in context.'),
 ('Correct the unnecessary time particle: あしたに としょかんに いきます。','あした としょかんに いきます。','Remove time に after あした; keep destination に.'),
 ('Write “at 4:00” entirely in kana, including the particle.','よじに','4:00 is よじ, not よんじ.'),
 ('Write “at 9:00 p.m.” entirely in kana, including the particle.','ごごくじに','9:00 is くじ; ごご specifies p.m.'),
 ('Write: What time do you go to bed? Use ねる.','なんじに ねますか。','Clock-time question なんじに + ねますか.'),
 ('Write: I get up at 6:30 every morning.','まいあさ ろくじはんに おきます。','No に after まいあさ; に after the clock time.'),
 ('Write: I will go to school tomorrow at 8:00. Use destination に.','あした はちじに がっこうに いきます。','Relative day without に, clock time with に, destination with に.')
]:q('time',p,a,w)

for p,a,w in [
 ('Turn たべる into a polite invitation ending in か.','たべませんか。','たべ + ません + か.'),
 ('Turn のむ into a polite invitation ending in か.','のみませんか。','のむ → のみ; add ませんか.'),
 ('Turn いく into a polite invitation ending in か.','いきませんか。','いく → いき; add ませんか.'),
 ('Turn する into a polite invitation ending in か.','しませんか。','The irregular stem is し.'),
 ('Turn くる into a polite invitation ending in か.','きませんか。','The irregular stem is き.'),
 ('Translate as an invitation: いっしょに コーヒーを のみませんか。','Would you like to have coffee together?','The context makes ませんか an invitation.'),
 ('Invite someone to see a movie on Saturday. Use どようびに and みる.','どようびに えいがを みませんか。','Time に + object を + invitation.'),
 ('Invite someone to study at the library tomorrow.','あした としょかんで べんきょうしませんか。','No に after あした; action-location で; する → しませんか.'),
 ('Invite someone to have lunch together.','いっしょに ひるごはんを たべませんか。','いっしょに means together; lunch is the object.'),
 ('Give a short, positive response to an invitation: “That sounds good.”','いいですね。','This clearly accepts the suggestion in this context.'),
 ('Gently decline a Saturday invitation using すみません and ちょっと.','すみません。どようびは ちょっと……。','The unfinished ちょっと conventionally implies difficulty.'),
 ('You agree to go. Ask “At what time will we go?”','なんじに いきますか。','なんじに asks for a clock time.'),
 ('You agree to have lunch. Ask “Where will we eat?”','どこで たべますか。','Ask where the action happens, so use で.'),
 ('Correct the invitation: えいがを みますませんか。','えいがを みませんか。','Use stem + ませんか, not ます + ませんか.'),
 ('In an invitation context, how does のみませんか differ from のみません?','のみませんか invites someone to drink; のみません states that someone does not / will not drink.','か and the invitation context change the function of the sentence.')
]:q('invites',p,a,w)

for p,a,w in [
 ('Complete for “I do not watch TV very often”: あまり テレビを（みます／みません）。','みません','あまり pairs with a negative ending in this pattern.'),
 ('Complete for “I do not drink coffee at all”: ぜんぜん コーヒーを（のみます／のみません）。','のみません','ぜんぜん + negative means not at all.'),
 ('Choose “sometimes”: いつも / ときどき / ぜんぜん.','ときどき','いつも = always; ぜんぜん with a negative = not at all.'),
 ('Choose “usually”: たいてい / よく / あまり.','たいてい','よく = often; あまり with a negative = not very much.'),
 ('Translate: よく としょかんで ほんを よみます。','I often read books at the library.','よく gives frequency, で gives place, を gives object.'),
 ('Correct the ending for “I do not listen to music very often”: あまり おんがくを ききます。','あまり おんがくを ききません。','Keep あまり and change the verb to negative.'),
 ('Order every chunk once: よみます / ほんを / わたしは / としょかんで.','わたしは としょかんで ほんを よみます。','Other natural orders can work; keep particles attached and the verb last.'),
 ('Order every chunk once: あした / いきます / がっこうに / わたしは.','わたしは あした がっこうに いきます。','あした わたしは がっこうに いきます is also acceptable.'),
 ('Order every chunk once: か / コーヒーを / のみません / いっしょに.','いっしょに コーヒーを のみませんか。','Place か after the final verb.'),
 ('Which phrase is the topic in しゅうまつは よく えいがを みます?','しゅうまつ','The topic is the weekend, not the movie or the person.'),
 ('How is the topic particle は pronounced? Answer in English letters.','wa','The spelling is は, while the topic-particle pronunciation is wa.'),
 ('Make coffee the topic: コーヒーを のみません。','コーヒーは のみません。','In this simple object-topic pattern, は replaces を.'),
 ('Correct the topic marking: コーヒーをは のみません。','コーヒーは のみません。','Do not combine をは in this pattern.'),
 ('Explain the contrast: コーヒーは のみません。おちゃは のみます。','I do not drink coffee, but I do drink tea.','Each object is made a topic with は; the endings create the contrast.'),
 ('What role does では play in うちでは べんきょうしません?','で marks the action location; は makes that location a topic or contrast.','The sentence means “At home, I do not study.” It may contrast home with another location.')
]:q('structure',p,a,w)

READINGS = [
 dict(id='R1',title='Aki’s weekday routine',text='わたしは アキです。まいあさ ろくじはんに おきます。しちじに うちで あさごはんを たべます。はちじに がっこうに いきます。ごごよじに うちに かえります。ばんは よく おんがくを ききます。テレビは あまり みません。',translation='I am Aki. Every morning I get up at 6:30. At 7:00 I eat breakfast at home. At 8:00 I go to school. At 4:00 p.m. I return home. In the evening I often listen to music. I do not watch TV very much.',items=[
 ('What time does Aki get up?','6:30.','ろくじはんに おきます gives the time.'),
 ('Where does Aki eat breakfast?','At home.','うちで marks the setting for eating.'),
 ('What is the destination at 8:00?','School.','がっこうに いきます names the destination.'),
 ('Does Aki never watch TV, or not watch it very much?','Aki does not watch it very much.','あまり + みません is weaker than ぜんぜん + みません.'),
 ('Copy the verb form meaning “return home” and give its dictionary form and group.','かえります; かえる; u-verb.','Final る changes to り before ます.')]),
 dict(id='R2',title='A Saturday invitation',text='ユイ：どようびに いっしょに えいがを みませんか。\nケン：いいですね。なんじに いきますか。\nユイ：ごごにじに いきます。\nケン：ひるごはんは？\nユイ：じゅうにじに レストランで たべませんか。\nケン：いいですね。',translation='Yui: Would you like to see a movie together on Saturday? Ken: Sounds good. What time will we go? Yui: We will go at 2:00 p.m. Ken: What about lunch? Yui: Would you like to eat at a restaurant at 12:00? Ken: Sounds good.',items=[
 ('What day is proposed for the movie?','Saturday.','どようびに is the day phrase.'),
 ('Does Ken accept the movie invitation? Give the Japanese evidence.','Yes: いいですね。','This response accepts the suggestion.'),
 ('What time will they go for the movie plan?','2:00 p.m.','ごごにじに いきます. The dialogue does not explicitly give the movie’s starting time.'),
 ('Where and when is lunch proposed?','At a restaurant at 12:00.','じゅうにじに marks time; レストランで marks place.'),
 ('Copy one invitation verb form from the dialogue.','みませんか / たべませんか','Both use the polite negative ending + か as invitations.')]),
 dict(id='R3',title='Nao’s study habits',text='ナオさんは まいにち にほんごを べんきょうします。たいてい としょかんで べんきょうします。うちでは あまり べんきょうしません。ときどき きっさてんで ほんを よみます。コーヒーは のみません。おちゃは よく のみます。',translation='Nao studies Japanese every day. Nao usually studies at the library. At home, Nao does not study very much. Sometimes Nao reads books at a cafe. Nao does not drink coffee. Nao often drinks tea.',items=[
 ('How often does Nao study Japanese?','Every day.','まいにち sets the overall study frequency.'),
 ('Where does Nao usually study?','At the library.','たいてい としょかんで gives the usual setting.'),
 ('True or false: Nao never studies at home. Explain from the wording.','False. The passage says not very much.','あまり べんきょうしません does not mean never.'),
 ('Which drink does Nao often have?','Tea.','おちゃは よく のみます.'),
 ('In コーヒーは のみません, why is コーヒー followed by は instead of を?','Coffee is the topic, contrasted here with tea.','は replaces を in this object-topic construction.')]),
 dict(id='R4',title='Moving the plan to Sunday',text='リナ：あした いっしょに としょかんで べんきょうしませんか。\nソラ：あしたは ちょっと……。にちようびは？\nリナ：いいですね。ごぜんくじに としょかんに いきます。\nソラ：わたしは くじはんに いきます。\nリナ：じゃあ、じゅうじに いっしょに べんきょうします。ひるごはんは じゅうにじに たべませんか。\nソラ：いいですね。',translation='Rina: Would you like to study together at the library tomorrow? Sora: Tomorrow is a little difficult ... How about Sunday? Rina: Sounds good. I will go to the library at 9:00 a.m. Sora: I will go at 9:30. Rina: Well then, we will study together at 10:00. Would you like to have lunch at 12:00? Sora: Sounds good.',items=[
 ('Does Sora accept the initial plan for tomorrow?','No; Sora gently declines it.','あしたは ちょっと…… is a soft refusal in this context.'),
 ('What replacement day does Sora suggest?','Sunday.','にちようびは？ asks “What about Sunday?”'),
 ('Who says they will go to the library at 9:00, Rina or Sora?','Rina.','Sora says くじはん, or 9:30.'),
 ('At what time will they study together?','10:00.','じゅうじに いっしょに べんきょうします.'),
 ('Explain the difference between としょかんで and としょかんに in this dialogue.','で marks where studying happens; に marks the destination of going.','The same place has different roles with different verbs.')])
]
for lab in READINGS:
    for p,a,w in lab['items']:q('reading',p,a,w,lab['id'])

LISTENINGS = [
 dict(id='L1',title='Morning and evening',focus='Clock times, affirmative and negative endings',lines=[
 'わたしはミカです。','まいあさ、しちじにおきます。','しちじはんに、あさごはんをたべます。','コーヒーはのみません。おちゃをのみます。','はちじに、がっこうにいきます。','まいばん、じゅういちじにねます。'],
 translation='I am Mika. Every morning I get up at 7:00. At 7:30 I eat breakfast. I do not drink coffee. I drink tea. At 8:00 I go to school. Every evening I go to bed at 11:00.',items=[
 ('What time does Mika get up?','7:00.','しちじに おきます.'),
 ('What time is breakfast?','7:30.','しちじはんに あさごはんを たべます.'),
 ('Which drink does Mika have, coffee or tea?','Tea.','コーヒーは のみません. おちゃを のみます.'),
 ('Where does Mika go at 8:00?','To school.','がっこうに いきます names the destination.'),
 ('Write in kana only the final verb you hear, meaning “go to bed.”','ねます','The final line ends じゅういちじに ねます.')]),
 dict(id='L2',title='An invitation for tomorrow',focus='Invitation, agreement, location, and time',lines=[
 'あした、いっしょにひるごはんをたべませんか。','いいですね。どこでたべますか。','レストランでたべます。','なんじにたべますか。','じゅうにじはんにたべます。','いいですね。'],
 translation='Would you like to have lunch together tomorrow? Sounds good. Where will we eat? We will eat at a restaurant. What time will we eat? We will eat at 12:30. Sounds good.',items=[
 ('Is the invitation for today or tomorrow?','Tomorrow.','あした appears at the start.'),
 ('What activity is proposed?','Having lunch together.','いっしょに ひるごはんを たべませんか.'),
 ('Where will they eat?','At a restaurant.','レストランで たべます.'),
 ('At what time will they eat?','12:30.','じゅうにじはんに たべます.'),
 ('Write the invitation verb form you hear in kana.','たべませんか','The first line uses たべ + ませんか.')]),
 dict(id='L3',title='How often?',focus='Frequency and negative endings',lines=[
 'わたしはハルです。','まいにち、にほんごをべんきょうします。','よく、としょかんでほんをよみます。','ときどき、えいがをみます。','テレビは、あまりみません。','コーヒーは、ぜんぜんのみません。'],
 translation='I am Haru. I study Japanese every day. I often read books at the library. I sometimes watch movies. I do not watch TV very much. I do not drink coffee at all.',items=[
 ('What does Haru do every day?','Studies Japanese.','まいにち にほんごを べんきょうします.'),
 ('Where does Haru often read?','At the library.','よく としょかんで ほんを よみます.'),
 ('How often does Haru watch movies?','Sometimes.','ときどき is attached to watching movies.'),
 ('Does Haru watch TV often?','No; not very much / not very often.','あまり みません gives the limited frequency.'),
 ('Does Haru drink coffee at all?','No.','ぜんぜん のみません means not at all.')]),
 dict(id='L4',title='Same place, different job',focus='Destination に, location で, and clock times',lines=[
 'あした、ごぜんくじに、としょかんにいきます。','としょかんで、にほんごをべんきょうします。','じゅうにじに、きっさてんにいきます。','きっさてんで、コーヒーをのみます。','ごごにじに、うちにかえります。'],
 translation='Tomorrow at 9:00 a.m. I will go to the library. I will study Japanese at the library. At 12:00 I will go to a cafe. I will drink coffee at the cafe. At 2:00 p.m. I will return home.',items=[
 ('Where does the speaker go at 9:00 a.m.?','To the library.','としょかんに いきます.'),
 ('What does the speaker do at the library?','Studies Japanese.','としょかんで にほんごを べんきょうします.'),
 ('Where does the speaker go at 12:00?','To a cafe.','じゅうにじに きっさてんに いきます.'),
 ('What does the speaker drink there?','Coffee.','きっさてんで コーヒーを のみます.'),
 ('Write the final verb in kana and state the time of that action in English.','かえります; 2:00 p.m.','ごごにじに うちに かえります.')]),
 dict(id='L5',title='A change of day',focus='Soft refusal, a new invitation, and confirming details',lines=[
 'どようびに、いっしょにえいがをみませんか。','すみません。どようびはちょっと。','じゃあ、にちようびは。','いいですね。なんじにいきますか。','ごごさんじにいきます。','ひるごはんは。','じゅうにじに、レストランでたべませんか。','いいですね。'],
 translation='Would you like to see a movie together on Saturday? Sorry, Saturday is a little difficult ... Well then, how about Sunday? Sounds good. What time will we go? We will go at 3:00 p.m. What about lunch? Would you like to eat at a restaurant at 12:00? Sounds good.',items=[
 ('Which day is initially proposed?','Saturday.','どようびに begins the first invitation.'),
 ('Does どようびは ちょっと mean acceptance or a gentle refusal here?','A gentle refusal.','With すみません, the unfinished response signals difficulty.'),
 ('What day is finally accepted?','Sunday.','にちようびは receives いいですね.'),
 ('At what time will they go for the movie plan?','3:00 p.m.','ごごさんじに いきます. A movie start time is not explicitly stated.'),
 ('What are the proposed lunch time and location?','12:00, at a restaurant.','じゅうにじに レストランで たべませんか.')])
]
for lab in LISTENINGS:
    for p,a,w in lab['items']:q('listening',p,a,w,lab['id'])

for p,a,w in [
 ('Give the group and polite nonpast negative of かえる (return home).','u-verb; かえりません','Final る → り; then add ません.'),
 ('Give the group and polite nonpast affirmative of おきる.','ru-verb; おきます','Remove る and add ます.'),
 ('Write: I will not come tomorrow. Use くる.','あした きません。','くる → きません; no に after あした.'),
 ('Write: I study Japanese at the library every day.','まいにち としょかんで にほんごを べんきょうします。','No time に after まいにち; location で; object を; irregular します.'),
 ('Write: I will go home at 4:00 p.m. Use かえる and destination に.','ごごよじに うちに かえります。','4:00 is よじ. The two に particles mark time and destination.'),
 ('Write: I do not watch movies very often. Use あまり.','あまり えいがを みません。','あまり needs a negative predicate in this pattern.'),
 ('Invite someone to have lunch together at 12:00 tomorrow.','あした じゅうにじに いっしょに ひるごはんを たべませんか。','Check relative day, exact time, object, and invitation ending.'),
 ('Use は twice to contrast these: “I do not drink coffee. I drink tea.”','コーヒーは のみません。おちゃは のみます。','Both objects become contrasting topics; を is replaced.'),
 ('Translate the difference: まいにち ほんを よみます。 / あした ほんを よみます。','I read books every day. / I will read a book tomorrow.','The same nonpast verb form expresses habit or future depending on the time expression.'),
 ('Write a two-turn dialogue: invite a friend to study at the library on Sunday at 10:00; the friend accepts. Use にちようびに.','A: にちようびに じゅうじに としょかんで べんきょうしませんか。\nB: いいですね。','Full credit: day, clock time, action place, correct invitation, and a clear acceptance. Natural alternative word order is fine.')
]:q('mastery',p,a,w)

assert len(QUESTIONS)==200,len(QUESTIONS)
assert [q['id'] for q in QUESTIONS]==list(range(1,201))
