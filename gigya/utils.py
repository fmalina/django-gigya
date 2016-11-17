from django.forms.widgets import TextInput


class BootstrapFormMixin(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, TextInput):
                widget_classes = field.widget.attrs.get('class', '').split()
                new_class = 'form-control'
                if new_class not in widget_classes:
                    widget_classes.append(new_class)
                field.widget.attrs['class'] = ' '.join(widget_classes)

