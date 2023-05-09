from posts.models import Comment, Follow, Group, Post, User
from rest_framework import generics, relations, serializers


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('author', 'post')
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    def validate(self, data):
        user = generics.get_object_or_404(
            User,
            username=data.get('following').username
        )
        follow = Follow.objects.filter(
            user=self.context.get('request').user,
            following=user
        ).exists()
        if user == self.context.get('request').user:
            raise serializers.ValidationError(
                'Вы не можете подписаться сам на себя!'
            )
        if follow:
            raise serializers.ValidationError(
                f'Вы уже подписаны на {user}!'
            )
        return data

    class Meta:
        fields = '__all__'
        model = Follow


class PostSerializer(serializers.ModelSerializer):
    author = relations.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Post
