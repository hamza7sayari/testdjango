import smtplib

from django.core.mail import BadHeaderError, send_mail, EmailMultiAlternatives, EmailMessage
from django.http import FileResponse
from rest_framework import viewsets, renderers, permissions
from rest_framework.decorators import action

from recruitments.candidates.models.candidacy import User, Candidate
from recruitments.candidates.serializers import CandidateSerializer
from recruitments.candidates.utils import Util
from recruitments.settings import EMAIL_HOST_USER


class CandidateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows candidate to be viewed or edited.
    """

    lookup_field = 'id'
    queryset = Candidate.objects.all().order_by('-first_name')
    serializer_class = CandidateSerializer

    permission_classes = (permissions.IsAuthenticated,)

    # permissions.IsAdminUser

    def perform_create(self, serializer, commit=False):
        email = serializer.validated_data.get('email')
        username = serializer.validated_data.get('username')
        email_body = f'Bonjour {username} Merci pour la validation de Votre candidature'
        data = {
            'email_body': email_body,
            'email_subject': 'validation by mail',
            'to_email': email
        }
        msg = EmailMessage(
            subject="Bienvenuttu !  candidattt",
            body=email_body,
            from_email=EMAIL_HOST_USER,
            to=[email, ])

        # msg.track_clicks = True
        serializer.validated_data['created_by'] = self.request.user

        try:
            subject = data['email_subject']
            message = data['email_body']
            recepient = data['to_email']
            send_mail(subject,
                      message, EMAIL_HOST_USER, [recepient], fail_silently=False)

            #add user self?req

            Util.send_email(data)
            serializer.validated_data['message'] = 'Mail Sent Success'
        except:
            serializer.validated_data['message'] = 'Invalid mail found'

        super(CandidateViewSet, self).perform_create(serializer)
