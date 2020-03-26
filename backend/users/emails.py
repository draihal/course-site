from djoser import email as djoser_email


class CustomActivationEmail(djoser_email.ActivationEmail):
    template_name = "users/email/activation.html"


class CustomConfirmationEmail(djoser_email.ConfirmationEmail):
    template_name = "users/email/confirmation.html"


class CustomPasswordResetEmail(djoser_email.PasswordResetEmail):
    template_name = "users/email/password_reset.html"


class CustomPasswordChangedConfirmationEmail(djoser_email.PasswordChangedConfirmationEmail):
    template_name = "users/email/password_changed_confirmation.html"


class CustomUsernameChangedConfirmationEmail(djoser_email.UsernameChangedConfirmationEmail):
    template_name = "users/email/username_changed_confirmation.html"


class CustomUsernameResetEmail(djoser_email.UsernameResetEmail):
    template_name = "users/email/username_reset.html"
