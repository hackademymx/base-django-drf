from decouple import config
from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings



class DefaultAccountAdapterCustom(DefaultAccountAdapter):

    def send_mail(self, template_prefix, email, context):
        context['activate_url'] = config('DOMAIN', default='http://localhost:8000') + config('VERIFY_ENDPOINT', default='/') + context['key']
        msg = self.render_mail(template_prefix, email, context)
        msg.send()
