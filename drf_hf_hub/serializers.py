""" Serializers """

from rest_framework import serializers


# Create your serializers here.
class BaseSerializer(serializers.Serializer):
    """Serializer that provides model field for subclasses"""

    model = serializers.CharField(
        required=False,
        max_length=64,
        help_text="The model to use for inference. Can be a model ID hosted on the Hugging Face Hub or a URL to a deployed Inference Endpoint",
    )


class TextSerializer(BaseSerializer):
    """Serialize text input"""

    text = serializers.CharField(
        max_length=4096,
        help_text="Input text",
    )


class ChatCompletionSerializer(BaseSerializer):
    """Serialize chat completion input"""

    messages = serializers.JSONField(
        help_text="Messages represented as a JSON array, a list of dicts with role and content keys.",
    )


class QuestionAnsweringSerializer(TextSerializer):
    """Serializer question answering input"""

    question = serializers.CharField(
        max_length=256,
        help_text="Question text",
    )


class TranslationSerializer(TextSerializer):
    """Serializer translation input"""

    source = serializers.CharField(
        max_length=5,
        help_text="Source language like en_XX",
    )
    target = serializers.CharField(
        max_length=5,
        help_text="Target language like ar_XX",
    )


class PromptSerializer(BaseSerializer):
    """Serializer for tasks that requires a prompt"""

    prompt = serializers.CharField(
        max_length=256,
        help_text="Prompt",
    )


class SentenceSimilaritySerializer(BaseSerializer):
    """Serializer for sentence similarity input"""

    sentence = serializers.CharField(
        max_length=4096,
        help_text="Sentence",
    )
    sentences = serializers.JSONField(
        help_text="Other sentences, a list of strings.",
    )


class ZeroShotClassificationSerializer(TextSerializer):
    """Serializer for zero shot text classification"""

    # Remove the file field
    file = None
    labels = serializers.JSONField(
        help_text="Text classification labels, a list of strings.",
    )
    is_multi_label = serializers.BooleanField(
        default=False,
        help_text="Boolean that is set to True if classes can overlap.",
    )
