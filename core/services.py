from django.core.mail import send_mail, send_mass_mail


class EmailService:

    def welcome_email(email, name):
        message: f"""Welcome to Patronne, {name}"""

        send_mail(
            'Welcome to Patronne',
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False,
        )
        return

    def password_reset_email(email):
        message: f"""Here's the link to reset your password"""

        send_mail(
            'trying to reset your password',
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False,
        )
        return
