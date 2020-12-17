"""
Forms for the shop coupon system
"""

from django import forms


class CouponApplyForm(forms.Form):
    code = forms.CharField()
