"""Build the self-contained kana-only 100-question particle quiz."""
import json
from collections import Counter
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = Path(__file__).with_name("particle_quiz_template.html")

PARTICLE_OPTIONS = {
    "を": ["を", "で", "に", "へ"],
    "に": ["に", "を", "で", "へ"],
    "で": ["で", "に", "を", "へ"],
    "へ": ["へ", "に", "で", "を"],
}


def make_particle(category, prompt, why, ordinal, accepted=None):
    choices = PARTICLE_OPTIONS[category][:]
    shift = ordinal % len(choices)
    choices = choices[shift:] + choices[:shift]
    answer = choices.index(category)
    good = [answer]
    if accepted:
        good = [i for i, value in enumerate(choices) if value in accepted]
    return {"category": category, "kind": "particle", "prompt": prompt,
            "choices": choices, "answers": good, "why": why}


def make_review(category, prompt, choices, answer, why):
    return {"category": category, "kind": "review", "prompt": prompt,
            "choices": choices, "answers": [answer], "why": why}


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

object_review = [
    ("You point to an unfamiliar thing and ask “What is this?” Choose the natural question.", ["これは なんですか。", "これは どこですか。", "これは だれですか。", "これは どうですか。"], 0, "なん asks “what.” どこ is “where,” だれ is “who,” and どう is “how.”"),
    ("You want to know who owns a book. Choose the question “Whose book is this?”", ["これは だれの ほんですか。", "これは どの ほんですか。", "これは だれは ほんですか。", "これは どこで ほんですか。"], 0, "だれの means “whose”; の connects the owner with the noun."),
    ("Ask “Which book?” Choose the phrase that can go before ですか.", ["どの ほん", "どれ ほん", "なんの ほん", "だれ ほん"], 0, "どの comes before a noun. どれ stands alone: どれですか。"),
    ("A friend asks whether that is your book. Choose the natural answer “Yes, it is my book.”", ["はい、わたしの ほんです。", "はい、わたしは ほんです。", "はい、わたしも ほんですか。", "はい、わたしじゃない ほんです。"], 0, "Noun の noun shows possession: わたしの ほん, “my book.”"),
    ("Ask “How much is this book?” Choose the natural question.", ["この ほんは いくらですか。", "この ほんは なんですか。", "この ほんは だれですか。", "この ほんは どこですか。"], 0, "いくら asks the price: “how much?”"),
]
for prompt, choices, answer, why in object_review:
    questions.append(make_review("を", prompt, choices, answer, why))

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
    8: ("Ask where someone is going: どこ（　）いきますか。", "どこ asks for the destination; both に and へ are natural.", ["に", "へ"]),
    11: ("Choose a destination particle: としょかん（　）きます。", "としょかん is where the person is coming to; に and へ both work.", ["に", "へ"]),
    13: ("Choose a destination particle: どようびに きっさてん（　）いきます。", "きっさてん is the destination. Both に and へ can mark it.", ["に", "へ"]),
    16: ("Choose a destination particle: うち（　）かえります。", "うち is the destination of returning home; either に or へ is natural.", ["に", "へ"]),
    18: ("Ask where the teacher is going: せんせいは どこ（　）いきますか。", "どこ asks for a destination; both に and へ can mark it.", ["に", "へ"]),
}
for n, (prompt, why) in enumerate(times):
    if n in ni_destinations:
        prompt, why, accepted = ni_destinations[n]
        questions.append(make_particle("に", prompt, why, n, accepted))
    else:
        questions.append(make_particle("に", prompt, why, n))

ni_review = [
    ("Choose the right question word: “Where is the library?”", ["としょかんは どこですか。", "としょかんは だれですか。", "としょかんは なんですか。", "としょかんは いくらですか。"], 0, "どこ asks “where.” A は B です question puts the topic before は."),
    ("Choose the correct reply: “Are you a student?” — “No, I am not a student.”", ["いいえ、がくせいじゃないです。", "いいえ、がくせいです。", "いいえ、がくせいもです。", "いいえ、がくせいのです。"], 0, "A noun negative in this lesson is noun + じゃないです."),
    ("Choose the natural sentence meaning “That is also a book.”", ["それも ほんです。", "それの ほんです。", "それを ほんです。", "それで ほんです。"], 0, "も can replace は to mean “also.”"),
    ("You see a person over there and ask “Who is that person?” Choose the natural sentence.", ["あのひとは だれですか。", "あのひとは どれですか。", "あのひとは いくらですか。", "あのひとは なんじですか。"], 0, "だれ asks “who”; あのひと means “that person over there.”"),
    ("A friend asks if the item is a watch. Choose the natural “No, it is not a watch.”", ["いいえ、とけいじゃないです。", "いいえ、とけいですか。", "いいえ、とけいのです。", "いいえ、とけいもです。"], 0, "じゃないです makes the noun predicate negative."),
]
for prompt, choices, answer, why in ni_review:
    questions.append(make_review("に", prompt, choices, answer, why))

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

