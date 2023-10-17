"""A module providing the Latin alphabet as symbols in various styles.""" 

from pyreport.symbols import Symbol, SymbolCollection

__all__ = ["BlackBoardSymbols", "CalligraphicSymbols", "FrakturSymbols"]


class BlackBoardSymbols(SymbolCollection):
    """A collection containing the Latin alphabet as symbols in blackboard style.

    Attributes
    ----------
    AA : Symbol
        The symbol for the double-struck capital letter A.
    BB : Symbol
        The symbol for the double-struck capital letter B.
    CC : Symbol
        The symbol for the double-struck capital letter C.
    DD : Symbol
        The symbol for the double-struck capital letter D.
    EE : Symbol
        The symbol for the double-struck capital letter E.
    FF : Symbol
        The symbol for the double-struck capital letter F.
    GG : Symbol
        The symbol for the double-struck capital letter G.
    HH : Symbol
        The symbol for the double-struck capital letter H.
    II : Symbol
        The symbol for the double-struck capital letter I.
    JJ : Symbol
        The symbol for the double-struck capital letter J.
    KK : Symbol
        The symbol for the double-struck capital letter K.
    LL : Symbol
        The symbol for the double-struck capital letter L.
    MM : Symbol
        The symbol for the double-struck capital letter M.
    NN : Symbol
        The symbol for the double-struck capital letter N.
    OO : Symbol
        The symbol for the double-struck capital letter O.
    PP : Symbol
        The symbol for the double-struck capital letter P.
    QQ : Symbol
        The symbol for the double-struck capital letter Q.
    RR : Symbol
        The symbol for the double-struck capital letter R.
    SS : Symbol
        The symbol for the double-struck capital letter S.
    TT : Symbol
        The symbol for the double-struck capital letter T.
    UU : Symbol
        The symbol for the double-struck capital letter U.
    VV : Symbol
        The symbol for the double-struck capital letter V.
    WW : Symbol
        The symbol for the double-struck capital letter W.
    XX : Symbol
        The symbol for the double-struck capital letter X.
    YY : Symbol
        The symbol for the double-struck capital letter Y.
    ZZ : Symbol
        The symbol for the double-struck capital letter Z.
    """

    AA = Symbol("AA", r"\mathbb{A}", "\u1D538")
    BB = Symbol("BB", r"\mathbb{B}", "\u1D539")
    CC = Symbol("CC", r"\mathbb{C}", "\u2102")
    DD = Symbol("DD", r"\mathbb{D}", "\u1D53B")
    EE = Symbol("EE", r"\mathbb{E}", "\u1D53C")
    FF = Symbol("FF", r"\mathbb{F}", "\u1D53D")
    GG = Symbol("GG", r"\mathbb{G}", "\u1D53E")
    HH = Symbol("HH", r"\mathbb{H}", "\u210D")
    II = Symbol("II", r"\mathbb{I}", "\u1D540")
    JJ = Symbol("JJ", r"\mathbb{J}", "\u1D541")
    KK = Symbol("KK", r"\mathbb{K}", "\u1D542")
    LL = Symbol("LL", r"\mathbb{L}", "\u1D543")
    MM = Symbol("MM", r"\mathbb{M}", "\u1D544")
    NN = Symbol("NN", r"\mathbb{N}", "\u2115")
    OO = Symbol("OO", r"\mathbb{O}", "\u1D546")
    PP = Symbol("PP", r"\mathbb{P}", "\u2119")
    QQ = Symbol("QQ", r"\mathbb{Q}", "\u211A")
    RR = Symbol("RR", r"\mathbb{R}", "\u211D")
    SS = Symbol("SS", r"\mathbb{S}", "\u1D54A")
    TT = Symbol("TT", r"\mathbb{T}", "\u1D54B")
    UU = Symbol("UU", r"\mathbb{U}", "\u1D54C")
    VV = Symbol("VV", r"\mathbb{V}", "\u1D54D")
    WW = Symbol("WW", r"\mathbb{W}", "\u1D54E")
    XX = Symbol("XX", r"\mathbb{X}", "\u1D54F")
    YY = Symbol("YY", r"\mathbb{Y}", "\u1D550")
    ZZ = Symbol("ZZ", r"\mathbb{Z}", "\u2124")

    @classmethod
    def get_symbols(cls):
        return super(BlackBoardSymbols, cls).get_symbols()

    @classmethod
    def list_symbols(cls):
        super(BlackBoardSymbols, cls).list_symbols()


