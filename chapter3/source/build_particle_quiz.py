"""Build the self-contained kana-only 100-question particle quiz."""
import json
import random
from collections import Counter
from pathlib import Path
import re

from particle_quiz_support import romaji_sentence, word_help


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = Path(__file__).with_name("particle_quiz_template.html")
APP = Path(__file__).with_name("particle_quiz_app.js")

PARTICLE_OPTIONS = {
    "を": ["を", "で", "に", "へ"],
    "に": ["に", "を", "で", "へ"],
    "で": ["で", "に", "を", "へ"],
    "へ": ["へ", "に", "で", "を"],
    "は": ["は", "の", "を", "で"],
    "の": ["の", "は", "を", "も"],
    "も": ["も", "は", "の", "を"],
    "か": ["か", "ね", "よ", "の"],
    "ね": ["ね", "よ", "か", "の"],
    "よ": ["よ", "ね", "か", "の"],
}


def make_particle(category, prompt, why, ordinal, accepted=None):
    if category in {"を", "に", "で", "へ"}:
        prompt = re.sub(
            r"^(?:Fill the (?:object|time|day|action-place) blank|"
            r"Choose (?:the movement|a destination) particle):",
            "Complete the sentence:", prompt,
        )
    choices = PARTICLE_OPTIONS[category][:]
    shift = ordinal % len(choices)
    choices = choices[shift:] + choices[:shift]
    answer = choices.index(category)
    good = [answer]
    if accepted:
        good = [i for i, value in enumerate(choices) if value in accepted]
    return {"category": category, "kind": "particle", "prompt": prompt,
            "choices": choices, "answers": good, "why": why}


questions = []

# Direct objects marked by を. Several items bring in earlier question words,
# demonstratives, and possessive の while keeping the particle decision central.
objects = [
    ("Fill the object blank: はるかさんは パン（　）たべます。", "パン is what Haruka eats, so it is the direct object."),
    ("Fill the object blank: たなかさんは みず（　）のみます。", "みず is what Tanaka drinks, so を marks it as the direct object."),
    ("Fill the object blank: わたしは ほん（　）よみます。", "ほん is what the speaker reads."),
    ("Fill the object blank: まいさんは おんがく（　）ききます。", "おんがく is what Mai listens to."),
    ("Fill the object blank: けんさんは テレビ（　）みます。", "テレビ is what Ken watches."),
    ("Fill the object blank: あきさんは ノート（　）かいます。", "ノート is what Aki buys."),
    ("Fill the object blank: ゆきさんは なまえ（　）かきます。", "なまえ is what Yuki writes."),
    ("Fill the object blank: たろうさんは にほんご（　）べんきょうします。", "にほんご is what Taro studies."),
    ("Fill the object blank: どようびに サッカー（　）します。", "サッカー is the activity done; use を with します."),
    ("Ask what someone drinks: なに（　）のみますか。", "なに means “what”; it is the thing being drunk, so use を."),
    ("Ask which book someone reads: どの ほん（　）よみますか。", "どの ほん means “which book”; the whole phrase is the object of よみます."),
    ("Ask about the thing being bought: あれ（　）かいますか。", "あれ means “that one over there”; it is the object being bought."),
    ("Fill the object blank: その えいが（　）みますか。", "その えいが means “that movie”; it is the object of みます."),
    ("Ask what someone reads at the library: としょかんで なに（　）よみますか。", "なに asks “what”; を marks the thing read. The fixed で marks where the reading happens."),
    ("Ask which movie someone watches: どの えいが（　）みますか。", "どの えいが means “which movie”; it is the object of みます."),
    ("Ask which one someone buys: どれ（　）かいますか。", "どれ means “which one” and can stand alone as the direct object."),
    ("Fill the object blank: きょう やさい（　）かいます。", "やさい is what the speaker buys."),
    ("Ask what someone eats today: きょう なに（　）たべますか。", "なに asks “what”; it is the direct object of たべます."),
    ("Fill the object blank: まいにち しんぶん（　）よみますか。", "しんぶん is what is read each day."),
    ("Ask what someone studies at the university: だいがくで なに（　）べんきょうしますか。", "なに asks what is studied, so it takes を. The fixed で marks the place of study."),
]
for n, (prompt, why) in enumerate(objects):
    questions.append(make_particle("を", prompt, why, n))

