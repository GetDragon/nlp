import sumy
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer

#Plain text parsers since we are parsing through text
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

import os

class SumyHelper:
    def ResumenLexRank(self, parser, percent):
        sumLexRank=LexRankSummarizer()
        my_summary=sumLexRank(parser.document,percent)
        ret_val = ""
        for s in my_summary:
            ret_val += str(s) + os.linesep
        
        return ret_val

    def ResumenLsa(self, parser, percent):
        sumLsa= LsaSummarizer()
        my_summary=sumLsa(parser.document,percent)
        ret_val = ""
        for s in my_summary:
            ret_val += str(s) + os.linesep
        
        return ret_val

    def ResumenLuhn(self, parser, percent):
        sumLuhn= LuhnSummarizer()
        my_summary=sumLuhn(parser.document,percent)
        ret_val = ""
        for s in my_summary:
            ret_val += str(s) + os.linesep
        
        return ret_val

    def Execute(self, type, text, p):
        filterLines = []
        lines = text.splitlines()
        for l in lines:
            if len(l) > 0:
                filterLines.append(l)

        percent = int(len(filterLines) * p / 100)

        parser=PlaintextParser.from_string(text,Tokenizer("spanish"))

        s = ""
        if type == "LexRank":
            s=self.ResumenLexRank(parser, percent)
        elif type == "Lsa":
            s=self.ResumenLsa(parser, percent)
        elif type == "Luhn":
            s=self.ResumenLuhn(parser, percent)

        return s