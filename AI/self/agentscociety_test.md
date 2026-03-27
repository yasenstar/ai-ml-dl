# AgentSociety AI Testing

```bash
(agentsociety-main) PS D:\test\agentsociety-main> uv run --python 3.12 python -m agentsociety2.backend.run
启动 AI Social Scientist Backend API 服务...
服务地址: http://0.0.0.0:8001
API文档: http://0.0.0.0:8001/docs
健康检查: http://0.0.0.0:8001/health
日志等级: info
------------------------------------------------------------
D:\test\agentsociety-main\.venv\Lib\site-packages\websockets\legacy\__init__.py:6: DeprecationWarning: websockets.legacy is deprecated; see https://websockets.readthedocs.io/en/stable/howto/upgrade.html for upgrade instructions
  warnings.warn(  # deprecated in 14.0 - 2024-11-09
D:\test\agentsociety-main\.venv\Lib\site-packages\uvicorn\protocols\websockets\websockets_impl.py:17: DeprecationWarning: websockets.server.WebSocketServerProtocol is deprecated
  from websockets.server import WebSocketServerProtocol
D:\test\agentsociety-main\.venv\Lib\site-packages\pydantic\_internal\_config.py:323: PydanticDeprecatedSince20: Support for class-based `config` is deprecated, use ConfigDict instead. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.11/migration/
  warnings.warn(DEPRECATION_MESSAGE, DeprecationWarning)
D:\test\agentsociety-main\.venv\Lib\site-packages\pydantic\_internal\_generate_schema.py:298: PydanticDeprecatedSince20: `json_encoders` is deprecated. See https://docs.pydantic.dev/2.11/concepts/serialization/#custom-serializers for alternatives. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.11/migration/
  warnings.warn(
LiteLLM logging initialized (callbacks=[])
Model list for default (with fallbacks): [{'model_name': 'qwen3-next-80b-a3b-instruct', 'litellm_params': {'model': 'openai/qwen3-next-80b-a3b-instruct', 'api_key': 'sk-_S-GiFnRK-761AMKYcoO3g', 'api_base': 'https://cloud.infini-ai.com/maas/v1'}}, {'model_name': 'qwen3-next-80b-a3b-instruct', 'litellm_params': {'model': 'openai/qwen3-next-80b-a3b-instruct', 'api_key': 'sk-_S-GiFnRK-761AMKYcoO3g', 'api_base': 'https://cloud.infini-ai.com/maas/v1'}}]
Fallbacks: [{'qwen3-next-80b-a3b-instruct': ['qwen3-next-80b-a3b-instruct']}]
注册工具: search_literature
注册工具: load_literature
Model list for coder (with fallbacks): [{'model_name': 'glm-4.7', 'litellm_params': {'model': 'openai/glm-4.7', 'api_key': 'sk-_S-GiFnRK-761AMKYcoO3g', 'api_base': 'https://cloud.infini-ai.com/maas/v1'}}, {'model_name': 'qwen3-next-80b-a3b-instruct', 'litellm_params': {'model': 'openai/qwen3-next-80b-a3b-instruct', 'api_key': 'sk-_S-GiFnRK-761AMKYcoO3g', 'api_base': 'https://cloud.infini-ai.com/maas/v1'}}, {'model_name': 'qwen3-next-80b-a3b-instruct', 'litellm_params': {'model': 'openai/qwen3-next-80b-a3b-instruct', 'api_key': 'sk-_S-GiFnRK-761AMKYcoO3g', 'api_base': 'https://cloud.infini-ai.com/maas/v1'}}]
Fallbacks: [{'glm-4.7': ['qwen3-next-80b-a3b-instruct', 'qwen3-next-80b-a3b-instruct']}]
注册工具: experiment_config
注册工具: run_experiment
注册工具: run_shell_command
注册工具: list_directory
注册工具: read_file
注册工具: write_file
注册工具: glob
注册工具: search_file_content
注册工具: replace
注册工具: write_todos
注册工具: hypothesis
注册工具: analyze
注册工具: synthesize
注册工具: generate_paper
Completion service initialized
INFO:     Started server process [34904]
INFO:     Waiting for application startup.
AI Social Scientist Backend Service 启动中...
项目根目录: D:\test\agentsociety-main\packages\agentsociety2
已注册 16 个工具
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
INFO:     127.0.0.1:55500 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55500 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55500 - "GET /health HTTP/1.1" 200 OK
