import os

from bfcl.model_handler.api_inference.openai import OpenAIHandler
from bfcl.constants.eval_config import (
    RESULT_PATH,
    VLLM_PORT,
)
from openai import OpenAI, RateLimitError


class OurQwenHandler(OpenAIHandler):
    def __init__(self, model_name, temperature) -> None:
        super().__init__(model_name, temperature)

        # Read from env vars with fallbacks
        self.vllm_host = os.getenv("VLLM_ENDPOINT", "localhost")
        self.vllm_port = os.getenv("VLLM_PORT", VLLM_PORT)

        self.base_url = f"http://{self.vllm_host}:{self.vllm_port}/v1"
        self.client = OpenAI(base_url=self.base_url, api_key="EMPTY")