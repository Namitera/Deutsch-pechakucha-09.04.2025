from manim import *

class Pictures(Scene):
    def construct(self):

        #２０枚の写真２０秒
        pictures = [
            "pechakucha/f1",
            "pechakucha/f2",
            "pechakucha/f3",
            "pechakucha/f4",
            "pechakucha/f5",
            "pechakucha/f6",
            "pechakucha/f7",
            "pechakucha/f8",
            "pechakucha/f9",
            "pechakucha/f10",
            "pechakucha/f11",
            "pechakucha/f12",
            "pechakucha/f13",
            "pechakucha/f14",
            "pechakucha/f15",
            "pechakucha/f16",
            "pechakucha/f17",
            "pechakucha/f18",
            "pechakucha/f19",
            "pechakucha/f20"
        ]

        piccount = len(pictures)
        blackbox = Rectangle(color=BLACK,fill_opacity=1).scale(20)

        img1 = ImageMobject(pictures[0])
        img1.scale(4.5/ img1.get_top()[1])

        self.play(FadeIn(img1),run_time=1)
        self.wait(18)
        
        for i in range(piccount):
            phase1 = ImageMobject(pictures[i])
            phase1.scale(4.5/ phase1.get_top()[1])

            if i+1 < piccount:
                phase2 = ImageMobject(pictures[i+1])
                phase2.scale(4.5/ phase2.get_top()[1])

                self.play(*[FadeOut(mob)for mob in self.mobjects],run_time=0.5)
                self.play(FadeIn(phase2),run_time=0.5)
                self.wait(19)

            else:
                self.play(FadeIn(blackbox))