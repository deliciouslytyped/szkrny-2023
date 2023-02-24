
# 20170517a Öt egymást követő számjegy legnagyobb összege
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20170517a

from infra import ProblemBase

from textwrap import dedent
from collections import deque

class Problem(ProblemBase):
    has_check = True
    s = dedent("""
                1090748135619415929462984244733782862448264161996232692431832786189721331849119295216264234525201987
                2239572917961570252731098708201771840636109797650775547990789062988421929895386098252280482051596968
                5161359163819677188654260932456012129055390188630101790025253579991720001007960002653583680090529780
                5880952350501630195475653911005312364560014847426035293551245843928918752768696279344088055617515694
                3499454066778251408149006161059202564385045780133264935658360472424073824428122451315177575191648992
                2636574372243227736807502762788304520650179276170094569916849725787968385173704999690096112051565505
                0115561271491492515342105748966629547032786321505730828430221664970324396138635251626409516168005427
                6234359963089216914461811874063953106654048857394348328774281674074953709935118687563599703901170218
                2361674945862096985700626361208270671540815706657513728102702231092756491027675916052087830463241104
                9364568754920967322982459184763427383790272448438018526977764941072715611580434690827459339991961414
                2427414105991174260605564837637563145276113626586283833686211579936380208785376755453367899156942344
                3395566631507008721353547025567031200413072549583450835743965382893607708097855057891296790735278005
                4935621561090795845172954115972927479877527738560008204118558930004777748727761853813510493840581861
                5986522116059603083564059418211897140378687262194814987276036536162988561748224130334854387853240247
                5141941718301228107820972930353737280457437209522870362277636394529086980625842235514850757103961938
                7449629866808188769662815778153079393179093143648340761738581819563002994422790754955061288818308430
                0796486932321791587659180355652161571154029921202761556078731079374774668415283629877086994501520312
                3186259420308569383894465706134623670423402682110295895495119708707654618662279629453645162075650935
                1018906023773821539532776208676978589731966330308893304665169436185078350641568336944530051437491311
                2988343672652385954049042734559287239495252271846174043678547546104743770197680255766058810380772707""").replace("\n", "")

    def simple_run(self):
        s = self.s
        return max([sum(map(int, s[i:i + 4 + 1])) for i in range(0, len(s) - 4)])

    def advanced_run(self):
        # "Használjuk a deque adatszerkezetet. Kérdés: hogyan tudnánk még a kódon optimalizálni? A sum(deque) hívásokat hogyan tudnánk kiiktatni? "
        d, s, m = deque("", 5), self.s, 0
        sum = 0
        for i in range(0, len(s)):
            v = int(s[i])
            if i > 4:
                old = d.popleft()
                sum -= old
            d.append(v)
            sum += v
            m = max(m, sum)
        return m



    def run(self):
        assert(self.simple_run() == self.advanced_run())
        return self.advanced_run()

if __name__ == "__main__":
    p = Problem()
    p.check()
