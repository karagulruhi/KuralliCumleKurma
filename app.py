from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import random
from difflib import SequenceMatcher


Builder.load_file("kuralli_cumle.kv")


class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)


class ModeScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)


with open("sentences.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    kolay_cumleler = [cumle.replace('kolay:', '')
                      for cumle in lines if cumle.startswith("kolay")]
    orta_cumleler = [cumle.replace('orta:', '')
                     for cumle in lines if cumle.startswith("orta")]
    zor_cumleler = [cumle.replace('zor:', '')
                    for cumle in lines if cumle.startswith("zor")]
    cok_zor_cumleler = [cumle.replace('çok zor:', '')
                        for cumle in lines if cumle.startswith("çok zor")]


class EasyScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def sendEasySentence(self):
        easySentences = kolay_cumleler

        easySentence = random.choice(easySentences)
        self.correctAnswer = easySentence  # dışarı çıkar
        easySentences.remove(easySentence)
        sentence = "/".join(random.sample(easySentence.split(),
                            len(easySentence.split())))
        self.ids.sentence_box.text = sentence
        self.ids.feedback.text = ''
        self.ids.answerId.text = ''
        self.ids.greenredbutton.background_color = (0.0, 0.0, 0.0, 0.0)

        if not easySentences:
            self.ids.forward.disabled = True

    def submit(self, answer):
        if self.ids.answerId.text:
            similarity = SequenceMatcher(
                None, self.correctAnswer, answer).ratio()
            similarity_percentage = similarity * 100
            similarity_percentage = self.e_similarity_percentage
            self.ids.feedback.text = f"{similarity_percentage:.2f}% Oranında doğru"
            if similarity_percentage <= 85:
                self.ids.greenredbutton.background_color = (1.0, 0.0, 0.0, 1.0)
                print("hey")
            else:
                self.ids.greenredbutton.background_color = (0.0, 1.0, 0.0, 1.0)

        else:
            pass
    


class SemiHardScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def sendSemiHardSentence(self):
        semiHardSentences = orta_cumleler
        semiHardSentence = random.choice(semiHardSentences)
        self.correctAnswer = semiHardSentence  # dışarı çıkar
        semiHardSentences.remove(semiHardSentence)
        sentence = "/".join(random.sample(semiHardSentence.split(),
                            len(semiHardSentence.split())))
        self.ids.feedback.text = ''
        self.ids.answerId.text = ''
        self.ids.greenredbutton.background_color = (0.0, 0.0, 0.0, 0.0)
        self.ids.sentence_box.text = sentence
        if not semiHardSentences:
            self.ids.forward.disabled = True

    def submit(self, answer):
        if self.ids.answerId.text:
            similarity = SequenceMatcher(
                None, self.correctAnswer, answer).ratio()
            similarity_percentage = similarity * 100
            self.ids.feedback.text = f"{similarity_percentage:.2f}% Oranında doğru"
            if similarity_percentage <= 85:
                self.ids.greenredbutton.background_color = (1.0, 0.0, 0.0, 1.0)
                print("hey")
            else:
                self.ids.greenredbutton.background_color = (0.0, 1.0, 0.0, 1.0)

        else:
            pass


class HardScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def sendHardSentence(self):

        hardSentences = zor_cumleler
        hardSentence = random.choice(hardSentences)
        self.correctAnswer = hardSentence  # dışarı çıkar
        hardSentences.remove(hardSentence)
        sentence = "/".join(random.sample(hardSentence.split(),
                            len(hardSentence.split())))
        self.ids.sentence_box.text = sentence
        self.ids.feedback.text = ''
        self.ids.answerId.text = ''
        self.ids.greenredbutton.background_color = (0.0, 0.0, 0.0, 0.0)

        if not hardSentences:
            self.ids.forward.disabled = True

    def submit(self, answer):
        if self.ids.answerId.text:
            similarity = SequenceMatcher(
                None, self.correctAnswer, answer).ratio()
            similarity_percentage = similarity * 100
            self.ids.feedback.text = f"{similarity_percentage:.2f}% Oranında doğru"
            if similarity_percentage <= 85:
                self.ids.greenredbutton.background_color = (1.0, 0.0, 0.0, 1.0)
                print("hey")
            else:
                self.ids.greenredbutton.background_color = (0.0, 1.0, 0.0, 1.0)

        else:
            pass


class VeryHardScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def sendVeryHardSentence(self):

        veryHardSentences = cok_zor_cumleler
        easySentence = random.choice(veryHardSentences)
        self.correctAnswer = easySentence  # dışarı çıkar
        veryHardSentences.remove(easySentence)
        sentence = "/".join(random.sample(easySentence.split(),
                            len(easySentence.split())))

        self.ids.sentence_box.text = sentence
        self.ids.feedback.text = ''
        self.ids.answerId.text = ''
        self.ids.greenredbutton.background_color = (0.0, 0.0, 0.0, 0.0)
        if not veryHardSentences:
            self.ids.forward.disabled = True

    def submit(self, answer):
        if self.ids.answerId.text:
            similarity = SequenceMatcher(
                None, self.correctAnswer, answer).ratio()
            similarity_percentage = similarity * 100
            self.ids.feedback.text = f"{similarity_percentage:.2f}% Oranında doğru"
            if similarity_percentage <= 85:
                self.ids.greenredbutton.background_color = (1.0, 0.0, 0.0, 1.0)
                
            else:
                self.ids.greenredbutton.background_color = (0.0, 1.0, 0.0, 1.0)
        else:
            pass
            

class KurallıCümle(App):
    def build(self):
        # Create the screen manager
        self.icon = 'icon.png'
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(ModeScreen(name='mode'))

        sm.add_widget(EasyScreen(name='easy'))
        sm.add_widget(SemiHardScreen(name='semiHard'))
        sm.add_widget(HardScreen(name='hard'))
        sm.add_widget(VeryHardScreen(name='veryHard'))
        return sm


if __name__ == "__main__":
    KurallıCümle().run()
