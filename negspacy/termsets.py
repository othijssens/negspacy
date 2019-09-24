"""
Default termsets for various languages
"""

LANGUAGES = dict()

#english termset dictionary
en = dict()
en['psuedo_negations'] = [
                "gram negative",
                "no further",
                "not able to be",
                "not certain if",
                "not certain whether",
                "not necessarily",
                "not rule out",
                "not ruled out",
                "not been ruled out",
                "without any further",
                "without difficulty",
                "without further",
            ]
en['preceding_negations'] = [
                "absence of",
                "declined",
                "denied",
                "denies",
                "denying",
                "did not exhibit",
                "no sign of",
                "no signs of",
                "not",
                "not demonstrate",
                "patient was not",
                "rules out",
                "doubt",
                "negative for",
                "no",
                "no cause of",
                "no complaints of",
                "no evidence of",
                "versus",
                "without",
                "without indication of",
                "without sign of",
                "without signs of",
                "ruled out",
            ]
en['following_negations'] = [
                "declined",
                "unlikely",
                "was ruled out",
                "were ruled out",
                "was not",
                "were not",
            ]
en['termination'] = [
                "although",
                "apart from",
                "as there are",
                "aside from",
                "but",
                "cause for",
                "cause of",
                "causes for",
                "causes of",
                "etiology for",
                "etiology of",
                "except",
                "however",
                "involving",
                "nevertheless",
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
                "still",
                "though",
                "trigger event for",
                "which",
                "yet",
            ]
LANGUAGES['en'] = en