class CalligraphicSymbols(SymbolCollection):
    """A collection containing the Latin alphabet as symbols in calligraphic style.

    Attributes
    ----------
    calA : Symbol
        The symbol for the calligraphic capital letter A.
    calB : Symbol
        The symbol for the calligraphic capital letter B.
    calC : Symbol
        The symbol for the calligraphic capital letter C.
    calD : Symbol
        The symbol for the calligraphic capital letter D.
    calE : Symbol
        The symbol for the calligraphic capital letter E.
    calF : Symbol
        The symbol for the calligraphic capital letter F.
    calG : Symbol
        The symbol for the calligraphic capital letter G.
    calH : Symbol
        The symbol for the calligraphic capital letter H.
    calI : Symbol
        The symbol for the calligraphic capital letter I.
    calJ : Symbol
        The symbol for the calligraphic capital letter J.
    calK : Symbol
        The symbol for the calligraphic capital letter K.
    calL : Symbol
        The symbol for the calligraphic capital letter L.
    calM : Symbol
        The symbol for the calligraphic capital letter M.
    calN : Symbol
        The symbol for the calligraphic capital letter N.
    calO : Symbol
        The symbol for the calligraphic capital letter O.
    calP : Symbol
        The symbol for the calligraphic capital letter P.
    calQ : Symbol
        The symbol for the calligraphic capital letter Q.
    calR : Symbol
        The symbol for the calligraphic capital letter R.
    calS : Symbol
        The symbol for the calligraphic capital letter S.
    calT : Symbol
        The symbol for the calligraphic capital letter T.
    calU : Symbol
        The symbol for the calligraphic capital letter U.
    calV : Symbol
        The symbol for the calligraphic capital letter V.
    calW : Symbol
        The symbol for the calligraphic capital letter W.
    calX : Symbol
        The symbol for the calligraphic capital letter X.
    calY : Symbol
        The symbol for the calligraphic capital letter Y.
    calZ : Symbol
        The symbol for the calligraphic capital letter Z.
    """

    calA = Symbol("calA", r"\mathcal{A}", "\u1D49C")
    calB = Symbol("calB", r"\mathcal{B}", "\u212C")
    calC = Symbol("calC", r"\mathcal{C}", "\u1D49E")
    calD = Symbol("calD", r"\mathcal{D}", "\u1D49F")
    calE = Symbol("calE", r"\mathcal{E}", "\u2130")
    calF = Symbol("calF", r"\mathcal{F}", "\u2131")
    calG = Symbol("calG", r"\mathcal{G}", "\u1D4A2")
    calH = Symbol("calH", r"\mathcal{H}", "\u210B")
    calI = Symbol("calI", r"\mathcal{I}", "\u2110")
    calJ = Symbol("calJ", r"\mathcal{J}", "\u1D4A5")
    calK = Symbol("calK", r"\mathcal{K}", "\u1D4A6")
    calL = Symbol("calL", r"\mathcal{L}", "\u2112")
    calM = Symbol("calM", r"\mathcal{M}", "\u2133")
    calN = Symbol("calN", r"\mathcal{N}", "\u1D4A9")
    calO = Symbol("calO", r"\mathcal{O}", "\u1D4AA")
    calP = Symbol("calP", r"\mathcal{P}", "\u1D4AB")
    calQ = Symbol("calQ", r"\mathcal{Q}", "\u1D4AC")
    calR = Symbol("calR", r"\mathcal{R}", "\u211B")
    calS = Symbol("calS", r"\mathcal{S}", "\u1D4AE")
    calT = Symbol("calT", r"\mathcal{T}", "\u1D4AF")
    calU = Symbol("calU", r"\mathcal{U}", "\u1D4B0")
    calV = Symbol("calV", r"\mathcal{V}", "\u1D4B1")
    calW = Symbol("calW", r"\mathcal{W}", "\u1D4B2")
    calX = Symbol("calX", r"\mathcal{X}", "\u1D4B3")
    calY = Symbol("calY", r"\mathcal{Y}", "\u1D4B4")
    calZ = Symbol("calZ", r"\mathcal{Z}", "\u1D4B5")

    @classmethod
    def get_symbols(cls):
        return super(CalligraphicSymbols, cls).get_symbols()

    @classmethod
    def list_symbols(cls):
        super(CalligraphicSymbols, cls).list_symbols()