de_review = [
    ("Choose the demonstrative for a book beside the listener: “That book.”", ["その ほん", "この ほん", "あの ほん", "どれ ほん"], 0, "その is used for something near the person you are speaking to; どの comes before a noun, but どれ stands alone."),
    ("Choose the correct question meaning “Which one is it?”", ["どれですか。", "どのですか。", "だれですか。", "どこですか。"], 0, "どれ means “which one” and stands by itself. Use どの before a noun."),
    ("Choose the natural sentence meaning “This is not a notebook.”", ["これは ノートじゃないです。", "これは ノートですか。", "これは ノートもです。", "これは ノートのです。"], 0, "じゃないです makes a noun predicate negative."),
    ("You are at a cafe. Ask “How is the coffee?” Choose the question with “how.”", ["コーヒーは どうですか。", "コーヒーは どこですか。", "コーヒーは だれですか。", "コーヒーは なんじですか。"], 0, "どう asks “how.”"),
    ("Choose the natural way to get agreement: “This is a nice book, isn't it?”", ["いい ほんですね。", "いい ほんですよか。", "いい ほんのです。", "いい ほんじゃないですか。"], 0, "ね can invite agreement or make a friendly comment."),
]
for prompt, choices, answer, why in de_review:
    questions.append(make_review("で", prompt, choices, answer, why))

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

he_review = [
    ("Choose the correct demonstrative for a book near you: “This book.”", ["この ほん", "その ほん", "あの ほん", "どれ ほん"], 0, "この comes before a nearby noun. どれ stands alone; どの comes before a noun when asking which."),
    ("Choose the natural question “Where is the station?”", ["えきは どこですか。", "えきは だれですか。", "えきは いくらですか。", "えきは なんですか。"], 0, "どこ asks where. The pattern is topic + は + place + ですか."),
    ("Choose the natural sentence meaning “That one over there is also a book.”", ["あれも ほんです。", "あれの ほんです。", "あれを ほんです。", "あれへ ほんです。"], 0, "あれ points to something away from both speakers; も means “also.”"),
    ("Choose the correct question word: “How is Japanese class?”", ["にほんごの クラスは どうですか。", "にほんごの クラスは どこですか。", "にほんごの クラスは だれですか。", "にほんごの クラスは どれですか。"], 0, "どう asks “how”; の connects にほんご with クラス."),
    ("Choose the natural sentence meaning “This is my notebook.”", ["これは わたしの ノートです。", "これは わたしを ノートです。", "これは わたしで ノートです。", "これは わたしへ ノートです。"], 0, "Noun + の + noun shows possession: わたしの ノート, “my notebook.”"),
]
for prompt, choices, answer, why in he_review:
    questions.append(make_review("へ", prompt, choices, answer, why))

assert len(questions) == 100, f"Expected 100 questions, got {len(questions)}"
assert Counter(q["category"] for q in questions) == {"を": 25, "に": 25, "で": 25, "へ": 25}
for number, question in enumerate(questions, 1):
    question["id"] = number
    assert len(question["choices"]) == 4
    assert question["answers"] and all(0 <= n < 4 for n in question["answers"])

# Keep Japanese learner-facing text free of kanji, as requested.
for question in questions:
    for value in [question["prompt"], *question["choices"]]:
        assert not any("\u3400" <= char <= "\u9fff" for char in value), value

template = TEMPLATE.read_text(encoding="utf-8")
page = template.replace("/*PARTICLE_QUIZ_DATA*/", json.dumps(questions, ensure_ascii=False, separators=(",", ":")))
if page == template:
    raise RuntimeError("Quiz data placeholder was not found")
assert not re.search(r"[\u3400-\u9fff]", page), "Quiz page should contain no kanji"
(ROOT / "particle-quiz.html").write_text(page, encoding="utf-8", newline="\n")
print(f"Built {len(questions)} questions in {ROOT / 'particle-quiz.html'}")
