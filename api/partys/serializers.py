from rest_framework import serializers

from apps.partys.models import Party
from apps.users.models import MyUser


class PartyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['name']


class PartyCreateSerializer(serializers.ModelSerializer):
    # 회식 생성 직렬화
    owner = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True
    )
    member = PartyMemberSerializer(
        source="party_set", many=True, read_only=True)

    class Meta:
        model = Party
        fields = [
            'owner',
            'title',
            'date',
            'member',
            'total',
            'count',
            'result'
        ]

    # def create(self, validated_data):
    #     people = validated_data.pop('people')
    #     instance = Party.objects.create(**validated_data)
    #     # instance = super().create(validated_data)
    #     for name in people:
    #         try:
    #             user = MyUser.objects.get(name=name)
    #             instance.member.add(user)
    #         except:
    #             pass
    #     return instance


class PartySerializer(serializers.ModelSerializer):
    # 회식 직렬화
    member = PartyMemberSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = Party
        fields = [
            'id',
            'title',
            'member',
            'total',
            'result',
        ]
