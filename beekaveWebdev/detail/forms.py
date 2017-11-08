from django import forms

from reviewPage.models import reviewMovie,reviewGame,reviewTV


class movieReviewForm(forms.ModelForm):

    class Meta:
        model = reviewMovie
        fields = '__all__'

class gameReviewForm(forms.ModelForm):

    class Meta:
        model = reviewGame
        fields = '__all__'

class tvReviewForm(forms.ModelForm):

    class Meta:
        model = reviewTV
        fields = '__all__'
