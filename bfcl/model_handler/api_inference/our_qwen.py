import os
import time
import re

from bfcl.model_handler.api_inference.openai import OpenAIHandler
from bfcl.constants.eval_config import (
    RESULT_PATH,
    VLLM_PORT,
)
from bfcl.model_handler.utils import retry_with_backoff
from openai import OpenAI, RateLimitError


class OurQwenHandler(OpenAIHandler):
    def __init__(self, model_name, temperature) -> None:
        super().__init__(model_name, temperature)

        # Read from env vars with fallbacks
        self.vllm_host = os.getenv("VLLM_ENDPOINT", "localhost")
        self.vllm_port = os.getenv("VLLM_PORT", VLLM_PORT)

        self.base_url = f"http://{self.vllm_host}:{self.vllm_port}/v1"
        self.client = OpenAI(base_url=self.base_url, api_key="EMPTY")
    
    @retry_with_backoff(error_type=RateLimitError)
    def generate_with_backoff(self, **kwargs):
        start_time = time.time()
        api_response = self.client.chat.completions.create(**kwargs)
        end_time = time.time()
        
        # 将回答结果的<think>标签去除掉
        api_response.choices[0].message.content = re.sub(r'<\s*think\s*>.*?<\s*/\s*think\s*>', '', api_response.choices[0].message.content, flags=re.DOTALL).strip()
        return api_response, end_time - start_time