# に marks clock times and days; it can also mark a destination. Both に and へ
# may be natural with destinations, so the quiz accepts either where appropriate.
times = [
    ("Fill the time blank: わたしは しちじ（　）おきます。", "A clock time such as しちじ takes に."),
    ("Fill the time blank: あきさんは はちじ（　）ねます。", "A specific clock time takes に."),
    ("Ask “At what time do you study?”: なんじ（　）べんきょうしますか。", "なんじ asks “what time”; に marks the time."),
    ("Fill the day blank: げつようび（　）としょかんへ いきます。", "A named day of the week can take に."),
    ("Fill the day blank: どようび（　）えいがを みます。", "に marks the named day, どようび."),
    ("Fill the time blank: まいばん じゅういちじ（　）ねます。", "じゅういちじ is a specific clock time, so use に."),
    ("Fill the time blank: まいあさ ろくじ（　）おきます。", "に follows the clock time ろくじ."),
    ("Fill the day blank: きんようび（　）にほんごを べんきょうします。", "きんようび is a named weekday, marked with に."),
    ("Fill the time blank: なんじ（　）うちへ かえりますか。", "なんじ asks when; に marks the time of going home."),
    ("Fill the day blank: にちようび（　）こうえんへ いきます。", "に can mark the named day にちようび."),
    ("Fill the time blank: たなかさんは ごぜん くじ（　）だいがくへ いきます。", "に marks the scheduled time ごぜん くじ."),
    ("Fill the time blank: じゅうじ（　）ほんを よみます。", "に marks the specific time じゅうじ."),
    ("Fill the day blank: すいようび（　）えいがを みます。", "すいようび is a named weekday, so に is natural."),
    ("Fill the time blank: まいにち はちじ（　）あさごはんを たべます。", "The specific time はちじ takes に."),
    ("Ask the time: なんじ（　）きっさてんで コーヒーを のみますか。", "なんじ asks “what time”; use に for the clock time."),
    ("Fill the day blank: もくようび（　）としょかんで べんきょうします。", "に marks the weekday もくようび."),
    ("Fill the time blank: はるかさんは ごご さんじ（　）ともだちに でんわします。", "さんじ is a clock time. に marks when the call is made."),
    ("Fill the day blank: かようび（　）だいがくで ほんを よみます。", "Use に after a named weekday."),
    ("Fill the time blank: まいばん くじ（　）テレビを みます。", "くじ is the time; に marks when the action happens."),
    ("Fill the day blank: どようび（　）なにを しますか。", "どようび takes に as a specified day; なに asks “what.”"),
]
ni_destinations = {
    6: ("Choose a destination particle: あした がっこう（　）いきます。", "がっこう is the destination. に and へ can both mark movement toward it.", ["に", "へ"]),
    8: ("Ask where Mai is going: まいさんは どこ（　）いきますか。", "どこ asks for the destination; both に and へ are natural.", ["に", "へ"]),
    11: ("Choose a destination particle: としょかん（　）きます。", "としょかん is where the person is coming to; に and へ both work.", ["に", "へ"]),
    13: ("Choose a destination particle: どようびに きっさてん（　）いきます。", "きっさてん is the destination. Both に and へ can mark it.", ["に", "へ"]),
    16: ("Choose a destination particle: けんさんは うち（　）かえります。", "うち is the destination of returning home; either に or へ is natural.", ["に", "へ"]),
    18: ("Ask where Yuki is going: ゆきさんは どこ（　）いきますか。", "どこ asks for a destination; both に and へ can mark it.", ["に", "へ"]),
}
for n, (prompt, why) in enumerate(times):
    if n in ni_destinations:
        prompt, why, accepted = ni_destinations[n]
        questions.append(make_particle("に", prompt, why, n, accepted))
    else:
        questions.append(make_particle("に", prompt, why, n))

