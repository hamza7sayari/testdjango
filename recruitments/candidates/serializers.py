from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ALL_FIELDS

# from recruitments.candidates.models.user import User
from recruitments.candidates.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)

    class Meta:
        model = Candidate
        fields = ALL_FIELDS