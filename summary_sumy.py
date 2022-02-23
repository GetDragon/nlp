import sumy
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer

#Plain text parsers since we are parsing through text
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

class SumyHelper:
    def ResumenLexRank(self, parser, percent):
        sumLexRank=LexRankSummarizer()
        my_summary=sumLexRank(parser.document,percent)
        ret_val = "Resumen Algoritmo LexRank\n"
        for s in my_summary:
            ret_val += str(s) + "\n"
        
        return ret_val

    def ResumenLsa(self, parser, percent):
        sumLsa= LsaSummarizer()
        my_summary=sumLsa(parser.document,percent)
        ret_val = "\nResumen Algoritmo LSA\n"
        for s in my_summary:
            ret_val += str(s) + "\n"
        
        return ret_val

    def ResumenLuhn(self, parser, percent):
        sumLuhn= LuhnSummarizer()
        my_summary=sumLuhn(parser.document,percent)
        ret_val = "\nResumen Algoritmo Luhn\n"
        for s in my_summary:
            ret_val += str(s) + "\n"
        
        return ret_val

    def Execute(self, text, p):
        filterLines = []
        lines = text.splitlines()
        for l in lines:
            if len(l) > 0:
                filterLines.append(l)

        percent = int(len(filterLines) * p / 100)

        parser=PlaintextParser.from_string(text,Tokenizer("spanish"))

        s = ""
        s+=self.ResumenLexRank(parser, percent)
        s+=self.ResumenLsa(parser, percent)
        s+=self.ResumenLuhn(parser, percent)

        return bytes(s, "utf-8")