# で marks the place where an action happens. ここ / そこ / あそこ and どこ
# bring in the place words from the previous chapter.
places = [
    ("Fill the action-place blank: わたしは としょかん（　）ほんを よみます。", "で marks where the reading happens; the book is the object marked by を."),
    ("Ask where someone buys bread: どこ（　）パンを かいますか。", "どこで asks “where” an action takes place."),
    ("Fill the action-place blank: きっさてん（　）コーヒーを のみます。", "で marks the place where the person drinks coffee."),
    ("Fill the action-place blank: うち（　）テレビを みます。", "うちで means the action of watching happens at home."),
    ("Fill the action-place blank: こうえん（　）サッカーを します。", "で marks the location of the soccer activity."),
    ("Fill the action-place blank: だいがく（　）にほんごを べんきょうします。", "で marks where the studying happens."),
    ("Fill the action-place blank: みせ（　）みずを かいます。", "で marks the shop as the location where the buying happens."),
    ("Ask “Where do you study Japanese?”: にほんごは どこ（　）べんきょうしますか。", "どこで asks where the action べんきょうします happens."),
    ("Fill the action-place blank: ここ（　）ほんを よみます。", "ここ means “here”; で marks the place of the action."),
    ("Fill the action-place blank: そこ（　）にほんごを べんきょうします。", "そこ means “there”; で marks where studying happens."),
    ("Fill the action-place blank: あそこ（　）えいがを みます。", "あそこで means the action happens over there."),
    ("Ask what someone buys at this shop: この みせで なに（　）かいますか。", "なに asks what is bought and を marks that direct object."),
    ("Ask which cafe someone drinks coffee at: どの きっさてん（　）コーヒーを のみますか。", "で marks which cafe is the place where the action happens."),
    ("Fill the action-place blank: まいにち うち（　）しんぶんを よみます。", "で marks the place of the reading."),
    ("Ask what someone studies at the university: だいがく（　）なにを べんきょうしますか。", "だいがくで asks where; なにを asks what is studied."),
    ("Fill the action-place blank: がっこう（　）えいごを べんきょうします。", "で marks where studying takes place."),
    ("Fill the action-place blank: へや（　）おんがくを ききます。", "で marks the room as the setting for listening."),
    ("Ask where someone watches television: どこ（　）テレビを みますか。", "どこで is the question form for an action location."),
    ("Fill the action-place blank: きょうは としょかん（　）なにを よみますか。", "で marks the reading location; なにを asks what is read."),
    ("Fill the action-place blank: その きっさてん（　）ともだちに でんわします。", "で marks where the phone call happens."),
]
for n, (prompt, why) in enumerate(places):
    questions.append(make_particle("で", prompt, why, n))

