
class calc_passer_rating:
    # comp --> completions
    # att --> passing attempts
    def a(comp, att):
        a = ((comp / float(att)) - 0.3) * 5
        return a

    # yds --> passing yards
    # att --> passing attempts
    def b(yds, att):
        b = ((yds / float(att)) - 3) * .25
        return b

    # td --> touchdown passes
    # att --> passing attempts
    def c(td, att):
        c = (td / float(att)) * 20
        return c

    # int --> interceptions
    # att --> passing attempts
    def d(int, att):
        d = 2.375 - ((int / float(att)) * 25)
        return d

    def passer_rating(a, b, c, d):
        return ((a + b + c + d) / 6.0) * 100
