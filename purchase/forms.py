from django import forms
from django.forms import formset_factory
from .models import PurchaseItem, PurchaseBillDetails, PurchaseBill
from stock.models import Stock


class PurchaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supplier'].widget.attrs.update({'class': 'textinput form-control'})
        # self.fields['name'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '[a-zA-Z\s]{1,50}', 'title' : 'Alphabets and Spaces only', 'required': 'true'})
        # self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10', 'pattern' : '[0-9]{10}', 'title' : 'Numbers only', 'required': 'true'})
        # self.fields['email'].widget.attrs.update({'class': 'textinput form-control'})
        
    class Meta:
        model = PurchaseBill
        fields = ['supplier', 'buyer_name', 'report', 'report_no', 'report_date', 'po_no', 'lc', 'style_no', 'file_no', 'lot_no', 'fabric_color', 'fabric_detail', 'store_location', 'order_qty']
        widgets = {
            
            'buyer_name' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'report' : forms.Select(attrs = {'class' : 'textinput form-control'}),
            'report_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'report_date' : forms.TextInput(attrs = {'class' : 'textinput form-control', 'type': 'date'}),
            'po_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'lc' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'style_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'file_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'lot_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'order_qty' : forms.NumberInput(attrs = {'class' : 'textinput form-control'}),
            'fabric_color' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'fabric_detail' : forms.Textarea(attrs = {'class' : 'textinput form-control', 'rows'  : '4'}),
            'store_location' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
        }
        labels = {
            'company': 'Company',
            'buyer_name': 'Buyer Name',
            'report': 'Inv/DC',
            'report_no': 'Inv/DC No',
            'report_date': 'Inv/DC Date',
            'po_no': 'PO No',
            'lc': 'LC',
            'style_no': 'Style No',
            'file_no': 'File No',
            'lot_no': 'Lot No',
            'product_item': 'Product Name',
            'fabric_color': 'Fabric Color',
            'fabric_detail': 'Fabric Detail',
            'store_location': 'Location',
            'order_qty': 'Order Qty',
            'receive_qty': 'Receive Qty',
            'uom': 'UOM',
            'unit_price': 'Uprice',
        }



# form used to render a single stock item form
class PurchaseItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Stock.objects.filter(is_deleted=False)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'true'})
        self.fields['unit_price'].widget.attrs.update({'class': 'textinput form-control setprice price', 'min': '0', 'required': 'true'})
        self.fields['uom'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = PurchaseItem
        fields = ['stock', 'quantity', 'unit_price', 'uom']


# formset used to render multiple 'PurchaseItemForm'
PurchaseItemFormset = formset_factory(PurchaseItemForm, extra=1)

class PurchaseDetailsForm(forms.ModelForm):
    class Meta:
        model = PurchaseBillDetails
        fields = ['eway','veh', 'destination', 'po', 'cgst', 'sgst', 'igst', 'cess', 'tcs', 'total']