# へ marks movement toward a destination and is pronounced “e.” に is also
# natural for many destinations, so both destination answers are accepted.
destinations = [
    ("Choose the movement particle: がっこう（　）いきます。", "がっこう is the destination. Both に and へ can mark movement toward it.", ["に", "へ"]),
    ("Choose the movement particle: あした としょかん（　）いきます。", "としょかん is the destination; に and へ are both natural here.", ["に", "へ"]),
    ("Ask “Where are you going?”: どこ（　）いきますか。", "どこ asks for the destination; either に or へ can mark it." , ["に", "へ"]),
    ("Choose the movement particle: きょうと（　）いきます。", "きょうと is the destination; に and へ can both mark movement toward it." , ["に", "へ"]),
    ("Choose the movement particle: うち（　）かえります。", "うち is the destination of going home; に and へ are both possible." , ["に", "へ"]),
    ("Choose the movement particle: えき（　）いきます。", "えき is the destination. に and へ are both natural choices." , ["に", "へ"]),
    ("Ask where Aki is going: あきさんは どこ（　）いきますか。", "どこ asks for the destination, marked naturally by に or へ." , ["に", "へ"]),
    ("Choose the movement particle: らいしゅう にほん（　）いきます。", "にほん is the destination; に and へ both work." , ["に", "へ"]),
    ("Choose the movement particle: まいにち だいがく（　）いきます。", "だいがく is the destination. Both に and へ may mark it." , ["に", "へ"]),
    ("Choose the movement particle: あした きっさてん（　）いきます。", "きっさてん is where the person is going; に and へ are both possible." , ["に", "へ"]),
    ("Choose the movement particle: ともだちは とうきょう（　）きます。", "とうきょう is where the friend is coming to; に and へ can both mark it." , ["に", "へ"]),
    ("Choose the movement particle: たなかさんは うち（　）かえります。", "うち is the destination of returning; either に or へ is natural." , ["に", "へ"]),
    ("Ask “Where are you going on Saturday?”: どようびに どこ（　）いきますか。", "どこ asks for the destination; use に or へ." , ["に", "へ"]),
    ("Choose the movement particle: あのひとは ぎんこう（　）いきます。", "ぎんこう is the destination; に or へ marks movement toward it." , ["に", "へ"]),
    ("Choose the movement particle: せんせいは きょうと（　）かえります。", "きょうと is the destination. Both に and へ are accepted." , ["に", "へ"]),
    ("Ask where your friend is going: ともだちは どこ（　）いきますか。", "どこ asks “where to”; に and へ both mark that destination." , ["に", "へ"]),
    ("Choose the movement particle: あさ えき（　）いきます。", "えき is where the person is going; に and へ both fit." , ["に", "へ"]),
    ("Choose the movement particle: まいしゅう としょかん（　）いきます。", "としょかん is the destination; either に or へ is natural." , ["に", "へ"]),
    ("Choose the movement particle: らいしゅう うち（　）かえります。", "うち is the destination of returning; に and へ may both be used." , ["に", "へ"]),
    ("Ask where the teacher is going: せんせいは どこ（　）いきますか。", "どこ asks for a destination; に or へ can mark it." , ["に", "へ"]),
]
for n, (prompt, why, accepted) in enumerate(destinations):
    questions.append(make_particle("へ", prompt, why, n, accepted))

earlier_particles = [
    ("は", "Ask “What is this?”: これ（　）なんですか。", "は marks これ as the topic: “What is this?”"),
    ("は", "Ask “Where is the library?”: としょかん（　）どこですか。", "は marks the library as the topic; どこ asks “where.”"),
    ("は", "Ask “How is Japanese class?”: にほんごの クラス（　）どうですか。", "は marks the class as the topic; どう asks “how.”"),
    ("は", "Ask “Who is that person?”: あのひと（　）だれですか。", "は marks that person as the topic; だれ asks “who.”"),
    ("の", "Say “It is my book”: わたし（　）ほんです。", "の connects an owner and a noun: わたしの ほん, “my book.”"),
    ("の", "Ask “Whose notebook is this?”: これは だれ（　）ノートですか。", "だれの means “whose.”"),
    ("の", "Say “It is a Japanese class”: にほんご（　）クラスです。", "の links にほんご and クラス."),
    ("の", "Say “It is the teacher's bag”: せんせい（　）かばんです。", "の shows whose bag it is."),
    ("も", "After saying that one is a book, add “This is also a book”: これ（　）ほんです。", "も means “also” and takes the place of は here."),
    ("も", "After saying this one is a notebook, add “That over there is also a notebook”: あれ（　）ノートです。", "も adds “also” to the topic."),
    ("も", "After saying Haruka is a student, say “I am also a student”: わたし（　）がくせいです。", "も means “also” and replaces は."),
    ("も", "After saying Ken studies Japanese, add “Mai studies Japanese too”: まいさん（　）にほんごを べんきょうします。", "も means “too” for Mai, who does the same action."),
    ("か", "Ask “Is this a book?”: これは ほんです（　）。", "か turns the polite statement into a question."),
    ("か", "Ask “Where is the station?”: えきは どこです（　）。", "か marks the end of a polite question; どこ asks “where.”"),
    ("か", "Ask “How much is this book?”: この ほんは いくらです（　）。", "か makes this a question; いくら asks “how much.”"),
    ("か", "Ask “How is the coffee?”: コーヒーは どうです（　）。", "か marks a question; どう asks “how.”"),
    ("ね", "Your friend says the book is good, and you agree: いい ほんです（　）。", "ね invites agreement, like “isn't it?”"),
    ("ね", "You and your friend both enjoyed the movie; agree that it was good: いい えいがです（　）。", "ね shares an observation and invites agreement."),
    ("よ", "Tell your friend information they did not know, “That is my book”: あれは わたしの ほんです（　）。", "よ gives the listener new information or emphasis."),
    ("よ", "Tell your friend something they did not know, “This is the library”: ここは としょかんです（　）。", "よ adds an informative or emphatic tone."),
]
for n, (category, prompt, why) in enumerate(earlier_particles):
    questions.append(make_particle(category, prompt, why, n))

