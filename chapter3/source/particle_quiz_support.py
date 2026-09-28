"""Kana readings and complete word help for the particle quiz sentences."""

import re


# Each entry is (part of speech, plain-English meaning). Include names,
# question words, and time words as well as every verb and noun in the quiz.
WORDS = {
    "あきさん": ("name", "Aki"),
    "あさ": ("time word", "morning"),
    "あさごはん": ("noun", "breakfast"),
    "あした": ("time word", "tomorrow"),
    "あそこ": ("place word", "over there"),
    "あのひと": ("noun", "that person over there"),
    "あれ": ("pointing word", "that one over there"),
    "いい": ("adjective", "good"),
    "いきます": ("verb", "go / will go"),
    "いくら": ("question word", "how much"),
    "うち": ("noun", "home"),
    "えいが": ("noun", "movie"),
    "えいご": ("noun", "English language"),
    "えき": ("noun", "station"),
    "おきます": ("verb", "get up / will get up"),
    "おんがく": ("noun", "music"),
    "かいます": ("verb", "buy / will buy"),
    "かえります": ("verb", "return / will return"),
    "かきます": ("verb", "write / will write"),
    "かばん": ("noun", "bag"),
    "かようび": ("time word", "Tuesday"),
    "がくせい": ("noun", "student"),
    "がっこう": ("noun", "school"),
    "ききます": ("verb", "listen to / will listen to"),
    "きっさてん": ("noun", "coffee shop"),
    "きます": ("verb", "come / will come"),
    "きょう": ("time word", "today"),
    "きょうと": ("place name", "Kyoto"),
    "きんようび": ("time word", "Friday"),
    "ぎんこう": ("noun", "bank"),
    "くじ": ("time word", "nine o'clock"),
    "けんさん": ("name", "Ken"),
    "げつようび": ("time word", "Monday"),
    "こうえん": ("noun", "park"),
    "ここ": ("place word", "here"),
    "この": ("pointing word", "this (before a noun)"),
    "これ": ("pointing word", "this one"),
    "ごご": ("time word", "p.m."),
    "ごぜん": ("time word", "a.m."),
    "さんじ": ("time word", "three o'clock"),
    "しちじ": ("time word", "seven o'clock"),
    "します": ("verb", "do / will do"),
    "しんぶん": ("noun", "newspaper"),
    "じゅういちじ": ("time word", "eleven o'clock"),
    "すいようび": ("time word", "Wednesday"),
    "せんせい": ("noun", "teacher"),
    "そこ": ("place word", "there, near the listener"),
    "その": ("pointing word", "that (before a noun)"),
    "たなかさん": ("name", "Tanaka"),
    "たべます": ("verb", "eat / will eat"),
    "たろうさん": ("name", "Taro"),
    "だいがく": ("noun", "university"),
    "だれ": ("question word", "who"),
    "でんわします": ("verb", "call by phone / will call"),
    "です": ("predicate", "am / is / are (polite)"),
    "テレビ": ("noun", "television"),
    "とうきょう": ("place name", "Tokyo"),
    "としょかん": ("noun", "library"),
    "ともだち": ("noun", "friend"),
    "どう": ("question word", "how"),
    "どこ": ("question word", "where"),
    "どの": ("question word", "which (before a noun)"),
    "どようび": ("time word", "Saturday"),
    "どれ": ("question word", "which one"),
    "なに": ("question word", "what"),
    "なまえ": ("noun", "name"),
    "なん": ("question word", "what"),
    "なんじ": ("question word", "what time"),
    "にちようび": ("time word", "Sunday"),
    "にほん": ("place name", "Japan"),
    "にほんご": ("noun", "Japanese language"),
    "ねます": ("verb", "sleep / will sleep"),
    "のみます": ("verb", "drink / will drink"),
    "ノート": ("noun", "notebook"),
    "はちじ": ("time word", "eight o'clock"),
    "はるかさん": ("name", "Haruka"),
    "パン": ("noun", "bread"),
    "へや": ("noun", "room"),
    "べんきょうします": ("verb", "study / will study"),
    "ほん": ("noun", "book"),
    "まいさん": ("name", "Mai"),
    "まいしゅう": ("time word", "every week"),
    "まいにち": ("time word", "every day"),
    "まいばん": ("time word", "every night"),
    "みず": ("noun", "water"),
    "みせ": ("noun", "shop / store"),
    "みます": ("verb", "see / watch"),
    "もくようび": ("time word", "Thursday"),
    "やさい": ("noun", "vegetables"),
    "ゆきさん": ("name", "Yuki"),
    "よみます": ("verb", "read / will read"),
    "らいしゅう": ("time word", "next week"),
    "わたし": ("pronoun", "I / me"),
    "クラス": ("noun", "class"),
    "コーヒー": ("noun", "coffee"),
    "サッカー": ("noun", "soccer"),
}

