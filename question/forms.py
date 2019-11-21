from django import forms


class QuestionsListForm(forms.Form):
    selected_item = forms.ChoiceField(choices=(('id', 'ID'), ('title', 'Name'), ('pub_date', 'Date')))


class QuestionCreateForm(forms.Form):
    title = forms.CharField(max_length=225)
    question = forms.CharField(max_length=3000, widget=forms.Textarea)


class AnswerCreateForm(forms.Form):
    answer = forms.CharField(max_length=3000, widget=forms.Textarea)