assert len(questions) == 100, f"Expected 100 questions, got {len(questions)}"
counts = Counter(q["category"] for q in questions)
assert counts == {"を": 20, "に": 20, "で": 20, "へ": 20,
                  "は": 4, "の": 4, "も": 4, "か": 4, "ね": 2, "よ": 2}

# Mix one item from each Lesson 3 particle and one earlier-particle item in
# every five-question span. A fixed seed keeps the order stable across builds.
rng = random.Random(311)
core = ["を", "に", "で", "へ"]
pools = {key: [q for q in questions if q["category"] == key] for key in core}
pools["earlier"] = [q for q in questions if q["category"] not in core]
rng.shuffle(pools["earlier"])
mixed = []
last_group = None
for round_number in range(20):
    groups = [*core, "earlier"]
    rng.shuffle(groups)
    if groups[0] == last_group:
        swap_at = next(i for i, group in enumerate(groups) if group != last_group)
        groups[0], groups[swap_at] = groups[swap_at], groups[0]
    for group in groups:
        question = pools[group][round_number]
        paired = [(choice, i in question["answers"])
                  for i, choice in enumerate(question["choices"])]
        rng.shuffle(paired)
        question["choices"] = [choice for choice, _ in paired]
        question["answers"] = [i for i, (_, accepted) in enumerate(paired) if accepted]
        mixed.append(question)
    last_group = groups[-1]
questions = mixed

for number, question in enumerate(questions, 1):
    question["id"] = number
    assert len(question["choices"]) == 4
    assert question["answers"] and all(0 <= n < 4 for n in question["answers"])
    sentence = question["prompt"].rsplit(": ", 1)[-1]
    assert "（　）" in sentence, f"Question {number} needs a particle blank"
    question["romaji"] = romaji_sentence(sentence)
    question["glossary"] = word_help(sentence)
    assert question["glossary"], f"Question {number} has no word help"
assert all(questions[i]["category"] != questions[i + 1]["category"]
           for i in range(99) if questions[i]["category"] in core
           and questions[i + 1]["category"] in core)
assert Counter(q["category"] if q["category"] in core else "earlier"
               for q in questions[:25]) == dict.fromkeys([*core, "earlier"], 5)
assert len({q["prompt"].rsplit(": ", 1)[-1] for q in questions}) == 100
assert len({q["answers"][0] for q in questions[:25]}) == 4

# Keep Japanese learner-facing text free of kanji, as requested.
for question in questions:
    for value in [question["prompt"], *question["choices"]]:
        assert not any("\u3400" <= char <= "\u9fff" for char in value), value

template = TEMPLATE.read_text(encoding="utf-8")
assert "/*PARTICLE_QUIZ_DATA*/" in template and "/*PARTICLE_QUIZ_APP*/" in template
page = template.replace("/*PARTICLE_QUIZ_DATA*/", json.dumps(questions, ensure_ascii=False, separators=(",", ":")))
page = page.replace("/*PARTICLE_QUIZ_APP*/", APP.read_text(encoding="utf-8"))
assert not re.search(r"[\u3400-\u9fff]", page), "Quiz page should contain no kanji"
(ROOT / "particle-quiz.html").write_text(page, encoding="utf-8", newline="\n")
print(f"Built {len(questions)} questions in {ROOT / 'particle-quiz.html'}")
