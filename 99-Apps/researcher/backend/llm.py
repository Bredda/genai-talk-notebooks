
from langchain_openai import ChatOpenAI
from langchain_core.tools import BaseTool


def get_llm_model(model_name = 'gpt-4o-mini', temperature =0.5, tags:list[str] = [], tools: list[BaseTool] = [], structured_output = None, api_key = None):
    model = ChatOpenAI(
        model=model_name,
        temperature=temperature,
        api_key=api_key,
        streaming=True
    )
    if (structured_output):
        model = model.with_structured_output(structured_output)
    if len(tools) > 0:
        model = model.bind_tools(tools)
    if len(tags):
        print(f"Setting tags: {tags}")
        model = model.with_config(tags=tags)

    return model