PARTICLES = set("をでにへはのもかねよ")
LONGEST_WORDS = sorted(WORDS, key=len, reverse=True)


def split_japanese(chunk):
    """Split a space-delimited kana chunk into known words and particles."""
    pieces = []
    while chunk:
        word = next((word for word in LONGEST_WORDS if chunk.startswith(word)), None)
        if word:
            pieces.append((word, "word"))
            chunk = chunk[len(word):]
        elif chunk[0] in PARTICLES:
            pieces.append((chunk[0], "particle"))
            chunk = chunk[1:]
        else:
            raise ValueError(f"Missing word gloss for {chunk!r}")
    return pieces


def word_help(sentence):
    seen = set()
    result = []
    for chunk in re.sub(r"[（　）。、]", " ", sentence).split():
        for word, kind in split_japanese(chunk):
            if kind == "word" and word not in seen:
                part_of_speech, meaning = WORDS[word]
                result.append([word, part_of_speech, meaning])
                seen.add(word)
    return result


BASE = dict(zip(
    "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん"
    "がぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ",
    "a i u e o ka ki ku ke ko sa shi su se so ta chi tsu te to na ni nu ne no ha hi fu he ho "
    "ma mi mu me mo ya yu yo ra ri ru re ro wa o n ga gi gu ge go za ji zu ze zo "
    "da ji zu de do ba bi bu be bo pa pi pu pe po".split(),
))
DIGRAPHS = dict(zip(
    "きゃ きゅ きょ しゃ しゅ しょ ちゃ ちゅ ちょ にゃ にゅ にょ ひゃ ひゅ ひょ "
    "みゃ みゅ みょ りゃ りゅ りょ ぎゃ ぎゅ ぎょ じゃ じゅ じょ びゃ びゅ びょ ぴゃ ぴゅ ぴょ".split(),
    "kya kyu kyo sha shu sho cha chu cho nya nyu nyo hya hyu hyo "
    "mya myu myo rya ryu ryo gya gyu gyo ja ju jo bya byu byo pya pyu pyo".split(),
))


def kana_to_romaji(word):
    # Map katakana to their hiragana equivalents before transliterating.
    word = "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in word)
    result = ""
    i = 0
    while i < len(word):
        char = word[i]
        if char == "っ":
            following = DIGRAPHS.get(word[i + 1:i + 3], BASE.get(word[i + 1], ""))
            result += "t" if following.startswith("ch") else following[:1]
            i += 1
        elif char == "ー":
            vowel = next((c for c in reversed(result) if c in "aeiou"), "")
            result += vowel
            i += 1
        elif word[i:i + 2] in DIGRAPHS:
            result += DIGRAPHS[word[i:i + 2]]
            i += 2
        elif char in BASE:
            result += BASE[char]
            i += 1
        else:
            raise ValueError(f"Missing romaji for {word!r}, character {char!r}")
    return result


def romaji_sentence(sentence):
    sentence = sentence.replace("（　）", " ___ ").replace("。", " . ").replace("、", " , ")
    result = []
    for chunk in sentence.split():
        if chunk in {"___", ".", ","}:
            result.append(chunk)
            continue
        for piece, kind in split_japanese(chunk):
            if kind == "particle" and piece in {"は", "へ", "を"}:
                result.append({"は": "wa", "へ": "e", "を": "o"}[piece])
            else:
                result.append(kana_to_romaji(piece))
    return " ".join(result).replace(" .", ".").replace(" ,", ",")
