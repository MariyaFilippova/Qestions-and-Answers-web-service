from django import forms


class QuestionsListForm(forms.Form):
    search_field = forms.CharField(max_length=225)


class QuestionCreateForm(forms.Form):
    title = forms.CharField(max_length=225)
    question = forms.CharField(max_length=3000, widget=forms.Textarea)


class AnswerCreateForm(forms.Form):
    answer = forms.CharField(max_length=3000, widget=forms.Textarea)
