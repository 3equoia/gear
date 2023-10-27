from django import forms

class Form(forms.Form):
	error_messages = {'required': '' , 'width':'35'}
	module = forms.FloatField(label='مقدار مدول را وارد کنید', error_messages=error_messages, required=True)
	teeth = forms.IntegerField(label='تعداد دندانه را وارد کنید', error_messages=error_messages, required=True)

