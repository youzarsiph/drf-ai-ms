""" Microservice API endpoints """

from pathlib import Path
from django.http import FileResponse
from huggingface_hub import InferenceClient
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.routers import APIRootView
from rest_framework.viewsets import GenericViewSet
from drf_hf_hub import serializers


# HF Inference Client
client = InferenceClient()


# Create your views here.
class TextViewSet(GenericViewSet):
    """API endpoints for working with text data"""

    serializer_class = serializers.TextSerializer

    def get_serializer_class(self) -> None:
        """Return different serializers for different actions"""

        match self.action:
            case "chat_completion":
                self.serializer_class = serializers.ChatCompletionSerializer

            case "question_answering":
                self.serializer_class = serializers.QuestionAnsweringSerializer

            case "sentence_similarity":
                self.serializer_class = serializers.SentenceSimilaritySerializer

            case "translation":
                self.serializer_class = serializers.TranslationSerializer

            case "text_generation":
                self.serializer_class = serializers.PromptSerializer

            case "text_to_image":
                self.serializer_class = serializers.PromptSerializer

            case "zero_shot_classification":
                self.serializer_class = serializers.ZeroShotClassificationSerializer

            case _:
                self.serializer_class = serializers.TextSerializer

        return super().get_serializer_class()

    @action(["post"], detail=False, url_path="chat-completion")
    def chat_completion(self, request: Request) -> Response:
        """A method for completing conversations using a specified language model."""

        # Serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "result": client.chat_completion(
                    messages=serializer.validated_data["messages"],
                    model=serializer.validated_data.get("model", None),
                )
            },
            status=status.HTTP_200_OK,
        )

    @action(["post"], detail=False, url_path="feature-extraction")
    def feature_extraction(self, request: Request) -> Response:
        """Generate embeddings for a given text."""

        # Serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "result": client.feature_extraction(
                    text=serializer.validated_data["text"],
                    model=serializer.validated_data.get("model", None),
                )
            },
            status=status.HTTP_200_OK,
        )

    @action(["post"], detail=False, url_path="fill-mask")
    def fill_mask(self, request: Request) -> Response:
        """Fill in a hole with a missing word (token to be precise)."""

        # Serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "result": client.fill_mask(
                    text=serializer.validated_data["text"],
                    model=serializer.validated_data.get("model", None),
                )
            },
            status=status.HTTP_200_OK,
        )

    @action(["post"], detail=False, url_path="question-answering")
    def question_answering(self, request: Request) -> Response:
        """Retrieve the answer to a question from a given text."""

        # Serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "answer": client.question_answering(
                    question=serializer.validated_data["question"],
                    context=serializer.validated_data["text"],
                    model=serializer.validated_data.get("model", None),
                )
            },
            status=status.HTTP_200_OK,
        )

    @action(["post"], detail=False, url_path="sentence-similarity")
    def sentence_similarity(self, request: Request) -> Response:
        """Compute the semantic similarity between a sentence and a list of other sentences by comparing their embeddings."""

        # Serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "result": client.sentence_similarity(
                    sentence=serializer.validated_data["sentence"],
                    other_sentences=serializer.validated_data["sentences"],
                    model=serializer.validated_data.get("model", None),
                )
            },
            status=status.HTTP_200_OK,
        )

    @action(["post"], detail=False)
    def summarization(self, request: Request) -> Response:
        """Generate a summary of a given text using a specified model."""

        # Serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "summary": client.summarization(
                    text=serializer.validated_data["text"],
                    model=serializer.validated_data.get("model", None),
                ).summary_text
            },
            status=status.HTTP_200_OK,
        )

    @action(["post"], detail=False, url_path="text-classification")
    def text_classification(self, request: Request) -> Response:
        """Perform text classification (e.g. sentiment-analysis) on the given text."""

        # Serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "result": client.text_classification(
                    text=serializer.validated_data["text"],
                    model=serializer.validated_data.get("model", None),
                )
            },
            status=status.HTTP_200_OK,
        )

    @action(["post"], detail=False, url_path="text-generation")
    def text_generation(self, request: Request) -> Response:
        """Given a prompt, generate the following text."""

        # Serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "result": client.text_generation(
                    prompt=serializer.validated_data["prompt"],
                    model=serializer.validated_data.get("model", None),
                )
            },
            status=status.HTTP_200_OK,
        )

    @action(["post"], detail=False, url_path="text-to-image")
    def text_to_image(self, request: Request) -> Response | FileResponse:
        """Generate an image based on a given text using a specified model."""

        # Serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        client.text_to_image(
            prompt=serializer.validated_data["prompt"],
            model=serializer.validated_data.get("model", None),
        ).save("image.png")

        return FileResponse(open("image.png", "rb"))

    @action(["post"], detail=False, url_path="text-to-speech")
    def text_to_speech(self, request: Request) -> Response | FileResponse:
        """Synthesize an audio of a voice pronouncing a given text."""

        # Serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        audio = client.text_to_speech(
            text=serializer.validated_data["text"],
            model=serializer.validated_data.get("model", None),
        )

        Path("audio.flac").write_bytes(audio)

        return FileResponse(open("audio.flac", "rb"))

    @action(["post"], detail=False, url_path="token-classification")
    def token_classification(self, request: Request) -> Response:
        """
        Perform token classification on the given text. Usually used for sentence parsing, either grammatical,
        or Named Entity Recognition (NER) to understand keywords contained within text.
        """

        # Serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "translation": client.token_classification(
                    text=serializer.validated_data["text"],
                    model=serializer.validated_data.get("model", None),
                )
            },
            status=status.HTTP_200_OK,
        )

    @action(["post"], detail=False)
    def translation(self, request: Request) -> Response:
        """Convert text from one language to another."""

        # Serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "translation": client.translation(
                    text=serializer.validated_data["text"],
                    model=serializer.validated_data.get("model", None),
                    src_lang=serializer.validated_data["source"],
                    tgt_lang=serializer.validated_data["target"],
                ).translation_text
            },
            status=status.HTTP_200_OK,
        )

    @action(["post"], detail=False, url_path="zero-shot-classification")
    def zero_shot_classification(self, request: Request) -> Response:
        """Provide as input a text and a set of candidate labels to classify the input text."""

        # Serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "translation": client.zero_shot_classification(
                    text=serializer.validated_data["text"],
                    labels=serializer.validated_data["labels"],
                    multi_label=serializer.validated_data["is_multi_label"],
                    model=serializer.validated_data.get("model", None),
                )
            },
            status=status.HTTP_200_OK,
        )


class RootAPIView(APIRootView):
    """Root API View that provides links to actions."""

    # Methods to remove from response
    filters = [
        "basename",
        "description",
        "detail",
        "name",
        "suffix",
        *dir(GenericViewSet),
    ]

    # URL map
    urls = {
        "text": TextViewSet,
    }

    def get(self, request: Request, *args, **kwargs) -> Response:
        """Return urls to extra actions"""

        return Response(
            {
                k: {
                    url.replace(
                        "_",
                        "-",
                    ): f"{request.scheme}://{request.get_host()}/{k}/{url.replace('_', '-')}"
                    for url in list(
                        filter(
                            lambda f: not f.startswith("_") and f not in self.filters,
                            dir(v),
                        )
                    )
                }
                for k, v in self.urls.items()
            }
        )
