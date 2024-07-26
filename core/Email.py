from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def enviar_email_resumo_pedido(pedido, produtos, valorDoPedido):
    subject = f'Pedido #{pedido.codigo}'
    html_message = render_to_string('Email.html', {'pedido': pedido,
                                                   'produtos': produtos,
                                                   'total': valorDoPedido})
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL
    to = pedido.cliente.email
    email = EmailMultiAlternatives(subject, plain_message, from_email, [to])
    email.attach_alternative(html_message, 'text/html')
    email.send()
