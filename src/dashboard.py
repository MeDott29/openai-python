from typing import List, Optional, Union

from src.openai.types.audio.transcription_create_params import \
    TranscriptionCreateParams
from src.openai.types.beta.thread_create_and_run_params import (
    Thread, ThreadCreateAndRunParams, Tool)
from src.openai.types.beta.threads.message_create_params import \
    MessageCreateParams
from src.openai.types.create_embedding_response import CreateEmbeddingResponse
from src.openai.types.file_create_params import FileCreateParams
from typing_extensions import Literal


class Dashboard:
    def create_message(self, content: str, role: str, file_ids: List[str], metadata: Optional[object]) -> None:
        message_params: MessageCreateParams = {
            "content": content,
            "role": role,
            "file_ids": file_ids,
            "metadata": metadata
        }
        # Call the API to create a message using message_params

    def create_and_run_thread(
        self,
        assistant_id: str,
        instructions: Optional[str],
        metadata: Optional[object],
        model: Optional[str],
        thread: Thread,
        tools: Optional[List[Tool]]
    ) -> None:
        thread_params: ThreadCreateAndRunParams = {
            "assistant_id": assistant_id,
            "instructions": instructions,
            "metadata": metadata,
            "model": model,
            "thread": thread,
            "tools": tools
        }
        # Call the API to create and run a thread using thread_params

    def create_embedding(self) -> CreateEmbeddingResponse:
        # Call the API to create an embedding
        return CreateEmbeddingResponse()

    def create_transcription(
        self,
        file: FileTypes,
        model: Union[str, Literal["whisper-1"]],
        language: str,
        prompt: str,
        response_format: Literal["json", "text", "srt", "verbose_json", "vtt"],
        temperature: float
    ) -> None:
        transcription_params: TranscriptionCreateParams = {
            "file": file,
            "model": model,
            "language": language,
            "prompt": prompt,
            "response_format": response_format,
            "temperature": temperature
        }
        # Call the API to create a transcription using transcription_params

    def create_file(self, file: FileTypes, purpose: Literal["fine-tune", "assistants"]) -> None:
        file_params: FileCreateParams = {
            "file": file,
            "purpose": purpose
        }
        # Call the API to create a file using file_params
