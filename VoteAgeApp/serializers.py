
from django.contrib.auth.models import User, Group
from django.core.files.base import ContentFile
from rest_framework import serializers
import re
import base64
import uuid
import imghdr
import models

class Base64ImageField(serializers.ImageField):
    """ Django-rest-framework field for base64 encoded image data. """
    def to_internal_value(self, base64_data):
        if isinstance(base64_data, basestring):
            # Strip data header and add missing padding
            base64_data = re.sub(r"^data\:.+base64\,(.+)$", r"\1", base64_data)
            missing_padding = 4 - len(base64_data) % 4
            if missing_padding:
                base64_data += b'='* missing_padding

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(base64_data)
            except TypeError:
                msg = "Please upload a valid image."
                raise serializers.ValidationError(msg)

            # Get the file name extension:
            extension = imghdr.what("file_name", decoded_file)
            if extension not in ("jpeg", "jpg", "png"):
                msg = "{0} is not a valid image type.".format(extension)
                raise serializers.ValidationError(msg)

            extension = "jpg" if extension == "jpeg" else extension
            file_name = ".".join([str(uuid.uuid4()), extension])
            data = ContentFile(decoded_file, name=file_name)

        return super(Base64ImageField, self).to_internal_value(data)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class VoteSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    class Meta:
        model = models.Vote
        fields = ('id', 'title', 'image', 'author', 'hasVoted', 'publishDate', 'expireDate','latitude', 'longitude', 'option')
        depth = 1

class OptionSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    class Meta:
        model = models.Option
        fields = ('voteID', 'title', 'image', 'menCount', 'womenCount')