class FrakturSymbols(SymbolCollection):
    """A collection containing the Latin alphabet as symbols in fraktur style.

    Attributes
    ----------
    frakA : Symbol
        The symbol for the fraktur capital letter A.
    frakB : Symbol
        The symbol for the fraktur capital letter B.
    frakC : Symbol
        The symbol for the fraktur capital letter C.
    frakD : Symbol
        The symbol for the fraktur capital letter D.
    frakE : Symbol
        The symbol for the fraktur capital letter E.
    frakF : Symbol
        The symbol for the fraktur capital letter F.
    frakG : Symbol
        The symbol for the fraktur capital letter G.
    frakH : Symbol
        The symbol for the fraktur capital letter H.
    frakI : Symbol
        The symbol for the fraktur capital letter I.
    frakJ : Symbol
        The symbol for the fraktur capital letter J.
    frakK : Symbol
        The symbol for the fraktur capital letter K.
    frakL : Symbol
        The symbol for the fraktur capital letter L.
    frakM : Symbol
        The symbol for the fraktur capital letter M.
    frakN : Symbol
        The symbol for the fraktur capital letter N.
    frakO : Symbol
        The symbol for the fraktur capital letter O.
    frakP : Symbol
        The symbol for the fraktur capital letter P.
    frakQ : Symbol
        The symbol for the fraktur capital letter Q.
    frakR : Symbol
        The symbol for the fraktur capital letter R.
    frakS : Symbol
        The symbol for the fraktur capital letter S.
    frakT : Symbol
        The symbol for the fraktur capital letter T.
    frakU : Symbol
        The symbol for the fraktur capital letter U.
    frakV : Symbol
        The symbol for the fraktur capital letter V.
    frakW : Symbol
        The symbol for the fraktur capital letter W.
    frakX : Symbol
        The symbol for the fraktur capital letter X.
    frakY : Symbol
        The symbol for the fraktur capital letter Y.
    frakZ : Symbol
        The symbol for the fraktur capital letter Z.
    """
    
    frakA = Symbol("frakA", r"\mathfrak{A}", "\u1D56C")
    frakB = Symbol("frakB", r"\mathfrak{B}", "\u1D56D")
    frakC = Symbol("frakC", r"\mathfrak{C}", "\u1D56E")
    frakD = Symbol("frakD", r"\mathfrak{D}", "\u1D56F")
    frakE = Symbol("frakE", r"\mathfrak{E}", "\u1D570")
    frakF = Symbol("frakF", r"\mathfrak{F}", "\u1D571")
    frakG = Symbol("frakG", r"\mathfrak{G}", "\u1D572")
    frakH = Symbol("frakH", r"\mathfrak{H}", "\u1D573")
    frakI = Symbol("frakI", r"\mathfrak{I}", "\u1D574")
    frakJ = Symbol("frakJ", r"\mathfrak{J}", "\u1D575")
    frakK = Symbol("frakK", r"\mathfrak{K}", "\u1D576")
    frakL = Symbol("frakL", r"\mathfrak{L}", "\u1D577")
    frakM = Symbol("frakM", r"\mathfrak{M}", "\u1D578")
    frakN = Symbol("frakN", r"\mathfrak{N}", "\u1D579")
    frakO = Symbol("frakO", r"\mathfrak{O}", "\u1D57A")
    frakP = Symbol("frakP", r"\mathfrak{P}", "\u1D57B")
    frakQ = Symbol("frakQ", r"\mathfrak{Q}", "\u1D57C")
    frakR = Symbol("frakR", r"\mathfrak{R}", "\u1D57D")
    frakS = Symbol("frakS", r"\mathfrak{S}", "\u1D57E")
    frakT = Symbol("frakT", r"\mathfrak{T}", "\u1D57F")
    frakU = Symbol("frakU", r"\mathfrak{U}", "\u1D580")
    frakV = Symbol("frakV", r"\mathfrak{V}", "\u1D581")
    frakW = Symbol("frakW", r"\mathfrak{W}", "\u1D582")
    frakX = Symbol("frakX", r"\mathfrak{X}", "\u1D583")
    frakY = Symbol("frakY", r"\mathfrak{Y}", "\u1D584")
    frakZ = Symbol("frakZ", r"\mathfrak{Z}", "\u1D585")

    @classmethod
    def get_symbols(cls):
        return super(FrakturSymbols, cls).get_symbols()

    @classmethod
    def list_symbols(cls):
        super(FrakturSymbols, cls).list_symbols()
        