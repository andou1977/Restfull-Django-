from rest_framework import serializers

from Api.models import Institution, Faculter, Option, Expert, Utilisateur


class Utilisateurserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'


class Institutionserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'


class faculterserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faculter
        fields = '__all__'


class Optionserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'


class Expertserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Expert
        fields = '__all__'




