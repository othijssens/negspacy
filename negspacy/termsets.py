"""
Default termsets for various languages
"""

LANGUAGES = dict()

# Dutch termset dictionary
nl = dict()
nl_clinical = dict()

nl_pseudo = [
    "probleemloos",
    "zonder probleem",
    "zonder moeilijkheid",
    "geen verandering",
    "geen duidelijke verandering",
    "geen evidente verandering",
    "geen significante verandering",
    "geen significante stijging",
    "geen stijging",
    "niet alleen",
    "niet noodzakelijk",
    "niet zeker of",
    "niet zeker dat",
    "niet uitsluiten"
]

nl_pseudo_clinical = nl_pseudo + [
    "geen verbetering",
    "geen verhoging",
    "geen afwijking",
    "geen afwijkingen",
    "geen oorzaak",
    "geen evidente oorzaak",
    "niet verdween"
]

nl_preceding = [
    "afwezigheid van",
    "uitgesloten van",
    "vrij van",
    "geen",
    "geen teken van",
    "geen bewijs van",
    "geen verder bewijs",
    "geen enkel bewijs",
    "geen aanwijzing van",
    "geen aanwijzing voor",
    "zonder",
    "zonder bewijs",
    "niet",
    "niets",
    "noch",
    "nooit",
    "negatief"   ,
    "ontkent"
]

nl_preceding_clinical = nl_preceding + [
    "geen beeld van",
    "negatief voor",
    "atypische symptomen"
]

nl_following = [
    "afwezig",
    "geweigerd",
    "niet aanwezig",
    "niet aanweisbaar",
    "niet vastgesteld",
    "niet van toepassing",
    "niet het geval",
    "niet bekend",
    "geldt niet",
    "worden uitgesloten",
    "zijn uitgesloten",
    "is uitgesloten",
    "werd uitgesloten",
    "onwaarschijnlijk",
    "twijfelachtig"
]

nl_following_clinical = nl_following + [
    "is negatief",
    "vrij"  # Needs decompounding, e.g. tumorvrij
]

nl_termination = [
    "hoewel",
    "losstaand van",
    "onafhankelijk van",
    "met uitzondering van",
    "behalve",
    "maar",
    "echter",
    "niettemin",
    "desalniettemin"
    "ondanks",
    "nog wel"
]

nl_termination_clinical = nl_termination + [
    "als oorzaak van",
    "als de oorzaak van",
    "als reden voor",
    "als redenen voor",
    "als de reden van",
    "als een reden voor",
    "als bijwerking van",
    "als trigger voor",
    "als gevolg van",
    "omwille van",
    "als secundaire oorzaak van",
    "als tweede oorzaak van",
    "als tweede reden van",
    "als bron voor",
    "als een bron van",
    "als ziekteoorzaak",
    "als etiologie van",
    "als oorsprong voor"
]

nl["pseudo_negations"] = nl_pseudo
nl_clinical["pseudo_negations"] = nl_pseudo_clinical

nl["preceding_negations"] = nl_preceding
nl_clinical["preceding_negations"] = nl_preceding_clinical

nl["following_negations"] = nl_following
nl_clinical["following_negations"] = nl_following_clinical

nl["termination"] = nl_termination
nl_clinical["termination"] = nl_termination_clinical

LANGUAGES["nl"] = nl
LANGUAGES["nl_clinical"] = nl_clinical



# english termset dictionary
en = dict()
pseudo = [
    "no further",
    "not able to be",
    "not certain if",
    "not certain whether",
    "not necessarily",
    "without any further",
    "without difficulty",
    "without further",
    "might not",
    "not only",
    "no increase",
    "no significant change",
    "no change",
    "no definite change",
    "not extend",
    "not cause",
    "not certain if",
    "not certain whether",
]
en["pseudo_negations"] = pseudo

preceding = [
    "absence of",
    "declined",
    "denied",
    "denies",
    "denying",
    "no sign of",
    "no signs of",
    "not",
    "not demonstrate",
    "symptoms atypical",
    "doubt",
    "negative for",
    "no",
    "versus",
    "without",
    "doesn't",
    "doesnt",
    "don't",
    "dont",
    "didn't",
    "didnt",
    "wasn't",
    "wasnt",
    "weren't",
    "werent",
    "isn't",
    "isnt",
    "aren't",
    "arent",
    "cannot",
    "can't",
    "cant",
    "couldn't",
    "couldnt",
    "never",
]
en["preceding_negations"] = preceding

following = [
    "declined",
    "unlikely",
    "was not",
    "were not",
    "wasn't",
    "wasnt",
    "weren't",
    "werent",
]
en["following_negations"] = following

termination = [
    "although",
    "apart from",
    "as there are",
    "aside from",
    "but",
    "except",
    "however",
    "involving",
    "nevertheless",
    "still",
    "though",
    "which",
    "yet",
    "still",
]
en["termination"] = termination

LANGUAGES["en"] = en

# en_clinical builds upon en
en_clinical = dict()
pseudo_clinical = pseudo + [
    "gram negative",
    "not rule out",
    "not ruled out",
    "not been ruled out",
    "not drain",
    "no suspicious change",
    "no interval change",
    "no significant interval change",
]
en_clinical["pseudo_negations"] = pseudo_clinical

preceding_clinical = preceding + [
    "patient was not",
    "without indication of",
    "without sign of",
    "without signs of",
    "without any reactions or signs of",
    "no complaints of",
    "no evidence of",
    "no cause of",
    "evaluate for",
    "fails to reveal",
    "free of",
    "never developed",
    "never had",
    "did not exhibit",
    "rules out",
    "rule out",
    "rule him out",
    "rule her out",
    "rule patient out",
    "rule the patient out",
    "ruled out",
    "ruled him out" "ruled her out",
    "ruled patient out",
    "ruled the patient out",
    "r/o",
    "ro",
]
en_clinical["preceding_negations"] = preceding_clinical

following_clinical = following + ["was ruled out", "were ruled out", "free"]
en_clinical["following_negations"] = following_clinical

termination_clinical = termination + [
    "cause for",
    "cause of",
    "causes for",
    "causes of",
    "etiology for",
    "etiology of",
    "origin for",
    "origin of",
    "origins for",
    "origins of",
    "other possibilities of",
    "reason for",
    "reason of",
    "reasons for",
    "reasons of",
    "secondary to",
    "source for",
    "source of",
    "sources for",
    "sources of",
    "trigger event for",
]
en_clinical["termination"] = termination_clinical
LANGUAGES["en_clinical"] = en_clinical

en_clinical_sensitive = dict()

preceding_clinical_sensitive = preceding_clinical + [
    "concern for",
    "supposed",
    "which causes",
    "leads to",
    "h/o",
    "history of",
    "instead of",
    "if you experience",
    "if you get",
    "teaching the patient",
    "taught the patient",
    "teach the patient",
    "educated the patient",
    "educate the patient",
    "educating the patient",
    "monitored for",
    "monitor for",
    "test for",
    "tested for",
]
en_clinical_sensitive["pseudo_negations"] = pseudo_clinical
en_clinical_sensitive["preceding_negations"] = preceding_clinical_sensitive
en_clinical_sensitive["following_negations"] = following_clinical
en_clinical_sensitive["termination"] = termination_clinical

LANGUAGES["en_clinical_sensitive"] = en_clinical_sensitive
